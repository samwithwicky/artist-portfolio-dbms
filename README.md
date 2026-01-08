# 🎨 Creator Portfolio Management System (DBMS Project)

A database-driven **creator portfolio management system** built using **Flask** and **SQL**, designed to demonstrate core **DBMS concepts** such as **ER modeling, normalization (3NF), relational constraints, and CRUD operations**, integrated with a functional and polished web interface.

---

## 📌 Project Overview

The Creator Portfolio Management System allows creators to maintain **multiple portfolios** for different creative domains (e.g. illustration, video editing, photography) and showcase their work through an interactive gallery.

This project bridges **theoretical DBMS concepts** with a **real-world web application**, making it suitable for academic evaluation as well as practical demonstration.

---

## 🎯 Objectives

* Design a normalized relational database schema
* Implement one-to-many relationships
* Enforce data integrity through constraints
* Integrate SQL queries with a backend application
* Build a functional, user-friendly frontend
* Demonstrate complete CRUD operations

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS, Bootstrap
* **Backend:** Python (Flask)
* **Database:** SQLite (demo) / MySQL-compatible schema
* **Templating Engine:** Jinja2

> 🔹 *SQLite is used for local demonstration due to ease of setup.
> The schema and queries are designed to be compatible with MySQL for deployment.*

---

## 🗂️ Database Design

### Entities

* **User** – stores authentication details
* **Portfolio** – represents a creative domain owned by a user
* **Work** – individual artworks or videos within a portfolio

### Relationships

* One **User** → Many **Portfolios**
* One **Portfolio** → Many **Works**

This structure ensures clear ownership and scalability.

---

## 🧱 Normalization

The database is normalized up to **Third Normal Form (3NF)**:

* **1NF:** All attributes are atomic
* **2NF:** No partial dependencies
* **3NF:** No transitive dependencies

This minimizes redundancy and ensures strong data integrity.

---

## 📂 Project Structure

```
creator-portfolio/
│
├── app.py                 # Main Flask application
├── schema.sql             # Database schema
├── init_db.py             # Database initialization script
├── database.db            # SQLite database (auto-generated)
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── profile.html
│   ├── portfolio.html
│   ├── add_portfolio.html
│   └── add_work.html
│
├── static/
│   └── uploads/           # Uploaded images/videos
│
└── README.md
```

---

## 🚀 Features

* User registration and login
* Create and manage **multiple portfolios**
* Add images and videos to portfolios
* Categorize creative works
* Search and filter works by category or keyword
* Fullscreen content viewer (image/video)
* Delete portfolios and individual works
* Clean, responsive UI using Bootstrap

---

## 🧪 DBMS Concepts Implemented

* Primary keys and foreign keys
* One-to-many relationships
* Referential integrity
* Cascading logical deletes
* SQL-based CRUD operations
* ER modeling and normalization
* Backend–database integration

---

## ▶️ How to Run the Project

### 1️⃣ Initialize the database (run once)

```bash
python init_db.py
```

### 2️⃣ Start the Flask server

```bash
python app.py
```

### 3️⃣ Open in browser

```
http://127.0.0.1:5000
```

---

## 🏁 Conclusion

The Creator Portfolio Management System successfully integrates **database design principles** with **application development**, resulting in a scalable, user-friendly, and academically sound project that reflects real-world system design practices.
