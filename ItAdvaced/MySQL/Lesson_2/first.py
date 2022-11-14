import pymysql
from easygui import *

with open('pass.txt', 'r') as file:
    pw = file.read()
try:
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='Maksuwa1488',
        database='sales',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        # with connection.cursor() as cursor:
        # create_table = "CREATE TABLE `Salesmen` (id int AUTO_INCREMENT, name varchar(30) UNIQUE , PRIMARY KEY (id));"
        # create_table2 = "CREATE TABLE `Customers` (id int AUTO_INCREMENT, name varchar(30) UNIQUE, PRIMARY KEY (id));"
        # create_table3 = "CREATE TABLE `Sales` (id int AUTO_INCREMENT, nameSalesmen varchar(30),
        # nameCustomers varchar(30), nameProduct varchar(30), summa int,  PRIMARY KEY (id),
        # FOREIGN KEY (nameSalesmen) REFERENCES Salesmen (name),
        # FOREIGN KEY (nameCustomers) REFERENCES Customers (name));"
        # cursor.execute(create_table)
        # cursor.execute(create_table2)
        # cursor.execute(create_table3)
        # print("well done")
        # with connection.cursor() as cursor:
            # insert = "INSERT INTO `Salesmen` (name) VALUES ('Sasha'), ('Max');"
            # insert2 = "INSERT INTO `Customers` (name) VALUES ('Nikola'), ('Alex');"
            # insert3 = "INSERT INTO `Sales` (nameSalesmen, nameCustomers, nameProduct, summa)" \
            #           " VALUES ('Sasha', 'Nikola', 'Phone', 4535);"
            # cursor.execute(insert)
            # cursor.execute(insert2)
            # cursor.execute(insert3)
            # connection.commit()
        while True:
            box = buttonbox('Что нужно?', 'Choose', ['Все сделки', 'Все сделки продавца', 'MAX SUMM', 'MIN SUMM'])
            if box == 'Все сделки':
                with connection.cursor() as cursor:
                    select_all = "SELECT * FROM `sales`;"
                    cursor.execute(select_all)
                    result = cursor.fetchall()
                    msgbox(result)
            elif box == 'Все сделки продавца':
                enter_select_one = enterbox('Введите имя продавца', 'Enter')
                with connection.cursor() as cursor:
                    create_table = f"Select * from `sales` where nameSalesmen = '{enter_select_one}'"
                    cursor.execute(create_table)
                    result = cursor.fetchall()
                    msgbox(result)
            elif box == 'MAX SUMM':
                with connection.cursor() as cursor:
                    create_table = f"Select * from `sales` where summa = (select max(summa) from `sales`)"
                    cursor.execute(create_table)
                    result = cursor.fetchall()
                    msgbox(result)
            elif box == 'MIN SUMM':
                with connection.cursor() as cursor:
                    create_table = f"Select * from `sales` where summa = (select MIN(summa) from `sales`)"
                    cursor.execute(create_table)
                    result = cursor.fetchall()
                    msgbox(result)
            else:
                break
    finally:
        connection.close()

except Exception as ex:
    print(ex)
