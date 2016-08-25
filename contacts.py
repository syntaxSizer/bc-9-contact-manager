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
        if not result:
            print ' No such contact'
            return None
        if  result <0:
            print ' Which  contact ??'
        for items in result:
            if items[2] > 1:
                print ' %s  %s %s' % ([items[0]], items[1], items[2])
            else:
                print str(items[1]), items[2]

        return result 

    def search_by_number(self):
        """
        search in the db by contact
        number using  db class instance
        """
        
        search_db = Database()

        result = search_db.number_search(self.my_number)
        if len(result) == 0:
            print 'no such number found try search by name'
            return
        for k, v in result.items():
            print(k,v)
        return result
