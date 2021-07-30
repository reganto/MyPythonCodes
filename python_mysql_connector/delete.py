from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def delete_user(user_id):
    # read database configuration
    db_config = read_db_config()
    
    # prepare query and data
    query = "DELETE FROM users WHERE id = %s"
    
    try:
        conn = MySQLConnection(**db_config)
        
        # delete user
        cursor = conn.cursor()
        cursor.execute(query, (user_id, ))
        
        # accept the changes
        conn.commit()
        
    except Error as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()
