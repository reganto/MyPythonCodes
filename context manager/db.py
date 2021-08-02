import sqlite3
from sqlite3 import IntegrityError


path = './db.sqlite3'

# Without context manager

# connection = sqlite3.connect(path)
# cursor = connection.cursor()

# cursor.execute("""
#     CREATE TABLE users(id INTEGER PRIMARY KEY, 
#     name TEXT, email TEXT unique)
# """)
# cursor.execute("""
#     INSERT INTO users(name, email) VALUES('reganto', 'rreganto@gmail.com')
# """)
# cursor.execute("""SELECT * FROM users""")

# users = cursor.fetchall()
# connection.commit()


# With context manager

class DBHandler:
    def __init__(self, dbname):
        self.dbname = dbname
        self.connection = None
        self.cursor = None
    
    def __enter__(self):
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exctype, value, traceback):
        if exctype is IntegrityError:
            print("That email taken, try another one")
        else:
            self.connection.commit()
            self.connection.close()
        # if return True -> suppress exceptions
        # if return False -> show exceptions to user(default)
        return True


# with DBHandler("testdb") as dbhandler:
#     dbhandler.execute("""
#     CREATE TABLE users(id INTEGER PRIMARY KEY, 
#     name TEXT, email TEXT unique)""")
#     dbhandler.execute("""
#     INSERT INTO users(name, email) VALUES('reganto', 
#     'rreganto@gmail.com')
#     """)
#     dbhandler.execute("""SELECT * FROM users""")
#     users = dbhandler.fetchall()
# print(users)

