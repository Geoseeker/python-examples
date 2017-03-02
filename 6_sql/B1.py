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

        queryInsert1 = """
            INSERT INTO Products (name, description, price)
             VALUES ("Mleko", "UHT2%", 5.20);
            """

        queryInsert2 = """
            INSERT INTO Products (name, description, price)
             VALUES ("Ser", "Bialy", 10.20);
            """
        queryInsert3 = """
            INSERT INTO Products (name, description, price)
             VALUES ("Jaja", "10sztuk", 8.99);
            """
        queryInsert4 = """
            INSERT INTO Products (name, description, price)
             VALUES ("Woda", "Gazowana", 1.99);
            """
        queryInsert5 = """
            INSERT INTO Products (name, description, price)
             VALUES ("Sok", "pomidorowy", 4.60);
            """


        product = {"name":"Maslo", "description":"maslane","price":5.80}

        queryInsert6 = """INSERT INTO Products(name, description, price) 
        VALUES ({},{},{})""".format(product["name"], product["description"], product["price"])



        try:
            cursor.execute(queryInsert1)
            cnx.commit()
        except Exception:
            print("Query insert1 not executed")

        try:
            cursor.execute(queryInsert2)
            cnx.commit()

        except Exception:
            print("Query insert2 not executed")

        try:
            cursor.execute(queryInsert3)
            cnx.commit()

        except Exception:
            print("Query insert3 not executed")

        try:
            cursor.execute(queryInsert4)
            cnx.commit()

        except Exception:
            print("Query insert4 not executed")

        try:
            cursor.execute(queryInsert5)
            cnx.commit()
            
        except Exception:
            print("Query insert5 not executed")




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
