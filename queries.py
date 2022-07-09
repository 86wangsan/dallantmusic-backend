STUDENT_REMAINED_CREDITS = """
SELECT 
    pr.student_id, pr.lesson_type
FROM
    lessoncredit lc
        LEFT JOIN
    purchase pr ON (lc.purchase_id = pr.id)
WHERE
    instructor_id = %s
    AND student_id = %s
    AND taken_date IS NULL
ORDER BY lc.create_time
limit 10"""

INSTRUCTOR_STUDENTS_LIST = """
SELECT 
    pr.student_id, st.name
FROM
    lessoncredit lc
        LEFT JOIN
    purchase pr ON (lc.purchase_id = pr.id)
        INNER JOIN
    student st ON (pr.student_id = st.id)
WHERE
    lc.instructor_id = %s
        AND taken_date IS NULL
GROUP BY pr.student_id;
"""
