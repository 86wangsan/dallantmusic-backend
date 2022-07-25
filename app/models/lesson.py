from sqlalchemy import Boolean, Column, Date, ForeignKey, Enum, String, Time
from sqlalchemy.dialects.mysql import INTEGER
from app.db.session import Base
from app.core.enums import LessonTypeEnum


class Lesson(Base):
    __tablename__ = "lesson"

    id = Column(
        INTEGER(display_width=11, unsigned=True), primary_key=True, index=True
    )
    lesson_type = Column(Enum(LessonTypeEnum))
    student_id = Column(
        INTEGER(display_width=11, unsigned=True),
        ForeignKey("user.id"),
        index=True,
    )
    instructor_id = Column(
        INTEGER(display_width=11, unsigned=True),
        ForeignKey("user.id"),
        index=True,
    )
    is_charged = Column(Boolean(), default=False, index=True)
    charged_date = Column(Date(), default=None)
    date = Column(Date(), index=True)
    time = Column(Time())
    review = Column(String(5000))
