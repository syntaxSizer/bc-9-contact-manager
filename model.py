import os
import sys
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# from sqlalchemy.orm import relationship

# Declarative system used to map the classes to the actual data in the db
Base = declarative_base()


class Firebase(Base):

    __tablename__ = 'contact_list'
    id = Column(Integer, primary_key=True, autoincrement=True)
    NAME = Column(String(250), nullable= False)
    PHONENUMBER = Column(String(250), nullable =False)

    # def __repr__(self):
    # 	return 'contacts :{} {}'.format(self.NAME, self.PHONENUMBER)




 # engine is an instance of Engine, and it represents the core interface to
 # the databas
engine = create_engine('sqlite:///ContactStorage.db', echo=False)
Base.metadata.create_all(engine)
