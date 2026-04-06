create database if not exists student_db;
use student_db;
create table students(
        REGISTER_NUMBER INT Primary key,
        NAME varchar(100),
        GENDER varchar(10),
        DOB date,
        DEPARTMENT varchar(50),
        YEAR int,
        SECTION varchar(10),
		CGPA decimal(3,2),
        ADMISSION_DATE Date,
        ADDRESS varchar(200),
        CONTACT varchar(15),
        EMAIL varchar(100),
        PARENT_CONTACT varchar(15)
        );
create table if not exists users(USER_ID int primary key,
								USERNAME varchar(50),
                                PASSWORD varchar(100)
                                );                     
insert into users values(1,'admin','admin@123');
alter table students
modify REGISTER_NUMBER BIGINT;
