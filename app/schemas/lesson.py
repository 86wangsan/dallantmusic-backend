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


class LessonDetailRead(LessonRead):
    lesson_id: int
    time: datetime.time
    review: Optional[str]
    instructor_id: int
    student_id: int


class LessonCreate(LessonBase):
    time: datetime.time
    student_id: int
    instructor_id: int
    review: Optional[str] = ""
    credit_id: int


class LessonChargeUpdate(LessonBase):
    charged_date: datetime.date


class LessonReviewUpdate(BaseModel):
    lesson_type: Optional[LessonTypeEnum]
    date: Optional[datetime.date]
    time: Optional[datetime.time]
    instructor_id: Optional[int]
    student_id: Optional[int]
    review: Optional[str]
