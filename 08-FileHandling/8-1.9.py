# Zadanie 8-1.9 - Pracownicy na stanowisku Software Engineer
# Co robi: czyta listę pracowników z pliku it_company.csv i wypisuje (ponumerowanych)
#          tylko tych, którzy pracują jako "Software Engineer".

file_name = 'it_company.csv'                 # w treści zadania jest literówka: it_company.txt
job_title = 'Software Engineer'

number = 1
with open(file_name, 'r') as file:
    for line in file:
        if job_title in line:                # in - czy napis zawiera tekst
            print(f'{number}. {line}', end="")
            number += 1
