from database import Database


class ContactEntries:
    """save contacts in the db"""

    def __init__(self, name, my_number):
        self.name = name
        self.my_number = my_number

    def add_contact(self):

        contact_list = {}
        # name = raw_input("Enter your name ")
        # my_number = input("Enter your Phone number ")

        contact_list[self.my_number] = self.name

        connect_db = Database()
        connect_db.add_contact(self.name, self.my_number)


class ContactSearch:

    def __init__(self, name):
        self.name = name

    def search_contact_list(self):
        """
        search in the db by contact 
        name using  db class instance
        """

        search_db = Database()
        result = search_db.contact_search(self.name)
        for items in result:
            print str(items[1]), items[2]
            # if self.name == values and self.name > 1:
            #     print "which %s ?" % self.name, values
            # print values
        return result

    # def search_by_number(self):
    #     """
    #     search in the db by contact
    #     number using  db class instance
    #     """
    #     search_db = Database()
    #     result = search_db.search_by_id(self.my_number)
    #     for items, values in result:
    #         # print str(i[1]), i[2]
    #         print items, values
    #     return result
