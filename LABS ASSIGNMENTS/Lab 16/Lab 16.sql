-- ========================================
-- LAB 16 – DATABASE DESIGN & QUERIES
-- Tasks 1–4: Complete SQL Schema, Inserts & Queries
-- ========================================

-- ------------------------------
-- TASK 1: STUDENT INFORMATION SYSTEM
-- ------------------------------
CREATE DATABASE IF NOT EXISTS college;
USE college;

-- Students Table
CREATE TABLE IF NOT EXISTS Students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    date_of_birth DATE,
    enrollment_year INT
);

-- Courses Table
CREATE TABLE IF NOT EXISTS Courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100) NOT NULL,
    course_code VARCHAR(10) UNIQUE NOT NULL,
    credits INT CHECK (credits > 0)
);

-- Enrollments Table
CREATE TABLE IF NOT EXISTS Enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrollment_date DATE DEFAULT (CURRENT_DATE),
    grade CHAR(2),
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE,
    CONSTRAINT unique_enrollment UNIQUE (student_id, course_id)
);

-- Insert sample data
INSERT INTO Students (first_name, last_name, email, date_of_birth, enrollment_year) VALUES
('Alice', 'Johnson', 'alice.johnson@example.com', '2002-03-15', 2025),
('Bob', 'Smith', 'bob.smith@example.com', '2001-06-10', 2024),
('Carol', 'Lee', 'carol.lee@example.com', '2003-11-22', 2025);

INSERT INTO Courses (course_name, course_code, credits) VALUES
('Database Systems', 'DBS101', 3),
('Data Structures', 'DS102', 4),
('Operating Systems', 'OS103', 3);

INSERT INTO Enrollments (student_id, course_id, enrollment_date, grade) VALUES
(1, 1, CURDATE(), 'A'),
(1, 2, CURDATE(), 'B'),
(2, 1, CURDATE(), 'A'),
(3, 3, CURDATE(), 'B');

-- Queries
-- Fetch all courses enrolled by a student
SELECT s.first_name, s.last_name, c.course_name, c.course_code
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id
WHERE s.student_id = 1;

-- Count number of students in each course
SELECT c.course_name, COUNT(e.student_id) AS total_students
FROM Courses c
LEFT JOIN Enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name
ORDER BY total_students DESC;

-- ------------------------------
-- TASK 2: HOSPITAL MANAGEMENT SYSTEM
-- ------------------------------
CREATE DATABASE IF NOT EXISTS hospital;
USE hospital;

-- Doctors Table
CREATE TABLE IF NOT EXISTS Doctors (
    doctor_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    specialization VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Patients Table
CREATE TABLE IF NOT EXISTS Patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    phone VARCHAR(20)
);

-- Appointments Table
CREATE TABLE IF NOT EXISTS Appointments (
    appointment_id INT PRIMARY KEY AUTO_INCREMENT,
    doctor_id INT NOT NULL,
    patient_id INT NOT NULL,
    appointment_date DATE NOT NULL,
    diagnosis VARCHAR(255),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id) ON DELETE CASCADE,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO Doctors (first_name, last_name, specialization, email) VALUES
('John', 'Adams', 'Cardiology', 'john.adams@hospital.com'),
('Emily', 'Clark', 'Neurology', 'emily.clark@hospital.com');

INSERT INTO Patients (first_name, last_name, date_of_birth, phone) VALUES
('Alice', 'Miller', '1980-05-14', '9876543210'),
('Bob', 'Wilson', '1990-07-23', '9876543211');

INSERT INTO Appointments (doctor_id, patient_id, appointment_date, diagnosis) VALUES
(1, 1, '2025-10-10', 'Checkup'),
(1, 2, '2025-10-12', 'Heart Issue'),
(2, 1, '2025-10-15', 'Headache');

-- Queries
-- List all appointments for a specific doctor
SELECT d.first_name AS doctor, p.first_name AS patient, a.appointment_date, a.diagnosis
FROM Appointments a
JOIN Doctors d ON a.doctor_id = d.doctor_id
JOIN Patients p ON a.patient_id = p.patient_id
WHERE d.doctor_id = 1;

-- Retrieve patient history by patient ID
SELECT p.first_name, p.last_name, d.first_name AS doctor, a.appointment_date, a.diagnosis
FROM Appointments a
JOIN Doctors d ON a.doctor_id = d.doctor_id
JOIN Patients p ON a.patient_id = p.patient_id
WHERE p.patient_id = 1;

-- Count total patients treated by each doctor
SELECT d.first_name, d.last_name, COUNT(DISTINCT a.patient_id) AS total_patients
FROM Doctors d
LEFT JOIN Appointments a ON d.doctor_id = a.doctor_id
GROUP BY d.doctor_id, d.first_name, d.last_name;

-- ------------------------------
-- TASK 3: LIBRARY MANAGEMENT SYSTEM
-- ------------------------------
CREATE DATABASE IF NOT EXISTS library;
USE library;

-- Books Table
CREATE TABLE IF NOT EXISTS Books (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(150) NOT NULL,
    author VARCHAR(100),
    genre VARCHAR(50),
    isbn VARCHAR(20) UNIQUE,
    published_year INT,
    available_copies INT DEFAULT 1 CHECK (available_copies >= 0)
);

