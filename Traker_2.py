import csv
"""
открываем и читаем csv файл без первой строчки
"""
with open("songs.csv", "r", encoding="utf-8", newline="") as filik:
    datestime = list(csv.DictReader(filik, delimiter=";"))

def