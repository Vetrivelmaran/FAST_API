from click import DateTime
from sqlalchemy import Column, Integer, String, DateTime, func
from database import Base

class Student(Base):
    __tablename__='studentlist'
    
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(50),unique=False)
    section=Column(String(2))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    created_by = Column(Integer, server_default='1', nullable=False)
    updated_by = Column(Integer, server_default='1', nullable=False)
    deleted_at = Column(DateTime(timezone=True), nullable=True)