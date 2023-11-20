# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# URL_DATABASE='mysql+pymysql://root:root@localhost:3306/STUDENT'

# engin = create_engine(URL_DATABASE)
# Sessionlocal =sessionmaker(autocommit=False,autoflush=False,bind=engin)

# Base =declarative_base()
from urllib.parse import quote
from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv
from pathlib import Path
# Replace 'your_username' and 'your_password' with your actual PostgreSQL username and password
# Replace 'localhost' with the actual hostname or IP address of your PostgreSQL server
# Replace '5432' with the actual port number if it's different
# Replace 'STUDENT' with the name of your PostgreSQL database
env_path =Path('.')/'.env'
load_dotenv(dotenv_path=env_path)
password =os.getenv('password')
encoded = quote(password)
URL_DATABASE = f'postgresql://postgres:{encoded}@localhost:5433/test'

engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
