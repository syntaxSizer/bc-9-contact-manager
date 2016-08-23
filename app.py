"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    contact_manager -n <name> -p <phonenumber> [--timeout=<seconds>]
    contact_manager search <name> [--timeout=<seconds>]
    contact_manager text <name> -m <message> [--timeout=<seconds>]
    contact_manager serial <port> [--baud=<n>] [--timeout=<seconds>]
    contact_manager (-i | --interactive)
    contact_manager (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    --baud=<n>  Baudrate [default: 9600]
"""
import sys, cmd
from docopt import docopt, DocoptExit
