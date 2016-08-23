from database import Database

class ContactEntries:
        """save contacts in the db"""

        def __init__(self, name, my_number):
            self.name = name
            self.my_number = my_number

        def add_contact(self):
            """
            save the contact in a dict with the phone number as a key
            """
            contact_dict = {}
            contact_dect[self.my_number] = self.name
            db_connect = Database()
            db_connect.add_contact(self.name, self.my_number)

class ContactSearch:

    def __init__(self, name):
        self.name = name

    def search_contact_list(self):
        """
        search in the db by contact 
        name using  db class instance
        """
        search_db = Database()
        result = search_db.search_by_name(self.name)
        for items, values in result:
            # print str(i[1]), i[2]
            print values
        return result
    