import mysql.connector

connection = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="secure_root",
  database="School"
)

cursor = connection.cursor()

# cursor.execute("CREATE DATABASE School")

# cursor.execute("SHOW DATABASES")

# cursor.execute("CREATE TABLE students (id int, name varchar(255))")

# cursor.execute("INSERT INTO students (id, name) VALUES (2, '" + name + "')")

# sql = "INSERT INTO students (id, name) VALUES (%s, %s)"
# val = [
#   (2,'Skanda'),
#   (3,'Soorya'),
#   (4,'Padma'),
#   (5,'Rahul')
# ]

# cursor.executemany(sql, val)

# connection.commit()

# cursor.execute("ALTER TABLE students ADD COLUMN mark float")

# cursor.execute("UPDATE students SET mark=98 WHERE id=1")

# cursor.execute("UPDATE students SET mark=89 WHERE name LIKE 'S%'")

# cursor.execute("UPDATE students SET mark=85 WHERE NOT id=1")


cursor.execute("DELETE FROM students WHERE id=2")

connection.commit()

cursor.execute("SELECT * FROM students")
result = cursor.fetchall()
for row in result:
  print(row)