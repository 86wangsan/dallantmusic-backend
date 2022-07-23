from sqlalchemy import Boolean, Column, String, Enum
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from app.db.session import Base
from app.core.enums import UserType


class User(Base):
    __tablename__ = "user"

    id = Column(
        INTEGER(display_width=11, unsigned=True), primary_key=True, index=True
    )
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    name = Column(String(255))
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean(), default=False)
    user_type = Column(Enum(UserType))
    phone_number = Column(String(13))
    level = Column(String(255))
    purpose = Column(String(255))
    credit = relationship(
        "Credit",
        back_populates="own_student",
        cascade="all, delete",
        passive_deletes=True,
    )
