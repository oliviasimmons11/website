import mysql.connector
#yes it is mysql.connector even though we just installed mysql-connector - idk either.


mydb = mysql.connector.connect(
   host="localhost",
   port="3306",
   user="root",
   passwd = "root",
)

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE user")
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
   print(db)
