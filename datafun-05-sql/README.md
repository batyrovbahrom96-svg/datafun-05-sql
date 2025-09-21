# datafun-05-sql
DataFun-05-SQL
Project Description

This project demonstrates how to use Python with SQLite, a lightweight file-based database.
It shows how to:

Create a database and a table with sqlite3.

Insert sample data into a table.

Query and display records from the database.

Technologies Used

Python 3.x

SQLite3 (Python Standard Library)

Pathlib (for file paths)

Virtual environment (venv)

Git & GitHub for version control

Setup Instructions
1. Clone the Repo
git clone https://github.com/batyrovbahrom96-svg/datafun-05-sql.git
cd datafun-05-sql

2. Create and Activate Virtual Environment
python -m venv .venv
.venv\Scripts\Activate.ps1    # Windows PowerShell

3. Install Dependencies
pip install -r requirements.txt

How to Run
1. Create the Database
python create_db.py


Expected output:

Database created: True

2. Query the Database
python query_db.py


Expected output:

Students in database:
(1, 'Alice', 20)
(2, 'Bob', 22)

File Structure
datafun-05-sql/
│
├── create_db.py        # Creates database, table, inserts records
├── query_db.py         # Queries and displays records
├── .gitignore          # Files/folders ignored by git
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation

Notes

The database file example.db is ignored in .gitignore so it won’t be uploaded to GitHub.

Each run of create_db.py adds data. To reset, add DROP TABLE IF EXISTS students before the CREATE TABLE command.
