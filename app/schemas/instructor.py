from typing import List, Optional
from pydantic import BaseModel
from app.schemas.credit import CreditRead
from app.schemas.lesson import LessonRead


class Student(BaseModel):
    user_id: int
    name: str


class StudentCreditList(Student):
    credit_list: List[CreditRead]


class StudentLessonHistory(Student):
    lesson_list: List[LessonRead]


class StudentInfo(Student):
    phone_number: Optional[str]
    level: Optional[str]
    purpose: Optional[str]
