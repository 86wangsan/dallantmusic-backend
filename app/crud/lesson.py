from typing import Any, Dict, List, Optional, Union
from fastapi import HTTPException
from sqlalchemy import between

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.crud.credit import crud_credit
from app.models.credit import Credit
from app.models.lesson import Lesson
from app.models.user import User
from app.schemas.instructor import StudentLessonHistory
from app.schemas.lesson import (
    LessonDetailRead,
    LessonRead,
    LessonCreate,
    LessonUpdate,
)
import datetime
from dateutil.relativedelta import relativedelta


class CRUDLesson(CRUDBase[LessonRead, LessonCreate, LessonUpdate]):
    def get_lesson_history_of_student(
        self,
        db: Session,
        instructor_id: int,
        student_id: int,
        year: int = None,
        month: int = None,
    ) -> Optional[StudentLessonHistory]:

        user_info = (
            db.query(User.id, User.name).filter(User.id == student_id).first()
        )

        if user_info is None:
            raise HTTPException(status_code=404, detail="User not found")

        if year is not None and month is not None:
            delta_month = relativedelta(months=1)
            delta_day = relativedelta(days=-1)
            date_month = datetime.date(year, month, 1)
            credits_result = (
                db.query(
                    Lesson.id,
                    Lesson.lesson_type,
                    Lesson.date,
                    Lesson.is_charged,
                )
                .filter(Lesson.instructor_id == instructor_id)
                .filter(Lesson.student_id == student_id)
                .filter(
                    between(
                        Lesson.date,
                        date_month,
                        date_month + delta_month + delta_day,
                    )
                )
                .order_by(Lesson.date)
                .all()
            )
        else:
            credits_result = (
                db.query(
                    Lesson.id,
                    Lesson.lesson_type,
                    Lesson.date,
                    Lesson.is_charged,
                )
                .filter(Lesson.instructor_id == instructor_id)
                .filter(Lesson.student_id == student_id)
                .order_by(Lesson.date)
                .all()
            )

        ret_data = dict()
        ret_data["user_id"] = user_info[0]
        ret_data["name"] = user_info[1]
        ret_data["lesson_list"] = []
        for lesson_id, lesson_type, date, is_charged in credits_result:
            ret_data["lesson_list"].append(
                LessonRead(
                    lesson_id=lesson_id,
                    lesson_type=lesson_type.value,
                    date=date,
                    is_charged=is_charged,
                )
            )

        return StudentLessonHistory(**ret_data)

    def get_lesson_history_of_instructor(
        self,
        db: Session,
        instructor_id: int,
        student_id: int,
        year: int = None,
        month: int = None,
    ) -> Optional[StudentLessonHistory]:

        user_info = (
            db.query(User.id, User.name)
            .filter(User.id == instructor_id)
            .first()
        )

        if user_info is None:
            raise HTTPException(status_code=404, detail="User not found")

        if year is not None and month is not None:
            delta_month = relativedelta(months=1)
            delta_day = relativedelta(days=-1)
            date_month = datetime.date(year, month, 1)
            credits_result = (
                db.query(
                    Lesson.id,
                    Lesson.lesson_type,
                    Lesson.date,
                    Lesson.is_charged,
                )
                .filter(Lesson.instructor_id == instructor_id)
                .filter(Lesson.student_id == student_id)
                .filter(
                    between(
                        Lesson.date,
                        date_month,
                        date_month + delta_month + delta_day,
                    )
                )
                .order_by(Lesson.date)
                .all()
            )
        else:
            credits_result = (
                db.query(
                    Lesson.id,
                    Lesson.lesson_type,
                    Lesson.date,
                    Lesson.is_charged,
                )
                .filter(Lesson.instructor_id == instructor_id)
                .filter(Lesson.student_id == student_id)
                .order_by(Lesson.date)
                .all()
            )

        ret_data = dict()
        ret_data["user_id"] = user_info[0]
        ret_data["name"] = user_info[1]
        ret_data["lesson_list"] = []
        for lesson_id, lesson_type, date, is_charged in credits_result:
            ret_data["lesson_list"].append(
                LessonRead(
                    lesson_id=lesson_id,
                    lesson_type=lesson_type.value,
                    date=date,
                    is_charged=is_charged,
                )
            )

        return StudentLessonHistory(**ret_data)

    def create_lesson_and_disable_credit(
        self, db: Session, *, obj_in: LessonCreate
    ) -> LessonRead:
        db_obj = Lesson(
            lesson_type=obj_in.lesson_type,
            student_id=obj_in.student_id,
            instructor_id=obj_in.instructor_id,
            date=obj_in.date,
            time=obj_in.time,
            credit_id=obj_in.credit_id,
            is_charged=False,
            review=obj_in.review,
        )
        db.add(db_obj)
        credit_obj = (
            db.query(Credit).filter(Credit.id == obj_in.credit_id).first()
        )
        crud_credit.update(db, db_obj=credit_obj, obj_in={"is_used": True})
        db.commit()
        db.refresh(db_obj)
        db.refresh(credit_obj)
        ret = LessonRead(
            lesson_type=db_obj.lesson_type,
            date=db_obj.date,
            is_charged=db_obj.is_charged,
            lesson_id=db_obj.id,
        )

        return ret

    def get_lesson_detail_read(
        self, db: Session, *, lesson_id: int
    ) -> LessonDetailRead:
        lesson_obj: Lesson = (
            db.query(Lesson).filter(Lesson.id == lesson_id).first()
        )
        return LessonDetailRead(
            lesson_id=lesson_obj.id,
            lesson_type=lesson_obj.lesson_type,
            date=lesson_obj.date,
            time=lesson_obj.time,
            review=lesson_obj.review,
            is_charged=lesson_obj.is_charged,
        )

    def create(self, db: Session, *, obj_in: LessonCreate) -> LessonRead:
        db_obj = Lesson(
            lesson_type=obj_in.lesson_type,
            student_id=obj_in.student_id,
            instructor_id=obj_in.instructor_id,
            date=obj_in.date,
            time=obj_in.time,
            credit_id=obj_in.credit_id,
            review=obj_in.review,
            is_charged=False,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: Lesson,
        obj_in: Union[LessonUpdate, Dict[str, Any]]
    ) -> LessonRead:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)


crud_lesson = CRUDLesson(LessonRead)
