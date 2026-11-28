# Zadanie 8-2.3 - Kopia pliku
# Co robi: robi kopię pliku healthy_lifestyle.txt: wczytuje cały jego tekst
#          i zapisuje go do nowego pliku copy_healthy_lifestyle.txt.

original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

with open(original_file, 'r', encoding='utf-8') as file:    # encoding='utf-8' - bo w tekście są znaki typu ’
    content = file.read()                                    # cały tekst naraz

with open(target_file, 'w', encoding='utf-8') as file:
    file.write(content)                                      # zapis całego tekstu do kopii

print(f'File {original_file} has been copied to {target_file}.')
