from pydantic import BaseModel

from app.core.enums import LessonTypeEnum
from app.models.user import User


class CreditBase(BaseModel):
    credit_type: LessonTypeEnum


class CreditCreate(CreditBase):
    own_student_id: int | User
    target_instructor_id: int | User

    class Config:
        arbitrary_types_allowed = True


class CreditUpdate(CreditBase):
    is_used: bool


class CreditRead(CreditBase):
    credit_id: int
