import pymysql
from easygui import *


def authorization(login, password, connection):
    with connection.cursor() as cursor:
        zp = f"select name from `users` where login = '{login.lower()}' and password = '{password}';"
        if cursor.execute(zp):
            msgbox("Успешная авторизация")
        else:
            msgbox("Неверный пароль")
        connection.commit()

def registration(login, password, name, connection):
    zp = f"insert into `users` (name, login, password) values ('{name}', '{login}', '{password}');"
    with connection.cursor() as cursor:
        cursor.execute(zp)
        connection.commit()
    msgbox("Успешная регистрация")
