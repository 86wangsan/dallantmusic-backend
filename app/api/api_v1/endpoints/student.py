from datetime import date
import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, Path

from app.api.depends import (
    get_current_active_user,
)
from app.core.enums import LessonTypeEnum
from app.models.user import User
from app.schemas.credit import CreditCreate, CreditRead
from app.schemas.instructor import (
    StudentCreditList,
    StudentInfo,
    StudentLessonHistory,
)
from app.api.depends import get_db
from sqlalchemy.orm import Session
from app.crud.credit import crud_credit
from app.crud.student import crud_student
from app.crud.lesson import crud_lesson
from app.schemas.lesson import LessonCreate, LessonRead

router = APIRouter()


@router.get("/instructorlist", response_model=List[StudentCreditList])
def get_student_list(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> List[StudentCreditList]:
    ret = crud_credit.get_all_inst_unused_credits_of_student(
        db, current_user.id
    )

    return ret


@router.get(
    "/info",
    response_model=StudentInfo,
)
def get_student_info(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> StudentInfo:
    ret = crud_student.get_student_info(db, current_user.id)
    return ret


@router.post(
    "/info",
    response_model=StudentInfo,
)
def update_student_info(
    db: Session = Depends(get_db),
    student_info: StudentInfo = None,
    current_user: User = Depends(get_current_active_user),
) -> StudentInfo:
    ret = crud_student.update_student_info(db, current_user.id, student_info)
    return ret


@router.get(
    "/instructor/credits/{instructor_id}",
    response_model=StudentCreditList,
)
def get_credits_to_instructor(
    db: Session = Depends(get_db),
    instructor_id: int = Path(
        default=1, title="the instructor's id to retrieve his/her info"
    ),
    current_user: User = Depends(get_current_active_user),
) -> Optional[StudentCreditList]:
    ret = crud_credit.get_unused_credits_of_student(
        db, instructor_id, current_user.id
    )
    return ret


# @router.post(
#     "/student/credits/{student_id}/add/{credit_type}",
#     response_model=CreditRead,
# )
# def add_credit_to_student(
#     db: Session = Depends(get_db),
#     student_id: int = Path(
#         default=1, title="the student's id to retrieve his/her info"
#     ),
#     credit_type: LessonTypeEnum = Path(
#         default="typePostPay", title="추가하고자 하는 크레딧의 type"
#     ),
#     current_user: User = Depends(get_current_active_user),
# ) -> Optional[CreditRead]:
#     type_dict = {
#         "type50": LessonTypeEnum.type50,
#         "type75": LessonTypeEnum.type75,
#         "type100": LessonTypeEnum.type100,
#         "typePostPay": LessonTypeEnum.typePostPay,
#     }
#     create_credit_obj = CreditCreate(
#         credit_type=credit_type,
#         own_student_id=student_id,
#         target_instructor_id=current_user.id,
#     )
#     db_obj = crud_credit.create(db, obj_in=create_credit_obj)
#     ret = CreditRead(credit_id=db_obj.id, credit_type=db_obj.credit_type)
#     return ret


@router.get(
    "/instructor/history/{instructor_id}",
    response_model=StudentLessonHistory,
)
def get_instructor_all_lesson_history(
    db: Session = Depends(get_db),
    instructor_id: int = Path(
        default=1, title="the student's id to retrieve his/her info"
    ),
    current_user: User = Depends(get_current_active_user),
) -> StudentLessonHistory:
    ret = crud_lesson.get_lesson_history_of_instructor(
        db, instructor_id=instructor_id, student_id=current_user.id
    )
    return ret


@router.get(
    "/instructor/history/{instructor_id}/{year}/{month}",
    response_model=StudentLessonHistory,
)
def get_student_monthly_lesson_history(
    db: Session = Depends(get_db),
    instructor_id: int = Path(
        default=1, title="the student's id to retrieve his/her info"
    ),
    year: int = Path(default=datetime.datetime.today().year, title="year"),
    month: int = Path(default=datetime.datetime.today().month, title="month"),
    current_user: User = Depends(get_current_active_user),
) -> StudentLessonHistory:
    ret = crud_lesson.get_lesson_history_of_student(
        db,
        instructor_id=instructor_id,
        student_id=current_user.id,
        year=year,
        month=month,
    )
    return ret
