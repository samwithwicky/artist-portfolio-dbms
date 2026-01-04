# 🎨 Artist Portfolio Management System (DBMS Project)

A database-driven artist portfolio management system built using **MySQL** and **Flask**, designed to demonstrate core **DBMS concepts** such as **ER modeling, normalization (3NF), relational constraints, and SQL operations**, integrated with a functional web interface.

---

## 📌 Project Overview

The Artist Portfolio Management System allows artists to manage portfolios and artworks, categorize them efficiently, and display artworks through a clean gallery interface.  
This project applies theoretical DBMS concepts to a real-world application.

---

## 🎯 Objectives

- Design a normalized relational database schema
- Implement one-to-many and many-to-many relationships
- Enforce referential integrity using constraints
- Integrate SQL queries with a backend application
- Provide a simple and functional frontend

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS  
- **Backend:** Python (Flask)  
- **Database:** MySQL  
- **Connectivity:** MySQL Connector (Python)

---

## 🗂️ Database Design

### Entities
- **Artist**
- **Portfolio**
- **Artwork**
- **Category**
- **Artwork_Category** (associative table)

### Relationships
- One Artist → Many Portfolios  
- One Portfolio → Many Artworks  
- Many Artworks ↔ Many Categories  

The many-to-many relationship between artworks and categories is resolved using an associative table to maintain normalization.

---

## 🧱 Normalization

The database is normalized up to **Third Normal Form (3NF)**:

- **1NF:** Atomic attributes  
- **2NF:** No partial dependency  
- **3NF:** No transitive dependency  

This ensures minimal redundancy and strong data integrity.

---

## 📂 Project Structure

```

artist-portfolio-dbms/
│
├── app.py              # Flask application
├── schema.sql          # Database schema
├── setup_db.py         # Database setup script
│
├── templates/
│   ├── gallery.html    # Artwork gallery
│   ├── add.html        # Add artwork page
│   └── edit.html       # Edit artwork page
│
├── static/
│   ├── style.css       # Stylesheet
│   └── images/         # Artwork images
│
└── README.md

````

---

## 🚀 Features

- Add, edit, and delete artworks
- Organize artworks into portfolios
- Categorize artworks using multiple categories
- Display artworks in a gallery view
- Gmail-style image preview
- Enforced referential integrity with cascading deletes

---

## 🧪 DBMS Concepts Implemented

- Primary and foreign keys
- Constraints (`UNIQUE`, `CHECK`)
- Cascading deletes (`ON DELETE CASCADE`)
- Many-to-many relationship resolution
- SQL joins and CRUD operations
- ER modeling and normalization

---

## ▶️ How to Run


````
1. Create the database and tables:
   ```sql
   SOURCE schema.sql;

2. Install required dependencies:

   ```bash
   pip install flask mysql-connector-python
   ```

3. Run the application:

   ```bash
   python app.py
   ```

4. Open your browser and visit:

   ```
   http://localhost:5000
   ```
```
## 🏁 Conclusion

The Artist Portfolio Management System successfully integrates DBMS theory with application development, showcasing effective database design, normalization, and backend integration.
