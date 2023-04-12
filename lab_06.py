import csv
from datetime import datetime
import random
import unidecode
import string

# Zadanie 1

with open('dswp_mg\zamowienia.csv', 'r+', newline='', encoding='utf-8') as plik_csv, \
        open('dswp_mg\zamowienia_pl.csv', 'w', newline='', encoding='utf-8') as plik_pl, \
        open('dswp_mg\zamowienia_de.csv', 'w', newline='', encoding='utf-8') as plik_de:
    kolumny = ['Kraj', 'Sprzedawca',
               'Data zamowienia', 'idZamowienia', 'Utarg']
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
            writer_polska.writerow(wiersz)
        elif wiersz['Kraj'] == 'Niemcy':
            writer_niemcy.writerow(wiersz)

# Zadanie 2


def join_files(file_list, output_file_name):
    with open(output_file_name, 'w') as output_file:
        for file_name in file_list:
            with open(file_name) as input_file:
                output_file.write(input_file.read())


# Zadanie 3

# def ekstrema(lista, n):
#     wybor = input(
#         'Wciśnij 0 - szukanie najmniejszych wartości\nWciśnij 1 - szukanie największych wartości\n')
#     if wybor == '0':
#         wybor = False
#     elif wybor == '1':
#         wybor = True
#     if not all(isinstance(i, (int, float)) for i in lista):
#         return "Lista zawiera elementy inne niż liczby."
#     sorted_list = sorted(lista, reverse=wybor)
#     return sorted_list[:n]


# A = [random.randint(1, 100) for _ in range(1, 100)]

# print(ekstrema(A, 5))

# Zadanie 4


def create_type_dict(lst):
    result_dict = {}
    for item in lst:
        item_type = type(item).__name__
        if item_type not in result_dict:
            result_dict[item_type] = []
        result_dict[item_type].append(item)
    return result_dict


mieszana = [1, 2.3, 'Zbyszek', 5, 'Marian', 3.14]
print(create_type_dict(mieszana))

# Zadanie 5


def dziel_nazwiska(nazwiska):
    litery = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'
    indeks = litery.index('n')
    with open('dswp_mg/A-M_nazwiska.txt', 'w', newline='', encoding='utf-8') as do_m, \
            open('dswp_mg/N-Z_nazwiska.txt', 'w', newline='', encoding='utf-8') as po_m:
        for nazwisko in nazwiska:
            if nazwisko[0].lower() in litery[:indeks]:
                do_m.write(nazwisko)
                do_m.write('\n')
            elif nazwisko[0].lower() in litery[indeks:]:
                po_m.write(nazwisko)
                po_m.write('\n')


dziel_nazwiska(nazwiska=['Mamba', 'Adamiak', 'Gorzyński', 'Żeliwny',
               'Ślimak', 'Cyc', 'Lek', 'Naruto', 'Mormon'])

# Zadanie 6


def odwroc_slowa(zdanie):
    slowa = zdanie.split()
    slowa = [slowo.strip(",.!?") for slowo in slowa]
    wynik = []
    slowo_new = ''
    for slowo in slowa:
        for i in range(len(slowo)-1, -1, -1):
            slowo_new += slowo[i]
        wynik.append(slowo_new)
        slowo_new = ''
    wynik = ' '.join(wynik)
    print(wynik)


odwroc_slowa('Ala ma kota!')

# Zadanie 7


def rozdaj_karty():
    wartosci = ['As', 'Król', 'Dama', 'Walet', '10',
                '9', '8', '7', '6', '5', '4', '3', '2']
    kolory = ['pik', 'karo', 'trefl', 'kier']
    talia = [wartosc + ' ' + kolor for wartosc in wartosci for kolor in kolory]
    random.shuffle(talia)
    gracze = {'Gracz A': [], 'Gracz B': [], 'Gracz C': [], 'Gracz D': []}
    for i in range(5):
        for gracz in gracze:
            karta = talia.pop()
            gracze[gracz].append(karta)
    for gracz in gracze:
        print(f'{gracz}: {gracze[gracz]}')


rozdaj_karty()

# Zadanie 8


def init_mail(path, domena):
    with open(path, 'r', encoding='utf-8') as plik1, \
            open('dswp_mg/maile.txt', 'w', encoding='utf-8') as output:
        for linia in plik1:
            slowa = linia.split()
            imie = ' '.join(slowa)
            mail = unidecode.unidecode('.'.join(slowa).lower()) + '@' + domena
            wynik = f'{imie}, {mail}'
            output.write(wynik)
            output.write('\n')


init_mail('dswp_mg/studenci.txt', 'student.uwm.edu.pl')

# Zadanie 9


def kolo_fortuny():
    lista_hasel = []
    with open('dswp_mg/hasla.txt', 'r', encoding='utf-8') as hasla:
        for haslo in hasla:
            lista_hasel.append(haslo)

    haslo = random.choice(lista_hasel)
    zadanie = ''
    znaki = [' ', '!', ',', '.', '?']
    for char in haslo:
        if char in znaki:
            zadanie += char
        else:
            zadanie += '_'

    while '_' in zadanie:
        print(zadanie)
        wybor = int(
            input('Co chcesz teraz zrobić?\n1: Podaj literę\n2: Podaj hasło\n'))
        if wybor == 1:
            litera = str(input('Podaj literę: '))
            if litera.lower() in haslo.lower():
                print('Brawo! Litera znajduje się w haśle!')
                indeks = haslo.lower().index(litera)
                print(indeks)
                for i in range(len(haslo)):
                    if haslo[i].lower() == litera.lower():
                        zadanie = zadanie[:i] + haslo[i] + zadanie[i+1:]
            else:
                print('Litera nie znajduje się w haśle')
        elif wybor == 2:
            full_haslo = str(input('Podaj hasło:\n'))
            if full_haslo == haslo:
                print('Brawo! Podałeś prawidłowo pełne hasło!')
                zadanie = haslo
            else:
                print('Podałeś nieprawidłowe hasło!')
        else:
            print('Podano złą opcję!')
    else:
        print('Brawo, to prawidłowa odpowiedź')


kolo_fortuny()
