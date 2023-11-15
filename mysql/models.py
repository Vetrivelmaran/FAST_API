from sqlalchemy import Column,Integer,String
from database import Base

class Student(Base):
    __tablename__='student'
    
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(50),unique=False)
    section=Column(String(2))