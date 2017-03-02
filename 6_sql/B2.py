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

        querySelect = """SELECT * FROM Products;"""
        try:
            cursor.execute(querySelect)
            for row in cursor:
                print(row)
        except Exception:
            print("Query select not executed")

        cursor.close()
        cnx.close() 
    except Exception:
        print("Not connected")

if __name__ == "__main__":
    solution()
