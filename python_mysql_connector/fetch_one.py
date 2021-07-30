from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def query_with_fetchone():
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        
        row = cursor.fetchone()
        
        while row is not None:
            print(row)
            row = cursor.fetchone()
    except Error as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()
