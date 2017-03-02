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

        query = """
            SELECT Orders.id, Products.name, Orders.description
            FROM Products
            JOIN ProductsOrders 
                ON Products.id=ProductsOrders.product_id
            JOIN Orders
                ON Orders.id=ProductsOrders.order_id
            ORDER BY Orders.id;
            """

        try:
            cursor.execute(query)

            printedOrders = []

            for (orderId, productName, orderDesc) in cursor:
                if orderId not in printedOrders:
                    print(orderDesc)
                    printedOrders.append(orderId)
                print("    " + productName)
       

        except Exception:
            print("Query not executed")

    except Exception:
        print("Not connected")

if __name__ == "__main__":
    solution()
