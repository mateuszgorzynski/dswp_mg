import sys
from array import array
from timeit import timeit
from collections import Counter, deque
import random
import time


# Zadanie 1
def zadanie1():
    setup = """
    from array import array
    import random
    """
    stmt1 = """
    tab_of_chars = array('f', [random.random() for _ in range(1_000_000)])
    """
    stmt2 = """
    tab_of_ints = array('i', [random.randint(1, 100) for _ in range(1_000_000)])
    """
    stmt3 = """
    tab_of_floats = array('f', [random.uniform(0.0, 1.0) for _ in range(1_000_000)])
    """
    stmt4 = """
    list_of_chars = [random.uniform(0.0, 1.0) for _ in range(1_000_000)]
    """
    stmt5 = """
    list_of_ints = [random.randint(1, 100) for _ in range(1_000_000)]
    """
    stmt6 = """
    list_of_floats = [random.uniform(0.0, 1.0) for _ in range(1_000_000)]
    """

    print("Czas inicjowania tablicy znaków: ", timeit(stmt1, setup, number=100))
    print("Czas inicjowania tablicy intów: ", timeit(stmt2, setup, number=100))
    print("Czas inicjowania tablicy floatów: ", timeit(stmt3, setup, number=100))
    print("Czas inicjowania listy znaków: ", timeit(stmt4, setup, number=100))
    print("Czas inicjowania listy intów: ", timeit(stmt5, setup, number=100))
    print("Czas inicjowania listy floatów: ", timeit(stmt6, setup, number=100))


# zadanie1()

# Zadanie 2


# Zadanie 3
def zadanie3():
    setup_deque = """
    from collections import deque
    import random
    d = deque()
    """
    stmt_deque_append = """
    d.append(random.randint(1, 100))
    """
    stmt_deque_appendleft = """
    d.appendleft(random.randint(1, 100))
    """

    print(
        "Czas operacji append na deque: ",
        timeit(stmt_deque_append, setup_deque, number=100000),
    )
    print(
        "Czas operacji appendleft na deque: ",
        timeit(stmt_deque_appendleft, setup_deque, number=100000),
    )

    # list
    setup_list = """
    import random
    l = []
    """
    stmt_list_append = """
    l.append(random.randint(1, 100))
    """
    stmt_list_insert = """
    l.insert(0, random.randint(1, 100))
    """

    print(
        "Czas operacji append na liście: ",
        timeit(stmt_list_append, setup_list, number=100000),
    )
    print(
        "Czas operacji insert(0) na liście: ",
        timeit(stmt_list_insert, setup_list, number=100000),
    )


# zadanie3()

# Zadanie 4

import csv


def zadanie4():
    with open("zamowienia.csv", newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        header = next(reader)
        for row in reader:
            record = {}
            for i, value in enumerate(row):
                record[header[i]] = value
            named_tuple = tuple(record.items())
            print(named_tuple)


# zadanie4()

# Zadanie 5


def top_10_percent(arr):
    num_top_elements = int(len(arr) * 0.1)
    sorted_arr = sorted(arr, reverse=True)
    top_arr = array(arr.typecode, sorted_arr[:num_top_elements])
    return top_arr


# arr = array('i', [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
# top_elements = top_10_percent(arr)
# print(top_elements)
# Zadanie 6


def create_kolo_fortuny(*args):
    counter = Counter(args)
    return deque(counter.elements())


# kolo_fortuny = create_kolo_fortuny(
#     "bankrut", "500", "bankrut", "500", "1000", "500", "1000", "1000"
# )
# print(kolo_fortuny)

# Zadanie 7


def rotate_kolo_fortuny(kolo_fortuny):
    # określenie liczby obrotów kołem fortuny
    n_rotations = random.randint(2, 6)

    # zastosowanie rotacji
    for i in range(n_rotations):
        # pobranie pierwszego elementu koła
        first_element = kolo_fortuny.popleft()

        # dodanie go na koniec koła
        kolo_fortuny.append(first_element)

        # wyświetlenie aktualnych wartości koła
        print(list(kolo_fortuny))

        # opóźnienie dla efektu animacji
        time.sleep(0.5)

    # zwrócenie wylosowanego elementu
    return kolo_fortuny[0]


# rotate_kolo_fortuny(kolo_fortuny)
