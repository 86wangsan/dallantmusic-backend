from typing import Any, Dict, List, Optional, Union
from sqlalchemy import between

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.lesson import Lesson
from app.models.user import User
from app.schemas.instructor import StudentLessonHistory
from app.schemas.lesson import LessonRead, LessonCreate, LessonUpdate
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
            # Todo: fastapi HTTP error
            raise Exception("HTTP 404 Error")

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

    # def get_all_students_unused_credits_to_instructor(
    #     self,
    #     db: Session,
    #     instructor_id: int,
    # ) -> List[StudentCreditList]:
    #     student_id_list = [
    #         k
    #         for (k,) in db.query(User.id)
    #         .filter(User.id == Credit.own_student_id)
    #         .filter(Credit.target_instructor_id == 4)
    #         .distinct()
    #         .all()
    #     ]
    #     ret_list = []
    #     for student_id in student_id_list:
    #         student_obj = crud_credit.get_student_unused_credits_to_instructor(
    #             db, instructor_id, student_id
    #         )
    #         ret_list.append(student_obj)

    #     return ret_list

    # def update_is_used_to_true(self, db: Session, credit_id: int) -> Credit:
    #     credit = db.query(Credit).get(credit_id)
    #     self.update(db, db_obj=credit, obj_in={"is_used": False})
    #     return credit

    def create(self, db: Session, *, obj_in: LessonCreate) -> LessonRead:
        db_obj = Lesson(
            lesson_type=obj_in.lesson_type,
            student_id=obj_in.student_id,
            instructor_id=obj_in.instructor_id,
            date=obj_in.date,
            time=obj_in.time,
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
