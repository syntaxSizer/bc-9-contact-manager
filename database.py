import sqlite3


class Database:
    def __init__(self):
        self.contacts = sqlite3.connect("ContactStorage.db")
        self.cursor = self.contacts.cursor()

        self.contacts.execute(
            "CREATE TABLE IF NOT EXISTS contact_list(ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT ,PHONENUMBER TEXT UNIQUE )")
        # print "Name and Number stored"

    def add_contact(self, name, my_number):
        '''
        insert the conatact the db
        '''
        with self.contacts:
            # commmits and closes connecction
            self.contacts.execute(
                "INSERT INTO contact_list(NAME ,PHONENUMBER) VALUES('{}', '{}')" .format(name, my_number))

    def contact_search(self, name):
        """
        query all names that equals
        to the search value 
        """
        query = self.contacts.execute(
            "SELECT * from contact_list WHERE NAME LIKE '%{}%'".format(name))
        result = [i for i in query]
        query.close()
        return result
        # return query
