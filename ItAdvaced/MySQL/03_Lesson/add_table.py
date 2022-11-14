import pymysql


def start(connection):
    with connection.cursor() as cursor:
        # create_table = "create table `users` (IDusers int auto_increment, name varchar(100)," \
        #                " login varchar(100) unique, password varchar(100),primary key (IDusers));"
        # cursor.execute(create_table)
        #
        # create_table = "create table `products` (idproducts int auto_increment, nameProduct varchar(300) unique," \
        #                "price int, primary key (idproducts));"
        # cursor.execute(create_table)

        create_table = "create table `cart` (idcart int auto_increment, LoginUser varchar(30), nameProduct varchar(30)," \
                       "price int,  primary key (idcart), foreign key (nameProduct) references products(nameProduct)," \
                       "foreign key (LoginUser) references users(login));"
        cursor.execute(create_table)
