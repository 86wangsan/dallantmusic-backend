import enum
from typing import List, Optional
from pydantic import BaseModel


class CreditTypeEnum(enum.Enum):
    type50 = "type50"
    type75 = "type75"
    type100 = "type100"
    typePostPay = "typePostPay"


class Credit(BaseModel):
    creditId: int
    creditType: CreditTypeEnum


class StudentSchema(BaseModel):
    userId: int
    name: str
    creditList: List[Credit]


class InstructorMainMenuData(BaseModel):
    studentList: List[StudentSchema]
