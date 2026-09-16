CREATE DATABASE iant_demo;

USE iant_demo;

CREATE TABLE students (
	student_id  INT PRIMARY KEY,
    first_name  VARCHAR(20) NOT NULL,
    city        VARCHAR(20),
    dept_id		INT,
    cgpa		DECIMAL(3, 2)
); 

INSERT INTO students (student_id, first_name, city, dept_id, cgpa) VALUES
(1, 'John', 'New York', 101, 3.5),
(2, 'Alice', 'Los Angeles', 102, 3.8),
(3, 'Bob', 'Chicago', 101, 3.2),
(4, 'Eve', 'Houston', 103, 3.9),
(5, 'Charlie', 'Phoenix', 102, 3.6);


SELECT * FROM students;

USE mydatabase;

SELECT * FROM mytable;