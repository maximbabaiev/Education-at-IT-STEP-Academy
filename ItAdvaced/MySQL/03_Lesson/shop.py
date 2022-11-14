from easygui import *
import pymysql


def selectAll(connection):
    with connection.cursor() as cursor:
        cursor.execute("select * from `products`;")
        output_product = cursor.fetchall()
        return output_product

