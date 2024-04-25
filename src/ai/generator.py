
import os
from dotenv import load_dotenv
from vertexai.generative_models import GenerativeModel, Part
import sqlite3

# Load the environment variables
load_dotenv()

# Define the env var
MODEL = os.getenv("MODEL")

def get_gemini_response(question, prompt):
    """
    This function is used to generate content using the generative model.

    Parameters:
    question (str): The question to be answered.
    prompt (str): The prompt for the model.

    Returns:
    str: An SQL query string.
    """
    try:
        model =GenerativeModel(MODEL)
    except ImportError as e:
        print(f"Error: {e}")
        raise RuntimeError("Failed to load the model") from e
    try:
        response = model.generate_content([question, prompt[0]])
    except Exception as e:
        print(f"Error: {e}")
        raise RuntimeError("Failed to generate content") from e
    return response.text

def read_sql_query(sql, db):
    """
    This function retrieves and returns the SQL query from the database.

    Parameters:
    sql (str): The SQL query to be executed.
    db (str): The database name.

    Returns:
    
    list (optional): A list of query results if the query returns multiple rows.
                    This behavior depends on how the query and results are stored.
    """
    try:
        conn=sqlite3.connect(db)
    except Exception as e:
        print(f"Error: {e}")
        raise RuntimeError("Failed to connect to the database") from e
    try: 
        cur=conn.cursor()
    except Exception as e:
        print(f"Error: {e}")
        raise RuntimeError("Failed to create cursor") from e
    try:
        cur.execute(sql)
    except Exception as e:
        print(f"Error: {e}")
        print("sql", sql)
        raise RuntimeError("Failed to execute the SQL query") from e
    try:
        rows=cur.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Error: {e}")
        raise RuntimeError("Failed to fetch all rows") from e
    try:
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
        raise RuntimeError("Failed to commit the changes") from e
    try:
        conn.close()
    except Exception as e:
        print(f"Error: {e}")
        raise RuntimeError("Failed to close the connection") from e
    return rows

prompt_text = [
"""
**You are an expert in converting English text to SQL queries!**

**Goal:** Generate an accurate SQL query that retrieves the desired information from the `STUDENT` database table based on the questions asked by the users.

**NOTE**: 
    Your whole job is to convert the user's question into a SQL query ONLY.
    DO NOT give any further explanations for the SQL query. 
    The database schema is provided below for reference. 
    You can assume that the database is already populated with data. 
    The SQL query should be generated based on the user's question.

**Database Name:** `STUDENT`
**Database Type:** SQLite
**Database File:** `student.db`
**Database Tables:** `STUDENT`
**Database Columns:** `NAME`, `CLASS`, `SECTION`, `MARKS`

**Database Schema:**

The `STUDENT` table has the following columns:

* `NAME` (VARCHAR(25)): Name of the student
* `CLASS` (VARCHAR(25)): Class the student belongs to
* `SECTION` (VARCHAR(25)): Section the student belongs to (optional)
* `MARKS` (INT(3)): Marks obtained by the student

**Examples:**

* **Question:** Question: How many students are there in the database?
* **Query:** `SELECT COUNT(*) AS Total_Students FROM STUDENT;`

* **Question:** How many students are there in each class??
* **Query:** `SELECT CLASS, COUNT(*) AS Total_Students FROM STUDENT GROUP BY CLASS;`

* **Question:** What is the average marks of students in each class?
* **Query:** `SELECT CLASS, AVG(MARKS) AS Average_Marks FROM STUDENT GROUP BY CLASS;`

* **Question:** What is the total number of students in each class?
* **Query:** `SELECT CLASS, COUNT(*) AS Total_Students FROM STUDENT GROUP BY CLASS;`

**Let's get started!**

Please ask your question about the `STUDENT` database, and I'll do my \
    best to generate the corresponding SQL query.
"""
]
