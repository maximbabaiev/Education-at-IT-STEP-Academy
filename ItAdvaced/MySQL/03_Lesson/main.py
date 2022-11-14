from easygui import *
import pymysql
from puth import authorization, registration
from add_table import start


# log_pass = multpasswordbox("Enter login and password:", "Enter", ["Login:", "Pass:"])

try:
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user="root",
        password="Maksuwa1488",
        database='basket',
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Welcome")
    try:
        while True:
            zapros = buttonbox("Choose", "Enter", ["Authorization", "Registration"])
            if zapros == "Authorization":
                log_pass1 = multpasswordbox("Enter login and password:", "Enter", ["Login:", "Pass"])
                authorization(login=log_pass1[0], password=log_pass1[1], connection=connection)
            elif zapros == "Registration":
                log_pass1 = multpasswordbox("Enter login and password:", "Enter", ["Name:", "Login:", "Pass:"])
                registration(log_pass1[1], log_pass1[2], log_pass1[0], connection)
            else:
                break
    finally:
        connection.close()
except Exception as ex:
    print(ex)
