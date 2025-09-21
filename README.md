# datafun-05-sql
README.md (Final Version)
DataFun-05-SQL Project

This project demonstrates how to create and query a relational database using SQLite and Python.
It includes examples of creating tables, loading data from CSV files, writing queries, and using SQL scripts.

Project Structure
datafun-05-sql/
│
├── data/  
│   ├── authors.csv  
│   └── books.csv  
│
├── books.db             # SQLite database file  
├── create_db.py         # Creates a new SQLite database  
├── load_data.py         # Loads authors and books from CSV into database  
├── query_books.py       # Queries and displays books with authors  
├── queries.py           # Runs multiple example SQL queries  
├── update_favorites.py  # Updates and queries favorite books  
├── init_db.sql          # SQL script to initialize tables and insert data  
├── requirements.txt     # Dependencies  
└── README.md            # Project documentation  

Steps to Run

Clone this repo:

git clone https://github.com/YOUR_USERNAME/datafun-05-sql.git
cd datafun-05-sql


Create and activate virtual environment:

python -m venv .venv
.venv\Scripts\activate    # Windows
source .venv/bin/activate # Mac/Linux


Install dependencies:

pip install -r requirements.txt


Run database creation and load scripts:

python load_data.py


Run queries:

python query_books.py
python queries.py


Open the database in SQLite Viewer (VS Code extension) to explore tables.
