import sqlite3
from datetime import datetime


class Database:
    def __init__(self):
        self.con = sqlite3.connect('contacts.db')
        self.cursor = self.con.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS Contacts_Book(id INTEGER PRIMARY KEY AUTOINCREMENT, created_at TIMESTAMP, contact_name TEXT, conatct_number TEXT UNIQUE)")

    def add_contact(self, contact_name, contact_number):
        with self.con:
            self.cursor.execute("INSERT INTO Contacts_book (created_at , contact_name , contact_number) VALUES('%s' '%s '%s')".format(
                datetime.now(), contact_name, contact_number))

    def search_by_name(self, arg):
        """
        Searches for contact based on name
        """
        res = self.cursor.execute(
            "SELECT * FROM Contacts_book WHERE contact_name LIKE '%{}%' ORDER BY id ".format(
                arg))
        search_result = [i for i in res]
        res.close()
        return search_result

    def search_by_id(self, my_id):
        """
        search for contact based on id
        """
        search_by_id = self.con.execute(
            "SELECT * FROM Contacts_book WHERE id LIKE '{}'".format(my_id))
