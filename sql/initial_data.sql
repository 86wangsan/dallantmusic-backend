insert into instructor (name) values ('이해정');


insert into student (name, phone_number, level, purpose)
values ('유승헌', '010-4650-8532', '전공 중 고 재수생', '해외 대학원 입학');
insert into student (name, phone_number, level, purpose)
values ('남궁승헌', '010-4650-8532', '전공 중 고 재수생', '해외 대학원 입학');
insert into student (name, phone_number, level, purpose)
values ('김지수', '010-4650-8532', '전공 중 고 재수생', '해외 대학원 입학');
insert into student (name, phone_number, level, purpose)
values ('유지연', '010-4650-8532', '전공 중 고 재수생', '해외 대학원 입학');
insert into student (name, phone_number, level, purpose)
values ('박정남', '010-4650-8532', '전공 중 고 재수생', '해외 대학원 입학');



insert into purchase (student_id, lesson_type, lesson_count, amount, payment_by)
values (1, '50분', 12, 960000, '현금결제');
insert into lessoncredit (purchase_id, instructor_id, taken_date)
values (1, 1, '2022-02-14')
;
insert into lesson (student_id, instructor_id, credit_id, review)
values (1, 1, 1, "오늘 열심히 하였습니다.");
insert into lessoncredit (purchase_id, instructor_id, taken_date)
values (1, 1, '2022-02-10')
;
insert into lesson (student_id, instructor_id, credit_id, review)
values (1, 1, 2, "정말 열심히 하였습니다.");
insert into lessoncredit (purchase_id, instructor_id)
values (1, 1)
;
insert into lessoncredit (purchase_id, instructor_id)
values (1, 1)
;
insert into lessoncredit (purchase_id, instructor_id)
values (1, 1)
;
insert into lessoncredit (purchase_id, instructor_id)
values (1, 1)
;
insert into lessoncredit (purchase_id, instructor_id)
values (1, 1)
;
insert into lessoncredit (purchase_id, instructor_id)
values (1, 1)
;
insert into lessoncredit (purchase_id, instructor_id)
values (1, 1)
;
insert into lessoncredit (purchase_id, instructor_id)
values (1, 1)
;
insert into lessoncredit (purchase_id, instructor_id)
values (1, 1)
;