-- Members Table
CREATE TABLE IF NOT EXISTS Members (
    member_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    join_date DATE DEFAULT (CURDATE())
);

-- Loans Table
CREATE TABLE IF NOT EXISTS Loans (
    loan_id INT PRIMARY KEY AUTO_INCREMENT,
    book_id INT NOT NULL,
    member_id INT NOT NULL,
    loan_date DATE NOT NULL DEFAULT (CURDATE()),
    due_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES Books(book_id) ON DELETE CASCADE,
    FOREIGN KEY (member_id) REFERENCES Members(member_id) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO Books (title, author, genre, isbn, published_year, available_copies) VALUES
('The Great Gatsby', 'F. Scott Fitzgerald', 'Classic', '9780743273565', 1925, 3),
('To Kill a Mockingbird', 'Harper Lee', 'Fiction', '9780061120084', 1960, 2),
('1984', 'George Orwell', 'Dystopian', '9780451524935', 1949, 4);

INSERT INTO Members (first_name, last_name, email, join_date) VALUES
('Alice', 'Johnson', 'alice.johnson@library.com', '2024-05-10'),
('Bob', 'Smith', 'bob.smith@library.com', '2024-07-01'),
('Carol', 'Lee', 'carol.lee@library.com', '2024-08-15');

INSERT INTO Loans (book_id, member_id, loan_date, due_date, return_date) VALUES
(1, 1, '2025-10-01', '2025-10-31', NULL),
(2, 2, '2025-09-10', '2025-10-10', '2025-10-05'),
(3, 3, '2025-09-01', '2025-09-30', NULL);

-- Queries
-- Retrieve all books currently issued
SELECT b.title, m.first_name, m.last_name, l.loan_date, l.due_date
FROM Loans l
JOIN Books b ON l.book_id = b.book_id
JOIN Members m ON l.member_id = m.member_id
WHERE l.return_date IS NULL;

-- Find overdue books
SELECT b.title, m.first_name, m.last_name, l.loan_date, l.due_date
FROM Loans l
JOIN Books b ON l.book_id = b.book_id
JOIN Members m ON l.member_id = m.member_id
WHERE l.return_date IS NULL AND l.due_date < CURDATE();

-- Count number of books loaned by each member
SELECT m.first_name, m.last_name, COUNT(l.loan_id) AS total_books_loaned
FROM Members m
LEFT JOIN Loans l ON m.member_id = l.member_id
GROUP BY m.member_id, m.first_name, m.last_name;

-- ------------------------------
-- TASK 4: ONLINE SHOPPING (E-COMMERCE) DATABASE
-- ------------------------------
CREATE DATABASE IF NOT EXISTS ecommerce;
USE ecommerce;

-- Users Table
CREATE TABLE IF NOT EXISTS Users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Products Table
CREATE TABLE IF NOT EXISTS Products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10,2) NOT NULL CHECK (price >= 0),
    stock INT DEFAULT 0 CHECK (stock >= 0)
);

-- Orders Table
CREATE TABLE IF NOT EXISTS Orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10,2),
    status ENUM('Pending','Shipped','Delivered','Cancelled') DEFAULT 'Pending',
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

-- OrderDetails Table
CREATE TABLE IF NOT EXISTS OrderDetails (
    order_detail_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    price_at_purchase DECIMAL(10,2) NOT NULL CHECK (price_at_purchase >= 0),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO Users (first_name, last_name, email, password_hash) VALUES
('Alice', 'Johnson', 'alice@shop.com', 'hash1'),
('Bob', 'Smith', 'bob@shop.com', 'hash2');

INSERT INTO Products (product_name, category, price, stock) VALUES
('Laptop', 'Electronics', 1200.00, 10),
('Phone', 'Electronics', 800.00, 20),
('Headphones', 'Accessories', 150.00, 30),
('Keyboard', 'Accessories', 100.00, 15);

INSERT INTO Orders (user_id, order_date, total_amount, status) VALUES
(1, '2025-11-01', 1950.00, 'Delivered'),
(1, '2025-11-03', 800.00, 'Pending'),
(2, '2025-11-02', 250.00, 'Delivered');

INSERT INTO OrderDetails (order_id, product_id, quantity, price_at_purchase) VALUES
(1, 1, 1, 1200.00),
(1, 3, 5, 150.00),
(2, 2, 1, 800.00),
(3, 4, 2, 100.00);

-- Queries
-- Retrieve all orders by a user
SELECT o.order_id, o.order_date, o.status, o.total_amount
FROM Orders o
JOIN Users u ON o.user_id = u.user_id
WHERE u.user_id = 1;

-- Find the most purchased product
SELECT p.product_name, SUM(od.quantity) AS total_sold
FROM Products p
JOIN OrderDetails od ON p.product_id = od.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_sold DESC
LIMIT 1;

-- Calculate total revenue in a given month
SELECT DATE_FORMAT(o.order_date, '%Y-%m') AS month,
       SUM(od.quantity * od.price_at_purchase) AS total_revenue
FROM Orders o
JOIN OrderDetails od ON o.order_id = od.order_id
WHERE DATE_FORMAT(o.order_date, '%Y-%m') = '2025-11'
GROUP BY month;
