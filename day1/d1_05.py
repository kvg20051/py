#!/usr/bin/env python3
"""Задача 05. Таблица умножения
Прочитать n, вывести таблицу n×n, выровненную по столбцам
(f-строки с шириной, например f"{x:4d}").
"""

def main():
    n = int(input())
    for j in range (1,n+1):
       for i in range (1,n+1):
           print(f"{i*j:4d}", end="")
       print()

if __name__ == "__main__":
    main()
