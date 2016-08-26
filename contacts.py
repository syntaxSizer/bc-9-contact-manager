from colorama import Fore, Back, Style
from database import Database


class ContactEntries:
    """save contacts in the db"""

    def __init__(self, name, my_number):
        self.name = name
        self.my_number = my_number

    def add_contact(self):
        """ this function will link
        the name and the number in a dict """
        contact_list = {}
        contact_list[self.my_number] = self.name
        connect_db = Database()
        connect_db.add_contact(self.name, self.my_number)


class ContactSearch:
    counter = 0

    def __init__(self, name):
        self.name = name

    def search_contact_list(self):
        """
        search in the db by contact 
        name using  db class instance
        """

        search_db = Database()
        result = search_db.contact_search(self.name)
        if not result:
            print Fore.YELLOW + ' No such contact'
            return None
        if result > 1:
            print ' Which  contact ??'
        for items in result:
            if items[2] > 1:
                print Fore.BLUE + ' %s  %s %s' % ([items[0]], items[1], items[2])
            else:
                print str(items[1]), items[2]

        return result