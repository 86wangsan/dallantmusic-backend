import enum


class UserType(enum.Enum):
    instructor = "instructor"
    student = "student"
    administrator = "administrator"


class LessonTypeEnum(enum.Enum):
    type50 = "type50"
    type75 = "type75"
    type100 = "type100"
    typePostPay = "typePostPay"
