from http.client import UnimplementedFileMode
from typing import Any, Dict, List, Optional, Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.credit import Credit
from app.models.user import User
from app.schemas.credit import CreditCreate, CreditRead, CreditUpdate
from app.schemas.instructor import StudentCreditList


class CRUDCredit(CRUDBase[Credit, CreditCreate, CreditUpdate]):
    def get_student_unused_credits_to_instructor(
        self,
        db: Session,
        instructor_id: int,
        student_id: int,
    ) -> Optional[StudentCreditList]:

        user_info = (
            db.query(User.id, User.name).filter(User.id == student_id).first()
        )

        if user_info is None:
            # Todo: fastapi HTTP error
            raise Exception("HTTP 404 Error")

        credits_result = (
            db.query(
                Credit.id,
                Credit.credit_type,
            )
            .filter(Credit.is_used == False)
            .filter(Credit.target_instructor_id == instructor_id)
            .filter(Credit.own_student_id == student_id)
            .all()
        )

        ret_data = dict()
        ret_data["user_id"] = user_info[0]
        ret_data["name"] = user_info[1]
        ret_data["credit_list"] = []
        for credit_id, credit_type in credits_result:
            ret_data["credit_list"].append(
                {
                    "credit_id": credit_id,
                    "credit_type": credit_type.value,
                }
            )
        return ret_data

    def get_unused_credits_of_student(
        self,
        db: Session,
        instructor_id: int,
        student_id: int,
    ) -> Optional[StudentCreditList]:

        user_info = (
            db.query(User.id, User.name)
            .filter(User.id == instructor_id)
            .first()
        )

        if user_info is None:
            # Todo: fastapi HTTP error
            raise Exception("HTTP 404 Error")

        credits_result = (
            db.query(
                Credit.id,
                Credit.credit_type,
            )
            .filter(Credit.is_used == False)
            .filter(Credit.target_instructor_id == instructor_id)
            .filter(Credit.own_student_id == student_id)
            .all()
        )

        ret_data = dict()
        ret_data["user_id"] = user_info[0]
        ret_data["name"] = user_info[1]
        ret_data["credit_list"] = []
        for credit_id, credit_type in credits_result:
            ret_data["credit_list"].append(
                {
                    "credit_id": credit_id,
                    "credit_type": credit_type.value,
                }
            )
        return ret_data

    def get_all_students_unused_credits_to_instructor(
        self,
        db: Session,
        instructor_id: int,
    ) -> List[StudentCreditList]:
        student_id_list = [
            k
            for (k,) in db.query(User.id)
            .filter(User.id == Credit.own_student_id)
            .filter(Credit.target_instructor_id == instructor_id)
            .distinct()
            .all()
        ]
        ret_list = []
        for student_id in student_id_list:
            student_obj = crud_credit.get_student_unused_credits_to_instructor(
                db, instructor_id, student_id
            )
            ret_list.append(student_obj)

        return ret_list

    def get_all_inst_unused_credits_of_student(
        self,
        db: Session,
        student_id: int,
    ) -> List[StudentCreditList]:
        instructor_id_list = [
            k
            for (k,) in db.query(User.id)
            .filter(User.id == Credit.target_instructor_id)
            .filter(Credit.own_student_id == student_id)
            .distinct()
            .all()
        ]
        ret_list = []
        for instructor_id in instructor_id_list:
            instructor_obj = crud_credit.get_unused_credits_of_student(
                db, instructor_id, student_id
            )
            ret_list.append(instructor_obj)

        return ret_list

    def update_is_used_to_true(self, db: Session, credit_id: int) -> Credit:
        credit = db.query(Credit).get(credit_id)
        self.update(db, db_obj=credit, obj_in={"is_used": False})
        return credit

    def create(self, db: Session, *, obj_in: CreditCreate) -> Credit:
        db_obj = Credit(
            own_student_id=obj_in.own_student_id,
            target_instructor_id=obj_in.target_instructor_id,
            credit_type=obj_in.credit_type,
            is_used=obj_in.is_used,
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


crud_credit = CRUDCredit(Credit)
