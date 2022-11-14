import pymysql

try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="123b123b",
        database="sakila",
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Okay")
    try:
    # with connection.cursor() as cursor:
        #     create_table = "CREATE DATABASE `students`"
        #     cursor.execute(create_table)
        # Create table
        # with connection.cursor() as cursor:
        #     create_table = "CREATE TABLE `students` (id int AUTO_INCREMENT, name varchar(30), password varchar(30), PRIMARY KEY (id));"
        #     cursor.execute(create_table)
        #     print("well done")
        # Insert data
        # with connection.cursor() as cursor:
        #     insert = "INSERT INTO `students` (name, password) VALUES ('Sasha', '12345'), ('Sasha', '123456')"
        #     cursor.execute(insert)
        #     connection.commit()
        # Drope table
        # with connection.cursor() as cursor:
        #     create_table = "DROP TABLE `students`"
        #     cursor.execute(create_table)
        # Delete data
        # with connection.cursor() as cursor:
        #     create_table = "DELETE FROM `students` WHERE name='Sasha';"
        #     cursor.execute(create_table)
        #     connection.commit()
        # Update data
        # with connection.cursor() as cursor:
        #     create_table = "UPDATE `students` SET password = 'qwerty' WHERE id = 6"
        #     cursor.execute(create_table)
        #     connection.commit()
        # Select data
        # with connection.cursor() as cursor:
        #     select_all = "SELECT * FROM `students`;"
        #     cursor.execute(select_all)
        #     result = cursor.fetchall()
        #     print(result)
        #     for row in result:
        #         print(row)


    finally:
        connection.close()
except:
    print("error")