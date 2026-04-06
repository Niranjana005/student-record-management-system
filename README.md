# Student Record Management System

This is a console-based application developed using Python and SQL to manage student records efficiently.

## Features

* Add new student records
* View student details
* Update existing student information
* Delete student records
* Role-based access (Admin & Viewer)
* Data stored permanently using SQL database

## User Roles

### 🔐 Admin

* Requires login using username and password
* Has full control over the system

#### Admin Operations:

* Add new student records
* View all student details
* Update student information
* Delete student records

---

### 👁️ Viewer

* No login required
* Can access using student register number

#### Viewer Operations:

* View their own student details only

---

## Technologies Used

* Python
* SQL (MySQL)

## How to Run

1. Install Python
2. Set up MySQL and create the database
3. Import the `student_db.sql` file
4. Run the program:

   ```
   python main.py
   ```

## Project Description

This project demonstrates CRUD (Create, Read, Update, Delete) operations with role-based access by integrating Python with a SQL database. It includes an Admin role for managing records and a Viewer role for accessing individual student details.

## Future Improvements

* Add search functionality
* Improve user interface
* Convert into a web-based application using Flask or Django

