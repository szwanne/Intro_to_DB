import mysql.connector

try:

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database=""
    )

    if mydb.is_connected():
        cursor = mydb.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("DATABASE called 'alx_book_store' created successfully!")


except mysql.connector.Error as e:
    print(f"Error in connecting to the database: {e}")


finally:
    if "cursor" in locals():
        cursor.close()
    if "mydb" in locals() and mydb.is_connected():
        mydb.close()
