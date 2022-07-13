from typing import Any

from fastapi import APIRouter, Depends, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr

from app.api.depends import (
    get_current_active_user,
    get_current_active_superuser,
)
from app.models.user import User
from app.schemas.instructor import (
    Credit,
    CreditTypeEnum,
    InstructorMainMenuData,
    StudentSchema,
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
            StudentSchema(
                userId=2,
                name="유승헌",
                creditList=[
                    Credit(creditId=1, creditType=CreditTypeEnum.type50),
                    Credit(creditId=2, creditType=CreditTypeEnum.type50),
                    Credit(creditId=3, creditType=CreditTypeEnum.type100),
                    Credit(creditId=4, creditType=CreditTypeEnum.type75),
                ],
            ),
            StudentSchema(
                userId=5,
                name="남궁승헌",
                creditList=[
                    Credit(creditId=6, creditType=CreditTypeEnum.typePostPay),
                    Credit(creditId=7, creditType=CreditTypeEnum.typePostPay),
                ],
            ),
        ]
    )
    return ret


@router.get("/student/", response_model=InstructorMainMenuData)
def get_student_list(
    current_user: User = Depends(get_current_active_user),
) -> InstructorMainMenuData:
    ret = InstructorMainMenuData(
        studentList=[
            StudentSchema(
                userId=2,
                name="유승헌",
                creditList=[
                    Credit(creditId=1, creditType=CreditTypeEnum.type50),
                    Credit(creditId=2, creditType=CreditTypeEnum.type50),
                    Credit(creditId=3, creditType=CreditTypeEnum.type100),
                    Credit(creditId=4, creditType=CreditTypeEnum.type75),
                ],
            ),
            StudentSchema(
                userId=5,
                name="남궁승헌",
                creditList=[
                    Credit(creditId=6, creditType=CreditTypeEnum.typePostPay),
                    Credit(creditId=7, creditType=CreditTypeEnum.typePostPay),
                ],
            ),
        ]
    )
    return ret
