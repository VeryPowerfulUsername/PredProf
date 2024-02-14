import csv
"""
открываем и читаем csv файл без первой строчки
"""
with open("songs.csv", "r", encoding="utf-8", newline="") as filik:
    datestime = list(csv.reader(filik, delimiter=";"))[1:]
"""
поиск песен по нужной дате
"""

for row in datestime:
        if "01.01.2002" in row[3]:
            print(f"{row[2]} - {row[1]} - {row[0]}")

'''
Исправление недостоющих данных в csv файл
Создание переменных для работы с недостоющими данными
lncount - количество символов в имеени артиста
lscount - количество символов в названии песни
dndata - дата указанная в начале задания
didata - дата выхода песни
'''

lncount =len(row[1])
lscount =len(row[2])
dndata = len("01.01.2002".split("."))
didata = len(row[3])

tnkon = ()
for row in datestime:
    if row[0]  == 0:
        tnkon = abs((dndata - didata) / (lncount + lscount)) * 10000
        print(tnkon)
"""
Перезапишем файл с недостоющими данными в файл songs_new.csv 
"""

with open("songs_new.csv", "w", encoding="utf-8", newline="") as filik_2:
    rewriter = csv.writer(filik_2, delimiter=";")
    rewriter.writerow(["streams", "artist_name", "track_name", "date"])
    rewriter.writerows(datestime)
    
