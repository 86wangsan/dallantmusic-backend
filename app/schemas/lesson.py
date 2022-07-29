import datetime
from typing import Optional
from pydantic import BaseModel
from app.core.enums import LessonTypeEnum


class LessonBase(BaseModel):
    lesson_type: LessonTypeEnum
    date: datetime.date
    is_charged: Optional[bool] = False


class LessonRead(LessonBase):
    lesson_id: int


class LessonCreate(LessonBase):
    time: datetime.time
    student_id: int
    instructor_id: int
    review: Optional[str] = ""
    credit_id: int


class LessonUpdate(LessonBase):
    charged_date: datetime.date
