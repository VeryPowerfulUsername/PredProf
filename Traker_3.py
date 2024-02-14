import csv
"""
открываем и читаем csv файл без первой строчки
"""
with open("songs.csv", "r", encoding="utf-8", newline="") as filik:
    datestime = list(csv.DictReader(filik, delimiter=";"))

nameartist = input("Введите имя артиста: ")
while nameartist != "0":
    for artist in datestime:
        if artist[" "] == nameartist:
