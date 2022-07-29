from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserUpdate

from app.crud.base import CRUDBase
from app.models.credit import Credit
from app.models.user import User
from app.schemas.instructor import Student, StudentInfo


class CRUDStudent(CRUDBase[Student, UserCreate, UserUpdate]):
    def get_student_info(
        self,
        db: Session,
        student_id: int,
    ) -> Optional[StudentInfo]:

        user_info = (
            db.query(
                User.id, User.name, User.phone_number, User.level, User.purpose
            )
            .filter(User.id == student_id)
            .first()
        )

        if user_info is None:
            # Todo: fastapi HTTP error
            raise Exception("HTTP 404 Error")

        ret_data = StudentInfo(
            user_id=user_info[0],
            name=user_info[1],
            phone_number=user_info[2],
            level=user_info[3],
            purpose=user_info[4],
        )
        return ret_data

    def update_student_info(
        self,
        db: Session,
        student_id: int,
        update_info: StudentInfo,
    ) -> Optional[StudentInfo]:

        user_info: User = db.query(User).filter(User.id == student_id).first()

        update_dict = {}
        if update_info.phone_number is not None:
            update_dict["phone_number"] = update_info.phone_number
        if update_info.level is not None:
            update_dict["level"] = update_info.level
        if update_info.purpose is not None:
            update_dict["purpose"] = update_info.purpose

        self.update(db, db_obj=user_info, obj_in=update_dict)

        if user_info is None:
            # Todo: fastapi HTTP error
            raise Exception("HTTP 404 Error")

        ret_data = StudentInfo(
            user_id=user_info.id,
            name=user_info.name,
            phone_number=user_info.phone_number,
            level=user_info.level,
            purpose=user_info.purpose,
        )
        return ret_data

    def create(self, db: Session, *, obj_in: UserCreate) -> Student:
        db_obj = Credit(
            own_student_id=obj_in.own_student_id,
            target_instructor_id=obj_in.target_instructor_id,
            credit_type=obj_in.credit_type,
            is_used=False,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: User,
        obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> Student:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)


crud_student = CRUDStudent(Student)
