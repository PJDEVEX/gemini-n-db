
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
    str: The generated content.
    """
    try:
        model =GenerativeModel(MODEL)
    except ImportError as e:
        print(f"Error: {e}")
        raise RuntimeError("Failed to load the model") from e
    try:
        response = model.generate_content([question, prompt])
    except Exception as e:
        print(f"Error: {e}")
        raise RuntimeError("Failed to generate content") from e
    return response.text

def read_sql_query(sql, db):
    """
    This function retrieves and returns the SQL query from the database.

    Parameters:
    sql (str): The SQL query to be executed to potentially retrieve the actual query string.
    db (str): The database name.

    Returns:
    str (optional): The retrieved SQL query string (if stored in the database).
    list (optional): A list of query results if the query returns multiple rows.
                    This behavior depends on how the query and results are stored.
    """
    try:
        with sqlite3.connect(db) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()

            if len(rows) == 1:
                return rows[0][0]  # Assuming single row, single column for query string
            elif len(rows) > 1:
                return [row[0] for row in rows]  # Return list of results (optional)
            else:
                # Handle the case where no rows are returned (optional)
                return None  # Or raise an exception if expected

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        raise

    except Exception as e:
        print(f"Error: {e}")
        raise

prompt=[
    """
    You are an expert in converting English text to SQL query!
    The SQL database has the name STUDENT and has following columns - NAME, \
    CLASS, SECTION. \n\n Fro example, \nExample 1: How many entries of records \
    are present?, the SQL command will be like SELECT COUNT(*) FROM STUDENTS; \n \
    Example 2: What are the names of students in class 10?, the SQL command will \
    be like SELECT NAME FROM STUDENTS WHERE CLASS = 10; \n\n also sql code should \
    not have ``` in the beginning and end and sql word in output. If you get any \
    error in configuration, please ask user to getting touch with the admin. \
   

"""
]