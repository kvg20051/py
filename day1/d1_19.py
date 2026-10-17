#!/usr/bin/env python3
"""Задача 15. Отчёт по access-логу nginx
    $ python3 d1_15.py < data/nginx.log
Тикет: «вечером 7 октября сайт отдавал ошибки». Пройдите по логу
один раз и выведите сводку:

    total: <всего запросов>
    POST: <запросов методом POST>
    4xx: <ответов с кодом 400–499>
    5xx: <ответов с кодом 500–599>
    traffic: <сумма размеров ответов, байт>
    biggest: <размер> <путь>
    first 5xx: <время>
    last 5xx: <время>

Поля строки после split():
    [0] IP   [3] "[07/Oct/2026:19:01:49"   [5] '"GET'
    [6] путь [8] код ответа                [9] размер, байт

Правила:
  - строки, в которых меньше 10 полей, пропускать;
  - время — только часы:минуты:секунды, например 19:01:49
    (подсказка: в поле [3] это всё после второго двоеточия...
    или проще — последние 8 символов);
  - если 5xx не было, вместо времени вывести "-".

Без списков и словарей: только переменные-счётчики, как в задаче 14.
"""

import sys

def main():
    total = 0
    total_4xx = 0
    total_5xx = 0
    num_of_post = 0
    sum_of_bytes = 0
    biggest = 0
    first_5xx = None
    last_5xx = None

    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 10:
            continue
        value = int(parts[8])
        value2 = int(parts[9])
        sum_of_bytes = sum_of_bytes + value2
        tt = parts[3]

        if parts[5] == "\"POST":
            num_of_post +=1
        if 400 <= value < 500:
            total_4xx +=1

        if 500 <= value < 600:
            total_5xx += 1
            last_5xx = tt[-8:]
            if first_5xx is None:
                first_5xx = tt[-8:]

        if value2 > biggest:
            biggest = value2
            path = parts[6]
        total +=1

    print(f"total: {total}")
    print(f"POST: {num_of_post}")
    print(f"4xx: {total_4xx}")

    if total_5xx == 0:
        print("first 5xx: -")
        print("last 5xx: -")
    else:
        print(f"first 5xx: {first_5xx}")
        print(f"last 5xx: {last_5xx}")

    print(f"traffic: {sum_of_bytes}")
    print(f"biggest: size {biggest}, path {path}")

if __name__ == "__main__":
    main()
