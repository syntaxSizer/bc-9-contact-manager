from database import Database
from colorama import Fore, Back, Style


class ContactEntries:
    """save contacts in the db"""

    def __init__(self, name, my_number):
        self.name = name
        self.my_number = my_number

    def add_contact(self):
        try:

            contact_list = {}
            contact_list[self.my_number] = self.name
            connect_db = Database()
            connect_db.add_contact(self.name, self.my_number)
            print 'contact saved succesfully'
        except:
            print Fore.MAGENTA + '  the contact already exist '


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
        if not result:
            print Fore.RED + ' No such contact'
            return None
        if result > 1:
            print ' Which  contact ??'
        for items in result:
            if items[2] > 1:
                print ' %s  %s ' % (items[1], [items[0]])
            # elif items[0] not in result:
            #     print 'no such contact! %s' % items[1]
            else:
                print str(items[1]), items[2]

        return result
