from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def insert_user(username, password, salt):
    query = "INSERT INTO users(username, password, salt) " \
            "VALUES(%s,%s,%s)"
    args = (username, password, salt)
    
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        
        cursor = conn.cursor()
        cursor.execute(query, args)
        
        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')
        
        conn.commit()
        
    except Error as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()
