from AfricasTalkingGateway import AfricasTalkingGateway
from contacts import ContactSearch


class SendSms:

    USERNAME = 'syntaxsizer'
    APIKEY = '34ca99d2a31142942ae5807e93aa795aa3489240b2d3f6bd3b203719c754ea5d'

   
    def __init__(self, to, message):
        self.to = to
        self.message = message

    def send_sms(self):
        name = self.to
        who_to_send = ContactSearch(name)
        contact = who_to_send.search_contact_list()

        # who_to_send.search_contact_list()

        #
        if (len(contact) > 0):
            tosend = AfricasTalkingGateway(SendSms.USERNAME, SendSms.APIKEY)
            tosend.sendMessage(contact[0][2], self.message)
