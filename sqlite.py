import sqlite3

#Connect to the Sqlite3 database
connection=sqlite3.connect("student.db")

#Create a cursor object using the cursor() method
cursor=connection.cursor()

#Create a table in the database
table_info="""
Create table STUDENT (NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25));

"""

cursor.execute(table_info)

#Insert a row of data
cursor.execute("""INSERT INTO STUDENT VALUES ('John', 'Data Science', 'A')""")
cursor.execute("""INSERT INTO STUDENT VALUES ('Smith', 'Data Science', 'B')""")
cursor.execute("""INSERT INTO STUDENT VALUES ('David', 'Data Science', 'C')""")
cursor.execute("""INSERT INTO STUDENT VALUES ('Harris', 'DEVOPS', 'D')""")
cursor.execute("""INSERT INTO STUDENT VALUES ('Chris', 'DEVOPS', 'E')""")
cursor.execute("""INSERT INTO STUDENT VALUES ('James', 'DEVOPS', 'F')""")

#Commit the changes in the database
print("Data inserted successfully")
data=cursor.execute("SELECT * FROM STUDENT")
for row in data:
    print(row)