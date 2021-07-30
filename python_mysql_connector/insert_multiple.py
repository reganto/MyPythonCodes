from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def insert_users(users):
    query = "INSERT INTO users(username, password, salt) " \
            "VALUES(%s,%s,%s)"
    
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        
        cursor = conn.cursor()
        cursor.executemany(query, users)
        
        conn.commit()
        
    except Error as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()


def main():
    users = [
        ('jj.javad', '1212', 'sdasdasdasdas'),
        ('roxa', 'as22', 'sdasdasdsdasd'),
        ('sega', '1255666', 'dfstetet4')
    ]
    
    insert_users(users)

