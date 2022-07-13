import datetime
import enum
from typing import List, Optional
from pydantic import BaseModel


class LessonTypeEnum(enum.Enum):
    type50 = "type50"
    type75 = "type75"
    type100 = "type100"
    typePostPay = "typePostPay"


class Credit(BaseModel):
    creditId: int
    creditType: LessonTypeEnum


class Student(BaseModel):
    userId: int
    name: str


class Lesson(BaseModel):
    lessonId: int
    lessonType: LessonTypeEnum
    date: datetime.date
    isCharged: bool


class StudentCreditList(Student):
    creditList: List[Credit]


class StudentLessonHistory(Student):
    lessonList: List[Lesson]


class StudentInfo(Student):
    phoneNumber: str
    level: str
    purpose: str


class InstructorMainMenuData(BaseModel):
    studentList: List[StudentCreditList]
