import sqlite3


class Database:
    def __init__(self):
        self.contacts = sqlite3.connect("ContactStorage.db")
        self.cursor = self.contacts.cursor()

        self.contacts.execute(
            "CREATE TABLE IF NOT EXISTS contact_list(ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT ,PHONENUMBER TEXT UNIQUE )")
        # print "Name and Number stored"

    def add_contat(self, name, my_number):
        '''
        call number function
        '''
        with self.contacts:
            # commmits and closes connecction
            self.contacts.execute(
                "INSERT INTO contact_list(NAME ,PHONENUMBER) VALUES('{}', '{}')" .format(name, my_number))

    def contact_search(self, name):
        query = self.contacts.execute(
            "SELECT * from contact_list WHERE NAME LIKE '%{}%'".format(name))
        # # print query
        result = [i for i in query]
        query.close()
        return result
        # return query

    def select_search(self, my_id):
        by_id = self.contacts.execute(
            "SELECT * from contact_list WHERE ID LIKE  '{}'".format(my_id))
