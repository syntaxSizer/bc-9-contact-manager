import sqlite3


class Database:
    def __init__(self):
        self.con = sqlite3.connect('contacts.db')
        self.cursor = self.con.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS Contacts_Book(id INTEGER PRIMARY KEY AUTOINCREMENT, contact_name TEXT, conatct_number TEXT UNIQUE)")

    def add_contact(self, name, my_number):
        '''
        call number function
        '''
        with self.con:
        #commmits and closes connecction
            self.con.execute("INSERT INTO contact_list(NAME ,PHONENUMBER) VALUES('{}', '{}')" .format(name, my_number))

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
