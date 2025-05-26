from sqlalchemy import Column, Integer, String, Date
from .database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)

class TimeOffRequest(Base):
    __tablename__ = 'requests'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    date = Column(Date)
    type = Column(String)
