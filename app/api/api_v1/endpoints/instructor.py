from datetime import date
import datetime
from typing import Any

from fastapi import APIRouter, Depends, Body, HTTPException, Path
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr

from app.api.depends import (
    get_current_active_user,
    get_current_active_superuser,
)
from app.models.user import User
from app.schemas.instructor import (
    Credit,
    Lesson,
    LessonTypeEnum,
    InstructorMainMenuData,
    Student,
    StudentCreditList,
    StudentInfo,
    StudentLessonHistory,
)
from app.schemas.user import UserRead, UserUpdate
from app.api.depends import get_db
from sqlalchemy.orm import Session
from app.crud.user import crud_user

router = APIRouter()


@router.get("/studentlist", response_model=InstructorMainMenuData)
def get_student_list(
    current_user: User = Depends(get_current_active_user),
) -> InstructorMainMenuData:
    ret = InstructorMainMenuData(
        studentList=[
            StudentCreditList(
                userId=2,
                name="유승헌",
                creditList=[
                    Credit(creditId=1, creditType=LessonTypeEnum.type50),
                    Credit(creditId=2, creditType=LessonTypeEnum.type50),
                    Credit(creditId=3, creditType=LessonTypeEnum.type100),
                    Credit(creditId=4, creditType=LessonTypeEnum.type75),
                ],
            ),
            StudentCreditList(
                userId=5,
                name="남궁승헌",
                creditList=[
                    Credit(creditId=6, creditType=LessonTypeEnum.typePostPay),
                    Credit(creditId=7, creditType=LessonTypeEnum.typePostPay),
                ],
            ),
        ]
    )
    return ret


@router.get(
    "/student/info/{studentId}",
    response_model=StudentInfo,
)
def get_student_info(
    studentId: int = Path(
        default=1, title="the student's id to retrieve his/her info"
    ),
    current_user: User = Depends(get_current_active_user),
) -> InstructorMainMenuData:
    ret = StudentInfo(
        userId=2,
        name="유승헌",
        phoneNumber="010-4650-8532",
        level="전공 중, 고, 재수생",
        purpose="해외 대학원 입학",
    )

    if studentId == 5:
        StudentInfo(
            userId=5,
            name="남궁승헌",
            phoneNumber="010-4650-8532",
            level="전공 중, 고, 재수생",
            purpose="해외 대학원 입학",
        )
    return ret


@router.get(
    "/student/credits/{studentId}",
    response_model=StudentCreditList,
)
def get_student_creditlist(
    studentId: int = Path(
        default=1, title="the student's id to retrieve his/her info"
    ),
    current_user: User = Depends(get_current_active_user),
) -> InstructorMainMenuData:
    ret = StudentCreditList(
        userId=2,
        name="유승헌",
        creditList=[
            Credit(creditId=1, creditType=LessonTypeEnum.type50),
            Credit(creditId=2, creditType=LessonTypeEnum.type50),
            Credit(creditId=3, creditType=LessonTypeEnum.type100),
            Credit(creditId=4, creditType=LessonTypeEnum.type75),
        ],
    )
    if studentId == 5:
        StudentCreditList(
            userId=5,
            name="남궁승헌",
            creditList=[
                Credit(creditId=6, creditType=LessonTypeEnum.typePostPay),
                Credit(creditId=7, creditType=LessonTypeEnum.typePostPay),
            ],
        )
    return ret


@router.get(
    "/student/history/{studentId}",
    response_model=StudentLessonHistory,
)
def get_student_all_lesson_history(
    studentId: int = Path(
        default=1, title="the student's id to retrieve his/her info"
    ),
    current_user: User = Depends(get_current_active_user),
) -> InstructorMainMenuData:
    ret = StudentLessonHistory(
        userId=2,
        name="유승헌",
        lessonList=[
            Lesson(
                lessonId=23,
                lessonType=LessonTypeEnum.type50,
                date=date(2022, 2, 8),
                isCharged=True,
            ),
            Lesson(
                lessonId=24,
                lessonType=LessonTypeEnum.type50,
                date=date(2022, 2, 10),
                isCharged=False,
            ),
            Lesson(
                lessonId=26,
                lessonType=LessonTypeEnum.type50,
                date=date(2022, 2, 14),
                isCharged=False,
            ),
        ],
    )

    if studentId == 5:
        ret = StudentLessonHistory(
            userId=5,
            name="남궁승헌",
            lessonList=[
                Lesson(
                    lessonId=23,
                    lessonType=LessonTypeEnum.type50,
                    date=date(2022, 2, 8),
                    isCharged=True,
                )
            ],
        )
    return ret


@router.get(
    "/student/history/{studentId}/{year}/{month}",
    response_model=StudentLessonHistory,
)
def get_student_monthly_lesson_history(
    studentId: int = Path(
        default=1, title="the student's id to retrieve his/her info"
    ),
    year: int = Path(default=datetime.datetime.today().year, title="year"),
    month: int = Path(default=datetime.datetime.today().month, title="month"),
    current_user: User = Depends(get_current_active_user),
) -> InstructorMainMenuData:
    ret = StudentLessonHistory(
        userId=2,
        name="유승헌",
        lessonList=[
            Lesson(
                lessonId=23,
                lessonType=LessonTypeEnum.type50,
                date=date(2022, 2, 8),
                isCharged=True,
            ),
            Lesson(
                lessonId=24,
                lessonType=LessonTypeEnum.type50,
                date=date(2022, 2, 10),
                isCharged=False,
            ),
            Lesson(
                lessonId=26,
                lessonType=LessonTypeEnum.type50,
                date=date(2022, 2, 14),
                isCharged=False,
            ),
        ],
    )

    if studentId == 5:
        ret = StudentLessonHistory(
            userId=5,
            name="남궁승헌",
            lessonList=[
                Lesson(
                    lessonId=23,
                    lessonType=LessonTypeEnum.type50,
                    date=date(2022, 2, 8),
                    isCharged=True,
                )
            ],
        )
    return ret
