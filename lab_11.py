import re
import pickle

# ZADANIE 1

# wszystkie liczby
r1 = r"\d+"
# wszystkie liczby co najmniej 3 cyfrowe
r2 = r"\d{3,}"
# wszystkie adresy IPv4
r3 = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
# wszystkie wyrazy rozpoczynające się od wielkiej litery
r4 = r"\b[A-Z]\w*\b"
# wszystkie linie z pliku, które mają co najmniej 4 wyrazy
r5 = r"^(?=(\b\w+\b\s+){3,})"
# wszystkie adresy url
r6 = r"\bhttps?://\S+\b"

with open("dswp_mg/strings.txt", "r") as plik:
    data = plik.read()
    numbers = re.findall(r1, data)
    numbers3 = re.findall(r2, data)
    ipv4 = re.findall(r3, data)
    capital = re.findall(r4, data)
    four_words = re.findall(r5, data)
    urls = re.findall(r6, data)

print(f"wszystkie liczby: \n {numbers}")
print(f"wszystkie liczby co najmniej 3 cyfrowe: \n {numbers3}")
print(f"wszystkie adresy IPv4: \n {ipv4}")
print(f"wszystkie wyrazy rozpoczynające się od wielkiej litery: \n {capital}")
print(f"wszystkie linie z pliku, które mają co najmniej 4 wyrazy: \n {four_words}")
print(f"wszystkie adresy url: \n {urls}")

# ZADANIE 3


class Osoba:
    def __init__(self, nazwa, wiek):
        self.nazwa = nazwa
        self.wiek = wiek

    def powitanie(self):
        print(f"Cześć, jestem {self.nazwa} i mam {self.wiek} lat.")


person = Osoba("Jan Asiński", 30)
with open("person.pickle", "wb") as file:
    pickle.dump(person, file)

with open("person.pickle", "rb") as file:
    loaded_person = pickle.load(file)

loaded_person.powitanie()

# ZADANIE 4

people = [Osoba("Jan Be", 35), Osoba("Marek Ce", 25), Osoba("Dawid Iksiński", 35)]
with open("people.pickle", "wb") as file:
    pickle.dump(people, file)

with open("people.pickle", "rb") as file:
    loaded_people = pickle.load(file)

for person in loaded_people:
    person.powitanie()
