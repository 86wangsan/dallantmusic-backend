-- 학생별 남아있는 크레딧 for 강사
SELECT 
    pr.student_id, pr.lesson_type
FROM
    lessoncredit lc
        LEFT JOIN
    purchase pr ON (lc.purchase_id = pr.id)
WHERE
    instructor_id = 1
    AND student_id = 1
    AND taken_date IS NULL
ORDER BY lc.create_time
limit 10;


-- 학생 수업내역 및 크레딧 정보 (강사, 학생 상세 페이지)
SELECT 
    st.name,
    st.purpose,
    st.level,
    st.phone_number,
    lc.id,
    pr.lesson_type,
    lc.taken_date
FROM
    lessoncredit lc
        INNER JOIN
    purchase pr ON (lc.purchase_id = pr.id)
        INNER JOIN
    student st ON (pr.student_id = st.id)
WHERE
    st.id = %(student_id)s
    AND lc.instructor_id = %(instructor_id)s
ORDER BY lc.taken_date desc;