import sqlite3

#Connect to the Sqlite3 database
connection=sqlite3.connect("student.db")

#Create a cursor object using the cursor() method
cursor=connection.cursor()

#Create a table in the database
table_info="""
Create table STUDENT (NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT(3));

"""

cursor.execute(table_info)

#Insert a row of data
cursor.execute("""INSERT INTO STUDENT VALUES ('John', 'Data Science', 'A', 90)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('Smith', 'Data Science', 'B', 85)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('David', 'Data Science', 'C',75)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('Harris', 'DEVOPS', 'D', 85)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('Chris', 'DEVOPS', 'E', 90)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('James', 'DEVOPS', 'F', 80)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('Emma', 'Data Science', 'B', 80)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('Olivia', 'Data Science', 'A', 95)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('Liam', 'Data Science', 'C', 75)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('Noah', 'DEVOPS', 'B', 78)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('Ava', 'DEVOPS', 'A', 88)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('Sophia', 'DEVOPS', 'B', 82)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('William', 'Backend Development', 'A', 92)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('Isabella', 'Backend Development', 'C', 68)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('Ethan', 'Backend Development', 'B', 85)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('Mia', 'Backend Development', 'A', 90)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('Emily', 'Data Science', 'A', 80)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('Jessica', 'Data Science', 'B', 75)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('Michael', 'Data Science', 'C', 65)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('Ryan', 'DEVOPS', 'A', 95)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('Emma', 'DEVOPS', 'B', 88)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('Sophia', 'DEVOPS', 'C', 78)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('Daniel', 'Machine Learning', 'A', 92)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('Olivia', 'Machine Learning', 'B', 85)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('William', 'Machine Learning', 'A', 88)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('Ava', 'Machine Learning', 'C', 70)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('Sophia', 'Machine Learning', 'B', 82)""")
cursor.execute("""INSERT INTO STUDENT VALUES ('Isabella', 'Machine Learning', 'A', 95)""")

# Save (commit) the changes
connection.commit()
print("Data inserted successfully")
data=cursor.execute("SELECT * FROM STUDENT")
for row in data:
    print(row)
connection.close()