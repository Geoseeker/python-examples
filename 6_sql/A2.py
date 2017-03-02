from mysql.connector import connect

user = 'root'
password = 'coderslab'
host = 'localhost'
database = 'exercises_db'

def solution():
    try:
        cnx = connect(user=user, password=password, host=host, database=database)
        print("Conncected")

        cursor = cnx.cursor()

        queryCreateTable1 = """CREATE TABLE Products(
            id int AUTO_INCREMENT, 
            name varchar(255), 
            description varchar(1023),
            price float(5,2), 
            PRIMARY KEY(id));"""

        queryCreateTable2 = """CREATE TABLE Orders(
            id int AUTO_INCREMENT, 
            description varchar(1023),
            PRIMARY KEY(id));"""
            
        queryCreateTable3 = """CREATE TABLE Clients(
            id int AUTO_INCREMENT,
            name varchar(255), 
            surname varchar(255), 
            PRIMARY KEY(id));"""

        queryInsert1 = """
            INSERT INTO Products (name, description, price)
             VALUES ("Mleko", "UHT2%", 5.20);
            """
        querySelect = """
            SELECT id, name, price FROM Products;
            """

        try:
            cursor.execute(queryCreateTable1)
        except Exception:
            print("Query 1 not executed")

        try:
            cursor.execute(queryCreateTable2)
        except Exception:
            print("Query 2 not executed")

        try:
            cursor.execute(queryCreateTable3)
        except Exception:
            print("Query 3 not executed")

        try:
            cursor.execute(queryInsert1)
            cnx.commit()
        except Exception:
            # cnx.rollback()
            print("Query insert1 not executed")


        try:
            cursor.execute(querySelect)
            for (i, n, p) in cursor:
                print("{}: {}  koszuje {}".format(i, n, p))
        except Exception:
            print("Query select not executed")

        cursor.close()
        cnx.close() 
    except Exception:
        print("Not connected")

if __name__ == "__main__":
    solution()
