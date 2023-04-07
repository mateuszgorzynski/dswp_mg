import csv
from datetime import datetime

# Zadanie 1

with open('dswp_mg\zamowienia.csv', 'r+', newline='', encoding='utf-8') as plik_csv, \
        open('dswp_mg\zamowienia_pl.csv', 'w', newline='', encoding='utf-8') as plik_pl, \
        open('dswp_mg\zamowienia_de.csv', 'w', newline='', encoding='utf-8') as plik_de:
    kolumny = ['Kraj', 'Sprzedawca', 'Data Zamowienia', 'idZamowenia', 'Utarg']
    reader = csv.DictReader(plik_csv, delimiter=';')
    writer = csv.DictWriter(plik_csv, fieldnames=kolumny)
    writer_polska = csv.DictWriter(plik_pl, fieldnames=kolumny)
    writer_niemcy = csv.DictWriter(plik_de, fieldnames=kolumny)
    writer_polska.writeheader()
    writer_niemcy.writeheader()
    for wiersz in reader:
        wiersz['Utarg'] = wiersz['Utarg'].replace('zł', '')
        wiersz['Utarg'] = wiersz['Utarg'].replace(',', '.')
        wiersz['Utarg'] = wiersz['Utarg'].replace(' ', '')
        wiersz['Data zamowienia'] = datetime.strptime(
            wiersz['Data zamowienia'], '%d.%m.%Y').strftime('%Y-%m-%d')

        if wiersz['Kraj'] == 'Polska':
            # writer_polska.writerow(wiersz)
            print(f'Wiersz polski: {wiersz}')
        elif wiersz['Kraj'] == 'Niemcy':
            # writer_niemcy.writerow(wiersz)
            print(f'Wiersz niemiecki: {wiersz}')
