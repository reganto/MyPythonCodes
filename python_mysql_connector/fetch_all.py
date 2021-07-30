from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def query_with_fetchall():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        
        print('Total Row(s):', cursor.rowcount)
#        print(rows)
        for row in rows:
            print(row)
    
    except Error as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()
