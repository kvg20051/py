#!/usr/bin/env python3
'''
16. Чтение и запись файла
Прочитать CSV-файл data/employees.csv со столбцами имя, отдел, зарплата и посчитать среднюю зарплату по отделам. Результат записать в новый файл.
Тренирует: open(), with, модуль csv, группировку данных.
'''

import sys
import csv

def main():
    with open('day1/data/employees.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
#            print(row['имя'], row['отдел'], row['зарплата'])
            parts = row.split() 
            print(part[0])

    with open('day1/data/result.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['отдел', 'средняя зарплата'])   # заголовок
        writer.writerow(['Разработка', 777000])          # пример строки

if __name__ == "__main__":
    main()
