from mysql.connector import connect

user = 'root'
password = 'coderslab'
host = 'localhost'
database = 'exercises_db'

def solution():
    # Tu piszemy kod    
    try:
        cnx = connect(user=user, password=password, host=host, database=database)
        print("Conncected")
        cnx.close() 
    except:
        print("Not connected")

if __name__ == "__main__":
    solution()
