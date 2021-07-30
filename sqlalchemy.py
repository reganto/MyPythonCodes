from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


engine = create_engine('mysql+mysqldb://username:password@host:port/DBNAME')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    age = Column(Integer)


# Base.metadata.create_all(engine)

# CRUD

# Insert
# user1 = User(name='John', age=23)
# session.add(user1)
# session.commit()

# Retrive
# result = session.query(User).filter_by(name='John').first()
# print(result.name)

# Update
# record = session.query(User).filter_by(name='John').first()
# record.name = 'Jack'
# session.add(record)
# session.commit()

# Delete
# record = session.query(User).filter_by(name='Jack').first()
# session.delete(record)
# session.commit()

# Alembic
# alembic init NAME
# alembic revision -m 'NAME'
# alembic upgrade REVISION
# alembic downgrade REVISION
# alembic current --verbose
# alembic history --verbose
