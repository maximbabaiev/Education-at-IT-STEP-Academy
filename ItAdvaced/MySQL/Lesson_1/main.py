import pymysql

try:
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='Maksuwa1488',
        database='people',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
            # create database
        # with connection.cursor() as cursor:
        #     create_database = "create database `People`"
        #     cursor.execute(create_database)
        #     connection.connect()

        # create table
        # with connection.cursor() as cursor:
        #     create_table = "CREATE table `people` (id int AUTO_INCREMENT," \
        #                    "name varchar(30)," \
        #                    "Surname varchar(30)," \
        #                    "city varchar(30)," \
        #                    "country varchar(30)," \
        #                    "dateOfBirth date, PRIMARY KEY(id));"
        #     cursor.execute(create_table)
        #     print('ok')

        # insert data
        # with connection.cursor() as cursor:
        #     insert = "INSERT INTO `people` (name," \
        #              " surname," \
        #              " city," \
        #              " country," \
        #              " dateOfBirth)" \
        #              " values ('max'," \
        #              " 'Babaiev'," \
        #              " 'Kharkiv'," \
        #              "'Ukraine'," \
        #              "'1992-02-14' );"
        #     cursor.execute(insert)
        #     connection.commit()
        #     print('ok')
        # drop data
        # with connection.cursor() as cursor:
        #     drop_table = "DROP table `people`"
        #     cursor.execute(drop_table)
        #     print('ok')
        # delete data
        # with connection.cursor() as cursor:
        #     delete_data = 'delete from `people` where name="max";'
        #     cursor.execute(delete_data)
        #     connection.commit()
        #     print('ok')
        # update data
        # with connection.cursor() as cursor:
        #     update_data = "update `people` set name='bob' where id=2"
        #     cursor.execute(update_data)
        #     connection.commit()
        #     print('ok')
        # select data
        # with connection.cursor() as cursor:
        #     select_all = "select * from `people`"
        #     cursor.execute(select_all)
        #     result = cursor.fetchall()
        #     for row in result:
        #         print(row)
    finally:
        connection.close()

except:
    print("error")
