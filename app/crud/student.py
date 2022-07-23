from http.client import UnimplementedFileMode
from typing import Any, Dict, List, Optional, Union

from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserUpdate

from app.crud.base import CRUDBase
from app.models.credit import Credit
from app.models.user import User
from app.schemas.credit import CreditCreate, CreditUpdate
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

    def create(self, db: Session, *, obj_in: CreditCreate) -> Credit:
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
        db_obj: Credit,
        obj_in: Union[CreditUpdate, Dict[str, Any]]
    ) -> Credit:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)


crud_student = CRUDStudent(Student)
