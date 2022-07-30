from fastapi import APIRouter

from app.api.api_v1.endpoints import login, users, instructor, student, lesson

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(
    instructor.router, prefix="/instructor", tags=["instructor"]
)
api_router.include_router(student.router, prefix="/student", tags=["student"])
api_router.include_router(lesson.router, prefix="/lesson", tags=["lesson"])
