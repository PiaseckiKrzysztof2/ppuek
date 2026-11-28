# Zadanie 8-4.5 - Moduł emails
# Co robi: MODUŁ z funkcjami, które wyrażeniami regularnymi wyciągają z pliku email.txt:
#          nadawcę, odbiorcę, temat i treść e-maila. Używa go program 8-4.5.py.

import re

EMAIL_FILE = 'email.txt'


def read_email():
    with open(EMAIL_FILE, 'r', encoding='utf-8') as file:
        return file.read()


def email_sender():
    match = re.search(r'^From:.*<(.+?)>', read_email(), re.MULTILINE)   # linijka zaczynająca się od From:
    return match.group(1)                    # group(1) - to, co złapał nawias ( )


def email_recipient():
    match = re.search(r'^To:.*<(.+?)>', read_email(), re.MULTILINE)
    return match.group(1)


def email_subject():
    match = re.search(r'^Subject: (.*)$', read_email(), re.MULTILINE)  # MULTILINE - ^ i $ działają dla każdej linijki
    return match.group(1)


def email_body():
    match = re.search(r'\n\n(.*)', read_email(), re.DOTALL)  # treść = wszystko po pierwszej pustej linijce
    return match.group(1).strip()            # DOTALL - kropka łapie też znaki nowej linii
