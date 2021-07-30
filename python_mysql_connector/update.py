from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def update_user(user_id, username):
    # read database configuration
    db_config = read_db_config()
    
    # prepare query and data
    query = """ Update users
                SET username = %s 
                WHERE id = %s """
    
    data = (username, user_id)
    
    try:
        conn = MySQLConnection(**db_config)
        
        # update table
        cursor = conn.cursor()
        cursor.execute(query, data)
        
        # accept the changes
        conn.commit()
    
    except Error as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()

