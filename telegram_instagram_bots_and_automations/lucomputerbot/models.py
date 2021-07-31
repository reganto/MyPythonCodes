import os
from peewee import *
from playhouse.pool import PooledMySQLDatabase

db = PooledMySQLDatabase(
        # "reganto$default", 
        'lubot',
        max_connections=8, 
        stale_timeout=200, 
        user='reganto', 
        passwd=os.environ.get('DATABASE_PASSWD'), 
        # host='reganto.mysql.pythonanywhere-services.com'
        host='localhost'
    )


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    chat_id = CharField(max_length=24, null=False, unique=True)
    username = CharField(max_length=255, null=False, unique=False)


db.create_tables([User, ], safe=True)
