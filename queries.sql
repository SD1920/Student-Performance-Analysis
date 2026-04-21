-- Create table
CREATE TABLE students (
    student_id INT,
    name VARCHAR(50),
    department VARCHAR(10),
    math INT,
    science INT,
    programming INT,
    attendance INT
);

-- 1. Display all student records
SELECT * FROM students;

-- 2. Calculate average marks of each student
SELECT name,
       ROUND((math + science + programming) / 3.0, 2) AS average_marks
FROM students;

-- 3. Identify top-performing student
SELECT name, ROUND((math + science + programming) / 3.0, 2) AS average_marks
FROM students
ORDER BY average_marks DESC
LIMIT 1;

-- 4. Department-wise average marks
SELECT department,
       ROUND(AVG((math + science + programming) / 3.0), 2) AS dept_avg
FROM students
GROUP BY department;

-- 5. Students scoring below 60 in any subject
SELECT name, math, science, programming
FROM students
WHERE math < 60 OR science < 60 OR programming < 60;

-- 6. Overall class average
SELECT ROUND(AVG((math + science + programming) / 3.0), 2) AS class_avg
FROM students;
