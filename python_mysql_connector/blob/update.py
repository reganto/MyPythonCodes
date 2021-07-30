from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def read_file(filename):
    with open(filename, 'rb') as f:
        photo = f.read()
    return photo


def insert_user_data(username, password, photo):
    # read file
    data = read_file(photo)
    
    # insert or update user info
    query = """ INSERT INTO users (username, password, photo)
                VALUES (%s,%s,%s)"""
    
    args = (username, password, data)
    
    db_config = read_db_config()
    
    try:
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, args)
        if cursor.lastrowid:
            print('last insert id is {}'.format(cursor.lastrowid))
        else:
            print('last insert id not found')
            
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
