from datetime import date
import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, Path

from app.api.depends import (
    get_current_active_user,
)
from app.models.user import User
from app.schemas.credit import CreditCreate
from app.schemas.instructor import (
    Lesson,
    LessonTypeEnum,
    StudentCreditList,
    StudentInfo,
    StudentLessonHistory,
)
from app.api.depends import get_db
from sqlalchemy.orm import Session
from app.crud.credit import crud_credit
from app.crud.student import crud_student

router = APIRouter()


@router.get("/studentlist", response_model=List[StudentCreditList])
def get_student_list(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> List[StudentCreditList]:
    ret = crud_credit.get_all_students_unused_credits_to_instructor(
        db, current_user.id
    )

    return ret


@router.get(
    "/student/info/{student_id}",
    response_model=StudentInfo,
)
def get_student_info(
    db: Session = Depends(get_db),
    student_id: int = Path(
        default=1, title="the student's id to retrieve his/her info"
    ),
) -> StudentInfo:
    ret = crud_student.get_student_info(db, student_id)
    return ret


@router.get(
    "/student/credits/{student_id}",
    response_model=StudentCreditList,
)
def get_student_creditlist(
    db: Session = Depends(get_db),
    student_id: int = Path(
        default=1, title="the student's id to retrieve his/her info"
    ),
    current_user: User = Depends(get_current_active_user),
) -> Optional[StudentCreditList]:
    ret = crud_credit.get_student_unused_credits_to_instructor(
        db, current_user.id, student_id
    )
    return ret


@router.post(
    "/student/credits/{student_id}/add/{credit_type}",
    response_model=StudentCreditList,
)
def get_student_creditlist(
    db: Session = Depends(get_db),
    student_id: int = Path(
        default=1, title="the student's id to retrieve his/her info"
    ),
    credit_type: LessonTypeEnum = Path(
        default="typePostPay", title="추가하고자 하는 크레딧의 type"
    ),
    current_user: User = Depends(get_current_active_user),
) -> Optional[StudentCreditList]:
    type_dict = {
        "type50": LessonTypeEnum.type50,
        "type75": LessonTypeEnum.type75,
        "type100": LessonTypeEnum.type100,
        "typePostPay": LessonTypeEnum.typePostPay,
    }
    create_credit_obj = CreditCreate(
        credit_type=type_dict.get(credit_type),
        own_student_id=student_id,
        target_instructor_id=current_user.id,
    )
    ret = crud_credit.create(db, obj_in=create_credit_obj)
    return ret


@router.get(
    "/student/history/{student_id}",
    response_model=StudentLessonHistory,
)
def get_student_all_lesson_history(
    student_id: int = Path(
        default=1, title="the student's id to retrieve his/her info"
    ),
    current_user: User = Depends(get_current_active_user),
) -> StudentLessonHistory:
    ret = StudentLessonHistory(
        user_id=2,
        name="유승헌",
        lesson_list=[
            Lesson(
                lesson_id=23,
                lesson_type=LessonTypeEnum.type50,
                date=date(2022, 2, 8),
                is_charged=True,
            ),
            Lesson(
                lesson_id=24,
                lesson_type=LessonTypeEnum.type50,
                date=date(2022, 2, 10),
                is_charged=False,
            ),
            Lesson(
                lesson_id=26,
                lesson_type=LessonTypeEnum.type50,
                date=date(2022, 2, 14),
                is_charged=False,
            ),
        ],
    )

    if student_id == 3:
        ret = StudentLessonHistory(
            user_id=3,
            name="남궁승헌",
            lesson_list=[
                Lesson(
                    lesson_id=23,
                    lesson_type=LessonTypeEnum.type50,
                    date=date(2022, 2, 8),
                    is_charged=True,
                )
            ],
        )
    return ret


@router.get(
    "/student/history/{student_id}/{year}/{month}",
    response_model=StudentLessonHistory,
)
def get_student_monthly_lesson_history(
    student_id: int = Path(
        default=1, title="the student's id to retrieve his/her info"
    ),
    year: int = Path(default=datetime.datetime.today().year, title="year"),
    month: int = Path(default=datetime.datetime.today().month, title="month"),
    current_user: User = Depends(get_current_active_user),
) -> StudentLessonHistory:
    ret = StudentLessonHistory(
        user_id=2,
        name="유승헌",
        lesson_list=[
            Lesson(
                lesson_id=23,
                lesson_type=LessonTypeEnum.type50,
                date=date(2022, 2, 8),
                is_charged=True,
            ),
            Lesson(
                lesson_id=24,
                lesson_type=LessonTypeEnum.type50,
                date=date(2022, 2, 10),
                is_charged=False,
            ),
            Lesson(
                lesson_id=26,
                lesson_type=LessonTypeEnum.type50,
                date=date(2022, 2, 14),
                is_charged=False,
            ),
        ],
    )

    if student_id == 3:
        ret = StudentLessonHistory(
            user_id=3,
            name="남궁승헌",
            lesson_list=[
                Lesson(
                    lesson_id=23,
                    lesson_type=LessonTypeEnum.type50,
                    date=date(2022, 2, 8),
                    is_charged=True,
                )
            ],
        )
    return ret
