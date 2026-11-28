# Zadanie 8-2.4 - Zapis wybranych pracowników do pliku
# Co robi: czyta plik it_company.csv linijka po linijce i do pliku software_engineer.txt
#          zapisuje tylko linijki z pracownikami na stanowisku "Software Engineer".

employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

job_title = 'Software Engineer'

with open(employees_file, 'r') as source:                # jeden plik do czytania...
    with open(position_file, 'w') as target:             # ...drugi do zapisu
        for line in source:
            if job_title in line:
                target.write(line)                       # linijka ma już \n na końcu

print(f'Employees working as {job_title} have been saved to {position_file}.')
