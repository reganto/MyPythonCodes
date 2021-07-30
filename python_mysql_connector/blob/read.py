from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def write_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)
        

def read_blob(user_id, filename='output.png'):
    query = "SELECT photo FROM users WHERE id = %s"
    
    db_config = read_db_config()
    
    try:
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, (user_id, ))
        
        photo = cursor.fetchone()[0]
#        print(type(photo[0]))

        # write data to file
        write_file(photo, filename)
        
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
