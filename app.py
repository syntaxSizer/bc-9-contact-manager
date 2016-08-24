# This example uses docopt with the built in cmd module to demonstrate an
# interactive command application.
"""
Usage:
    contact_manager -n <name> -p <phonenumber>    add new contact
    contact_manager search <name>                 search for a contact
    contact_manager text <name> -m <message>      send SMS
    contact_manager (-i | --interactive)
    contact_manager (-h | --help | --version)
Options:
    -i, --interactive                             Interactive Mode
    -h, --help                                    Show this screen and exit.
    
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from contacts import ContactEntries, ContactSearch
from sms import SendSms
from colorama import Fore, Back, Style
from pyfiglet import Figlet


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print("invalid command! try again")
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class Interactive (cmd.Cmd):

    f = Figlet(font='slant')
    # print Fore.RED+f.renderText('contact Manager')

    intro = Back.WHITE + Fore.RED + \
        f.renderText('Welcome to Consolia Contact Manager!')
    print'(type help for a list of commands.)'
    prompt = 'contact_manager>>> '
    file = None

    def add_contact(self, name, number):
        new_contact = ContactEntries(name, number)
        new_contact.add_contact()

    def search(self, name):
        search_item = ContactSearch(name)
        search_item.search_contact_list()

    def sms(self, name, message):
        send_msg = SendSms(name, message)
        send_msg.send_sms()
        # print 'SMS sent successfully'

    @docopt_cmd
    def do_add(self, args):
        """Usage: add -n <name> -p <phonenumber>"""
        # print/ args['<name>'], "number is ", args['<phonenumber>']
        self.add_contact(args['<name>'], args['<phonenumber>'])

    @docopt_cmd
    def do_search(self, args):
        """Usage: search search <name>"""
        self.search(args['<name>'])

    @docopt_cmd
    def do_text(self, args):
        """Usage: send <name> -m <message>..."""

        self.sms(args['<name>'], (" ".join(args['<message>'])))

    def do_quit(self, args):
        """Quits out of Interactive Mode."""

        print(Fore.BLUE + Interactive.f.renderText(' Bye O.o '))
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    Interactive().cmdloop()

print (opt)
