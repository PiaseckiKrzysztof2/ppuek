# Zadanie 8-4.5 - Dane z e-maila
# Co robi: korzysta z funkcji z modułu emails i wypisuje nadawcę, odbiorcę,
#          temat i treść e-maila zapisanego w pliku email.txt.

import emails                                # własny moduł (plik emails.py w tym samym folderze)

print('Sender:   ', emails.email_sender())
print('Recipient:', emails.email_recipient())
print('Subject:  ', emails.email_subject())
print('Body:')
print(emails.email_body())
