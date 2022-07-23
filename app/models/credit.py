from sqlalchemy import Boolean, Column, ForeignKey, Enum
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from app.db.session import Base
from app.core.enums import LessonTypeEnum


class Credit(Base):
    __tablename__ = "credit"

    id = Column(
        INTEGER(display_width=11, unsigned=True), primary_key=True, index=True
    )
    own_student_id = Column(
        INTEGER(display_width=11, unsigned=True),
        ForeignKey("user.id"),
        index=True,
    )
    own_student = relationship("User", back_populates="credit")
    target_instructor_id = Column(
        INTEGER(display_width=11, unsigned=True),
        # ForeignKey("user.id"),
        index=True,
    )
    is_used = Column(Boolean(), default=False, index=True)
    credit_type = Column(Enum(LessonTypeEnum))
