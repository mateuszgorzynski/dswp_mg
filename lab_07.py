# Zadanie 1
from typing import Callable, Dict, List


def extract_numbers(vals: list[any]) -> list[int | float]:
    for element in vals:
        print(f'Obecny element -> {element} typ: {type(element)}')
        if not isinstance(element, int) and not isinstance(element, float):
            vals.remove(element)
    return vals


print(extract_numbers(
    ['Ala', 8, 'kotów', 3.54, 'psa', 3453, 3.4, 234, 23]))

# Zadanie 2

wyrazy = input("Wprowadź listę wyrazów oddzielonych spacją: ").split()
posortowane = sorted(wyrazy, key=lambda wyraz: len(wyraz), reverse=True)
print(posortowane)

# Zadanie 3


def sort_elements(vals: list[int | str]) -> list[int | str]:
    posortowane = sorted(vals)
    return posortowane

# Zadanie 4


def odwroc_slowa(zdanie):
    slowa = zdanie.split()
    slowa = list(map(lambda slowo: slowo.strip(",.!?"), slowa))
    wynik = list(map(lambda slowo: slowo[::-1], slowa))
    wynik = ' '.join(wynik)
    print(wynik)


odwroc_slowa('Ala ma kota!')

# Zadanie 5


def sort_dict(vals: dict[str, list[int]], func) -> int:
    for key in vals:
        vals[key].sort(key=lambda x: x)
        sorted_keys = sorted(vals.keys())
    sorted_dict = {}
    for key in sorted_keys:
        sorted_dict[key] = vals[key]

    return sorted_dict


my_dict = {'Jan': [1, 3, 4, 7], 'Adam': [
    2, -5, 10, 6], 'Kasia': [-3, 8, 0, -1]}
print(sort_dict(my_dict, max))
