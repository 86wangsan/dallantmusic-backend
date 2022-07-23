import datetime
import enum
from typing import List, Optional
from pydantic import BaseModel
from app.core.enums import LessonTypeEnum
from app.schemas.credit import CreditRead


class Student(BaseModel):
    user_id: int
    name: str


class Lesson(BaseModel):
    lesson_id: int
    lesson_type: LessonTypeEnum
    date: datetime.date
    is_charged: bool


class StudentCreditList(Student):
    credit_list: List[CreditRead]


class StudentLessonHistory(Student):
    lesson_list: List[Lesson]


class StudentInfo(Student):
    phone_number: Optional[str]
    level: Optional[str]
    purpose: Optional[str]
