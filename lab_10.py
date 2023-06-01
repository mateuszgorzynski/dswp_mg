import os
import csv
import pprint
from datetime import datetime, timedelta


# Zadanie 1
def create_folders(paths):
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Utworzono folder: {path}")
        else:
            print(f"Folder już istnieje: {path}")


folder_paths = ["folder1", "folder2/subfolder", "folder3/subfolder1/subfolder2"]
# create_folders(folder_paths)

# Zadanie 2


def merge_txt_files_to_csv(folder_path, output_csv_path):
    with open(output_csv_path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)

        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".txt"):
                    file_path = os.path.join(root, file)

                    with open(file_path, "r") as txt_file:
                        content = txt_file.read().strip()

                        if content:  # Pomijaj puste pliki
                            writer.writerow([content])

    print(f"Scalono pliki .txt do pliku CSV: {output_csv_path}")


folder_path = "data"
output_csv_path = "lab10zad2file.csv"
# merge_txt_files_to_csv(folder_path, output_csv_path)

# Zadanie 3

user_time_str = input("Podaj czas w formacie HH:MM:SS: ")

user_time_dt = datetime.strptime(user_time_str, "%H:%M:%S").time()

time_zones = {"Tokio": 7, "Waszyngton": -6, "Sydney": 8, "Londyn": -1}

for city, hours in time_zones.items():
    new_time = datetime.combine(datetime.today(), user_time_dt) + timedelta(hours=hours)
    print(f"{city}: {new_time.time()}")

# Zadanie 4


def calculate_age():
    birth_date = input("Podaj swoją datę urodzenia w formacie YYYY/MM/DD \n")
    today = datetime.now()
    birth_year, birth_month, birth_day = map(int, birth_date.split("/"))
    print(f"Dzisiaj jest: {today}")

    years = today.year - birth_year  # 23
    months = today.month - birth_month  # -5
    days = today.day - birth_day  # 19

    if months < 0:
        years -= 1
        months += 12

    if days < 0:
        months -= 1
        days += 30

    print(f"Dzisiaj jest: {today}")
    print(f"Dzisiaj masz {years} lat, {months} miesięcy i {days} dni.")


calculate_age()
# Zadanie 5


def convert_date_format(file_name, date_column_index, source_format, target_format):
    input_file = "lab10zad2file.csv"
    output_file = file_name

    with open(input_file, "r") as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)

        for row in rows:
            if len(row) > date_column_index:
                date_str = row[date_column_index]
                try:
                    date_obj = datetime.strptime(date_str, source_format)
                    formatted_date = date_obj.strftime(target_format)
                    row[date_column_index] = formatted_date
                except ValueError:
                    print(f"Nieprawidłowy format daty: {date_str}")

    with open(output_file, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(rows)

    print(f"Przekonwertowano daty w pliku {input_file} i zapisano jako {output_file}")


file_name = "converted_lab10zad2file.csv"
date_column_index = 0  # Indeks kolumny z datą (liczone od zera)
source_format = "%d-%m-%Y"  # Format źródłowy
target_format = "%Y-%m-%d"  # Format docelowy

# convert_date_format(file_name, date_column_index, source_format, target_format)
