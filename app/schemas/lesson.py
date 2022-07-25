import datetime
from pydantic import BaseModel
from app.core.enums import LessonTypeEnum


class LessonBase(BaseModel):
    lesson_type: LessonTypeEnum
    date: datetime.date
    is_charged: bool


class LessonRead(LessonBase):
    lesson_id: int


class LessonCreate(LessonBase):
    time: datetime.time
    student_id: int
    instructor_id: int
    review: str


class LessonUpdate(LessonBase):
    charged_date: datetime.date
