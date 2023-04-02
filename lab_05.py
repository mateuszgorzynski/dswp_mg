# Zadanie 1
import math
from typing import Union, List, Tuple
import random
A = {1 / i for i in range(1, 11)}
print(f'Zbiór A: {A}')
B = {2 ** x for x in range(11)}
print(f'Zbiór B: {B}')
C = {x for x in B if x % 4 == 0}
print(f'Zbiór C: {C}')

# Zadanie 2
macierz = [[random.randint(0, 100) if i == j else 0 for i in range(4)]
           for j in range(4)]
print(macierz)

# Zadanie 3
zdanie = 'Ala ma kota!'
slowa = zdanie.split()
slowa = [slowo.strip(",.!?") for slowo in slowa]
krotki = [tuple((slowo, [ord(slowo[i]) for i in range(len(slowo))]))
          for slowo in slowa]
print(krotki)

# Zadanie 4
Num = Union[int, float]


def row_kwadratowe(a: Num, b: Num, c: Num) -> Num:
    delta = b**2 - 4 * a * c
    if (delta < 0):
        # brak pierwiastków
        return -1
    elif (delta == 0):
        # jeden pierwiastek
        x = (-b) / (2 * a)
        return x
    else:
        # równanie ma dwa pierwiastki
        x1 = (- b - math.sqrt(delta)) / (2 * a)
        x2 = (- b + math.sqrt(delta)) / (2 * a)
        return x1, x2


print(row_kwadratowe(6, 1, 3))
print(row_kwadratowe(1, 2, 1))
print(row_kwadratowe(1, 4, 1))

# Zadanie 5


def rzut_kostka(n: int) -> List[Tuple[str, int]]:
    rzuty = [0] * 6
    for i in range(n):
        rzut = random.randint(1, 6)
        rzuty[rzut-1] += 1
    wynik = []
    for i in range(6):
        wynik.append(('oczka: ' + str(i+1), 'rzutów: ' + str(rzuty[i])))
    return wynik


n = int(input("Podaj ilość rzutów: "))
wyniki = rzut_kostka(n)
for wynik in wyniki:
    print(wynik)

# Zadanie 6


def sort_string(*stringi: str) -> List[str]:
    return sorted(stringi)


stringi = input("Podaj ciągi znaków oddzielone spacjami: ").split()
posortowane = sort_string(*stringi)
print(posortowane)

# Zadanie 7


def sumuj(**punkty: int) -> int:
    return sum(punkty.values())


suma = sumuj(wisla=20, legia=15, lech=25)
print("Łączna liczba punktów: ", suma)
