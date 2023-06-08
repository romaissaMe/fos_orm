import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase

#create a new databse data
engine = create_engine('sqlite:///alexandria.db', echo=True)

#create Alexandria databse 
Base = declarative_base()
Base.metadata.create_all(engine)

#add bokk table
class Book(Base):
    __tablename__ = "book"
    book_id = Column(Integer, primary_key=True)
    author= Column(String)
    title = Column(String)
    description= Column(String)
    year=Column(Integer)

    
Base.metadata.create_all(engine)


#connect to alexandria
engine.connect()