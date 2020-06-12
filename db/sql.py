from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

url = 'mysql+mysqlconnector://root:594546594546wsl@127.0.0.1:4306/qa'

engin = create_engine(url,pool_size=5)
Session = sessionmaker(bind=engin)