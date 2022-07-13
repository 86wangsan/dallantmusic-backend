// 공통 field
// data (성공시 존재, 에러시 null)
// error (에러시 존재, 성공시 null)

// + headers: Authorizatioin에 Bearer token 인증 사용
// request body에 세부 내용 넣기

const register_response_success = {
  data: {
    email: "sejeonglee2@gmail.com",
  },
  error: null,
};

const register_response_fail = {
  data: null,
  error: {
    code: 101,
    message: "이미 존재하는 이메일입니다.",
  },
};

const login_response_success = {
  data: {
    user_type: "instructor",
    access_token: access_token,
    token_type: "bearer",
  },
  error: null,
};

const login_response_fail = {
  data: null,
  error: {
    code: 102,
    message: "올바른 ID, PW가 아닙니다.",
  },
};

//get(Auth)
const instructor_students_list = {
  data: {
    studentList: [
      {
        userId: 2,
        name: "유승헌",
        creditList: [
          {
            creditId: 1,
            creditType: "type50",
          },
          {
            creditId: 2,
            creditType: "type50",
          },
          {
            creditId: 3,
            creditType: "type100",
          },
        ],
      },
      {
        userId: 5,
        name: "남궁승헌",
        creditList: [
          {
            creditId: 1,
            creditType: "typePostPay",
          },
          {
            creditId: 2,
            creditType: "typePostPay",
          },
        ],
      },
    ],
  },
  error: null,
};

//instructor/stinfo/2
//get(Auth)
const instructor_student_info = {
  data: {
    studentInfo: {
      userId: 2,
      name: "유승헌",
      phoneNumber: "010-4650-8532",
      level: "전공 중, 고, 재수생",
      purpose: "해외 대학원 입학",
    },
  },
  error: null,
};

//get(Auth)
const instructor_student_credits = {
  data: {
    creditList: [
      {
        creditId: 1,
        creditType: "type50",
      },
      {
        creditId: 2,
        creditType: "type50",
      },
      {
        creditId: 3,
        creditType: "type100",
      },
    ],
  },
  error: null,
};

//instructor/stlessonhist/2/2022/2
//get(Auth)
const instructor_student_lesson_history = {
  data: {
    lessonList: [
      {
        lessonId: 23,
        lessonType: "type50",
        date: "2022-02-08",
        isCharged: false,
      },
      {
        lessonId: 24,
        lessonType: "type50",
        date: "2022-02-10",
        isCharged: false,
      },
      {
        lessonId: 26,
        lessonType: "type50",
        date: "2022-02-14",
        isCharged: false,
      },
    ],
  },
  error: null,
};

//post(Auth)
//외상 크레딧 추가

//post(Auth)
//수강 내용 추가 . 수강 히스토리로 옮김. 크레딧 하나 삭제
//instructor/lessonreview/2
// request body_ {date, startTime, creditId, comment}
// response {isPosted, creditId}

//get
const student_instructor_list = {};

//get
//자기 자신 학생정보 불러오기
//post
//학생정보 수정
