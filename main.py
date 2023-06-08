import sqlalchemy
from sqlalchemy import create_engine, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase

#create a new databse data
engine = create_engine('sqlite:///alexandria.db', echo=True)

#create Alexandria databse 
Base = declarative_base()
Base.metadata.create_all(engine)

#add book table
class Book(Base):
    __tablename__ = "book"
    book_id = Column(Integer, primary_key=True)
    author= Column(String)
    title = Column(String)
    description= Column(String)
    year=Column(Integer)

    
Base.metadata.create_all(engine)

#inserting 5 books
with engine.connect() as conn:
    result = conn.execute(
        insert(Book),
        [
            {"book_id":521,"author":"Laura Mitchell","title":"The Secret Garden of Dreams","description":"A heartwarming tale about a young girl who discovers a magical garden that brings hope and healing to all who enter.","year":2009},
            {"book_id":522,"author":"Laura Mitchell","title":"The Secret Garden of Dreams","description":"A heartwarming tale about a young girl who discovers a magical garden that brings hope and healing to all who enter.","year":2009},
            {"book_id":520,"author":"Laura Mitchell","title":"The Secret Garden of Dreams","description":"A heartwarming tale about a young girl who discovers a magical garden that brings hope and healing to all who enter.","year":2009},
            {"book_id":50,"author":"Laura Mitchell","title":"The Secret Garden of Dreams","description":"A heartwarming tale about a young girl who discovers a magical garden that brings hope and healing to all who enter.","year":2009},
            {"book_id":16,"author":"Laura Mitchell","title":"The Secret Garden of Dreams","description":"A heartwarming tale about a young girl who discovers a magical garden that brings hope and healing to all who enter.","year":2009},
        ],
    )
    conn.commit()


