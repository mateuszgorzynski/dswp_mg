import this
import random
import string
import sys
# Zadanie 1

num = int(input("Podaj liczbę całkowitą: "))
binarna = ""
osemkowa = ""
szesnastkowa = ""

num1 = num
num2 = num
num3 = num

while num1 > 0:
    binarna = str(num1 % 2) + binarna
    num1 = num1 // 2

while num2 > 0:
    osemkowa = str(num2 % 8) + osemkowa
    num2 = num2 // 8

while num3 > 0:
    modulo = num3 % 16
    if modulo > 9:
        szesnastkowa = string.ascii_uppercase[modulo - 10] + szesnastkowa
    else:
        szesnastkowa = str(modulo) + szesnastkowa
    num3 = num3 // 16


print("Liczba binarna: ", binarna)
print("Liczba ósemkowa: ", osemkowa)
print("Liczba szesnastkowa: ", szesnastkowa)

# Zadanie 2
liczba = input("Podaj wartość: ")

if liczba.isdigit():
    print("Podana wartość jest rzutowalna na typ int")
else:
    print("Podana wartość nie jest rzutowalna na typ int")

if liczba.replace(".", "", 1).isdigit() and liczba.count(".") <= 1 and liczba.isnumeric() == False:
    print("Podana wartość jest rzutowalna na typ float")
else:
    print("Podana wartość nie jest rzutowalna na typ float")

# Zadanie 3
print('Podaj jakąś wartość liczbową:')
liczba = int(sys.stdin.readline())

wynik = ''
wyrazenie = ''
cyfry = str(liczba)
for i in range(len(cyfry)):
    pozycja = 10**(len(cyfry)-i-1)
    cyfra = int(cyfry[i])
    wynik += f'{cyfra} * {pozycja} + '

wynik = wynik[:-2]

sys.stdout.write(f'Podaną liczbę można zapisać jako: {wynik} \n')

# Zadanie 4

# Zadanie 5
zdanie = input("Podaj zdanie: ")
slowa = zdanie.split()
slowa = [slowo.strip(",.!?") for slowo in slowa]
sort = sorted(slowa, key=lambda x: len(x))
print("Posortowane wyrazy:")
for slowo in sort:
    print(slowo)

# Zadanie 6

ilosc = int(input("Podaj ilość zdań: "))

dane = [['Koleżanki i koledzy', 'Z drugiej strony',
         'Podobnie', 'Nie zapominajmy jednak, że',
         'W ten oto sposób', 'Praktyka dnia codziennego dowodzi, że',
         'Wagi i znaczenia tych problemów nie trzeba szerzej uzasadniać, ponieważ',
         'Różnorakie i bogate doświadczenia', 'Troska organizacji, a szczególnie',
         'Wyższe założenia ideowe, a także'],
        ['realizacja nakreślonych zadań programowych',
         'zakres i miejsce szkolenia kadr',
         'stały wzrost ilości i zakres naszej aktywności',
         'aktualna struktura organizacji',
         'nowy model działalności organizacyjnej',
         'dalszy rozwój różnych form działalności',
         'stałe zabezpieczenie informacyjno programowe naszej działalności',
         'wzmacnianie i rozwijanie struktur',
         'konsultacja z szerokim aktywem',
         'rozpoczęcie powszechnej akcji kształtowania postaw'],
        ['zmusza nas do przeanalizowania', 'spełnia istotną rolę w kształtowaniu',
         'wymaga sprecyzowania i określenia', 'pomaga w przygotowaniu i realizacji',
         'zabezpiecza udział szerokiej grupie w kształtowaniu', 'spełnia ważne zadania w wypracowaniu',
         'umożliwia w większym stopniu tworzenie', 'powoduje docenianie wagi',
         'przedstawia interesującą próbę sprawdzenia', 'pociąga za sobą proces wdrażania i unowocześniania'],
        ['istniejących warunków administracyjno-finansowych.',
            'dalszych kierunków rozwoju.', 'systemu powszechnego uczestnictwa.',
            'postaw uczestników wobec zadań stawianych przez organizację.',
            'nowych propozycji.', 'kierunków postępowego wychowania.',
            'systemu szkolenia kadry odpowiadającego potrzebom.',
            'odpowiednich waruknków aktywizacji.', 'modelu rozwoju.', 'form oddziaływania.']]

zdanko = ""
for i in range(ilosc):
    for podtablica in dane:
        wylosowane_slowo = random.choice(podtablica)
        zdanko += wylosowane_slowo + " "

    zdanko = zdanko.strip()
    print(f'Zdanie nr {i+1}:\n{zdanko}')
    zdanko = ""
