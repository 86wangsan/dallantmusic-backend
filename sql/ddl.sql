CREATE TABLE `dallantmusic`.`instructor` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(20) NOT NULL,
  `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `instructor_name` (`name` ASC) VISIBLE)
COMMENT = '강사 정보를 담은 테이블';

CREATE TABLE `dallantmusic`.`student` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(20) NOT NULL,
  `phone_number` VARCHAR(45) NULL,
  `level` VARCHAR(200) NULL,
  `purpose` VARCHAR(200) NULL,
  `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`));


CREATE TABLE `dallantmusic`.`purchase` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `student_id` INT NOT NULL,
  `lesson_type` VARCHAR(20) NOT NULL,
  `lesson_count` INT NOT NULL,
  `amount` DECIMAL NOT NULL,
  `payment_by` VARCHAR(45) NULL,
  `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`purchase_id`));


CREATE TABLE `dallantmusic`.`lesson` (
  `lesson_id` INT NOT NULL AUTO_INCREMENT,
  `student_id` INT NOT NULL,
  `instructor_id` INT NOT NULL,
  `credit_id` INT NULL,
  `postpay_id` INT NULL,
  `review` VARCHAR(800) NULL,
  `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`lesson_id`));


CREATE TABLE `dallantmusic`.`lessoncredit` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `purchase_id` INT NOT NULL,
  `instructor_id` INT,
  `taken_date` DATE NULL,
  `paid_date` DATE NULL,
  `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`));


CREATE TABLE `dallantmusic`.`postpaycredit` (
  `id` INT NOT NULL,
  `lesson_id` INT NULL,
  `paid` TINYINT NULL DEFAULT 0,
  `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`));
