"""Задача 13. Сумма столбца

Ввод: строки вида «имя число».
Вывод (каждое в своей строке):
    sum: <сумма>
    avg: <среднее с 2 знаками>
    max: <максимум> (<имя>)

    $ python3 d1_13.py < data/scores.txt
"""
#!/usr/bin/env python3

import sys

def main():
    total=0
    maximum=0
    count=0
    Name = None

    for line in sys.stdin:
        parts=line.split()
        if len(parts) < 2:
            continue
        count +=1
        value = int(parts[1])
        if value < 0:
            print("некорректные данные", file=sys.stderr)
            sys.exit(1)
        total = total + value
        if value > maximum:
            maximum = value
            Name = parts[0]

    if count == 0:
        print("нет данных", file=sys.stderr)
        sys.exit(1)

    print(f"sum: {total}")
    print(f"maximum: {maximum}", Name)
    print(f"avg: {total/count}")

if __name__ == "__main__":
    main()

