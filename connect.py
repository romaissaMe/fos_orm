import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

#create a new databse data
engine = create_engine('sqlite:///alexandria.db', echo=True)

#create Alexandria databse 
Base = declarative_base()
Base.metadata.create_all(engine)

#connect to alexandria
engine.connect()