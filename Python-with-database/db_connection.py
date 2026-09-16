# pyright: reportMissingImports=false
import mysql.connector
from dotenv import load_dotenv 
import os 

load_dotenv()

mydb = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

cursor = mydb.cursor()

cursor.execute("USE mydatabase")

# cursor.execute("CREATE TABLE myTable (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")

# cursor.execute("INSERT INTO myTable (name) VALUES ('John Doe')")
# cursor.execute("INSERT INTO myTable (name) VALUES ('Alice Doe')")
# cursor.execute("INSERT INTO myTable (name) VALUES ('Bob Doe')")

sql = "INSERT INTO myTable (name) \
    VALUES (%s)"
val = [('Jack Doe',), ('Joy Doe',)]

# cursor.executemany(sql, val)

mydb.commit()
cursor.execute("SELECT * FROM myTable")


results = cursor.fetchone()

for row in results:
    print(row)

# print(mydb)