from fastapi import APIRouter, Depends, Path

from app.api.depends import (
    get_current_active_user,
)
from app.models.user import User
from app.api.depends import get_db
from sqlalchemy.orm import Session
from app.crud.lesson import crud_lesson
from app.schemas.lesson import LessonDetailRead

router = APIRouter()


@router.get(
    "/detail/{lesson_id}",
    response_model=LessonDetailRead,
)
def get_lesson_detail(
    db: Session = Depends(get_db),
    lesson_id: int = Path(default=1, title="lesson id"),
    current_user: User = Depends(get_current_active_user),
) -> LessonDetailRead:
    ret = crud_lesson.get_lesson_detail_read(db, lesson_id=lesson_id)
    return ret
