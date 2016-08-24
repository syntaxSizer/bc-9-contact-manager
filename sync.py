from firebase import firebase
from model import Firebase, Base
import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
from colorama import Fore, Back, Style


firebase = firebase.FirebaseApplication(
    'https://datasetexample.firebaseio.com/Contact_manager', None)

# from sync import contact_list
engine = create_engine('sqlite:///ContactStorage_sqlalchemy.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


class Cloude:
    '''
    this class will facilitate uploading
    and retriving the data from tghe cloude 
    '''
    def upload_firebase():
    	# dict to store the data 
        data_row = {}
        #list for the primary key
        data = []
        # my db data
        conta = session.query(Firebase).all()
        # store the data in the dict
        for i in conta:
            data_row[i.data] = [d for d in conta]

        # name = click.prompt(click.style(
        #     'Please enter your username:', fg='cyan', bold=True))
        print Fore.GREEN + 'Syncing..... '
        # ship the data to the cloude
        jsonData = firebase.put('/contacts_data', data_row)
        if jsonData:
            print Fore.CYAN + 'Done!'
            exit()
        else:
            print 'try again'
