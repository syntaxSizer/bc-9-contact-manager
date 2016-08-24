import os
import sys
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship

# it link ORM
Base = declarative_base()


class Firebase(Base):
	__tablename__ = 'contact_list'
	# Here we define columns for the table contact_list
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key = True, autoincrement = True)
    contact_number = column(Integer, unique = True)
    contact_name = Column(String(250), nullable = False)

    def __repr__ (self):
    	return 'contact_list: {}'.format(self.contact_list)

engine = create_engine('sqlite:///ContactStorage_sqlalchemy.db')
Base.metadata.create_all(engine)	

