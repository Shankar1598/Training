import mysql.connector

connection = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="secure_root",
  database="School"
)

# print(connection)

cursor = connection.cursor()

# create db
# cursor.execute("CREATE DATABASE Student")
# for db in cursor:
#   print(db)

# create table
# cursor.execute("CREATE TABLE students (id int, name VARCHAR(255))")
# cursor.execute("SHOW TABLES")
# for table in cursor:
#   print(table)

# insert
# cursor.execute("INSERT INTO students (id, name) VALUES (1, 'Shankar'), (2, 'Skanda'), (3, 'Soorya')")
# connection.commit()

# sql = "INSERT INTO students (id, name) VALUES (%s, %s)"
# val = [
#   (1,'Shankar'),
#   (2,'Skanda'),
#   (3,'Soorya'),
#   (4,'Padma'),
#   (5,'Rahul')
# ]
# cursor.executemany(sql, val)
# connection.commit()
# print(cursor.rowcount, "was inserted.")

# alter
# cursor.execute("ALTER TABLE students ADD COLUMN marks float")

# select
cursor.execute("SELECT * FROM students")
result = cursor.fetchall()
for row in result:
  print(row[1])

# cursor.execute("TRUNCATE TABLE students")

