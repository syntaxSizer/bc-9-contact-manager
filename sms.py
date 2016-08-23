from AfricasTalkingGateway import AfricasTalkingGateway
from contacts import ContactSearch


class SendTesxt:

    USERNAME = 'syntaxsizer'
    APIKEY = '34ca99d2a31142942ae5807e93aa795aa3489240b2d3f6bd3b203719c754ea5d'

    def __init__(self, to, msg):
        self.to = to
        self.msg = msg

        def send_sms(self):
            name = self.to
            to_who = ContactSearch(name)
            Contact = to_who.search_contact_list()

            if (len(Contact) > 0):
                send_to = AfricasTalkingGateway(
                    SendTesxt.USERNAME, SendTesxt.APIKEY)
                send_to.sendMessage(contact[0][2], self.message)
