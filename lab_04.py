import string
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
