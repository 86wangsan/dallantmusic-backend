from calendar import c
import datetime
from sqlalchemy.orm import Session
from app.core.enums import LessonTypeEnum
from app.crud.lesson import crud_lesson

from app.crud.user import crud_user
from app.crud.credit import crud_credit
from app.models.user import UserType
from app.schemas.credit import CreditCreate
from app.schemas.lesson import LessonCreate
from app.schemas.user import UserCreate
from app.core.config import settings


def init_db(db: Session) -> None:
    init_test_db(db)
    # user = crud_user.get_by_email(db, email=settings.FIRST_SUPERUSER_EMAIL)
    # if not user:
    #     user_in = UserCreate(
    #         email=settings.FIRST_SUPERUSER_EMAIL,
    #         password=settings.FIRST_SUPERUSER_PASSWORD,
    #         is_superuser=True,
    #         user_type=UserType.administrator,
    #         name="이세정",
    #     )
    #     crud_user.create_superuser(db=db, obj_in=user_in)


def init_test_db(db: Session) -> None:
    user = crud_user.get_by_email(db, email=settings.FIRST_SUPERUSER_EMAIL)
    if not user:
        crud_user.create_superuser(
            db=db,
            obj_in=UserCreate(
                email=settings.FIRST_SUPERUSER_EMAIL,
                password=settings.FIRST_SUPERUSER_PASSWORD,
                is_superuser=True,
                user_type=UserType.administrator,
                name="이세정",
            ),
        )
        crud_user.create(
            db=db,
            obj_in=UserCreate(
                email="test1@nav.com",
                password="secret1234",
                user_type=UserType.student,
                name="유승헌",
                phone_number="010-0000-0000",
                level="일반 초.중.고 음악 전공생",
                purpose="임용고시/자격증 준비",
            ),
        )
        crud_user.create(
            db=db,
            obj_in=UserCreate(
                email="test2@nav.com",
                password="secret1234",
                user_type=UserType.student,
                name="남궁승헌",
                phone_number="010-0000-0000",
                level="취미생",
                purpose="전공 희망",
            ),
        )

        crud_user.create(
            db=db,
            obj_in=UserCreate(
                email="test4@nav.com",
                password="secret1234",
                user_type=UserType.instructor,
                name="이혜정",
            ),
        )
        for _ in range(4):
            crud_credit.create(
                db,
                obj_in=CreditCreate(
                    credit_type=LessonTypeEnum.type50,
                    own_student_id=2,
                    target_instructor_id=4,
                ),
            )
        for _ in range(2):
            crud_credit.create(
                db,
                obj_in=CreditCreate(
                    credit_type=LessonTypeEnum.type75,
                    own_student_id=2,
                    target_instructor_id=4,
                ),
            )
        for _ in range(2):
            crud_credit.create(
                db,
                obj_in=CreditCreate(
                    credit_type=LessonTypeEnum.typePostPay,
                    own_student_id=3,
                    target_instructor_id=4,
                ),
            )
        crud_lesson.create(
            db,
            obj_in=LessonCreate(
                lesson_type=LessonTypeEnum.type50,
                date=datetime.date(2022, 1, 8),
                is_charged=True,
                time=datetime.time(11, 0),
                student_id=2,
                instructor_id=4,
                review="1월8일 수업입니다. 최대 5000바이트",
            ),
        )
        crud_lesson.create(
            db,
            obj_in=LessonCreate(
                lesson_type=LessonTypeEnum.type50,
                date=datetime.date(2022, 1, 10),
                is_charged=True,
                time=datetime.time(11, 0),
                student_id=2,
                instructor_id=4,
                review="1월10일 수업입니다. 최대 5000바이트",
            ),
        )
        crud_lesson.create(
            db,
            obj_in=LessonCreate(
                lesson_type=LessonTypeEnum.type50,
                date=datetime.date(2022, 1, 31),
                is_charged=True,
                time=datetime.time(11, 0),
                student_id=2,
                instructor_id=4,
                review="1월31일 수업입니다. 최대 5000바이트",
            ),
        )
        crud_lesson.create(
            db,
            obj_in=LessonCreate(
                lesson_type=LessonTypeEnum.type50,
                date=datetime.date(2022, 2, 8),
                is_charged=True,
                time=datetime.time(11, 0),
                student_id=2,
                instructor_id=4,
                review="2월8일 수업입니다. 최대 5000바이트",
            ),
        )
        crud_lesson.create(
            db,
            obj_in=LessonCreate(
                lesson_type=LessonTypeEnum.type50,
                date=datetime.date(2022, 2, 10),
                is_charged=False,
                time=datetime.time(11, 0),
                student_id=2,
                instructor_id=4,
                review="2월 10일 수업입니다. 최대 5000바이트",
            ),
        )
        crud_lesson.create(
            db,
            obj_in=LessonCreate(
                lesson_type=LessonTypeEnum.type50,
                date=datetime.date(2022, 2, 14),
                is_charged=False,
                time=datetime.time(11, 0),
                student_id=2,
                instructor_id=4,
                review="2월 14일 수업입니다. 최대 5000바이트",
            ),
        )
