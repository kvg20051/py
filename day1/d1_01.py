#!/usr/bin/env python3
"""Задача 01. Привет
Прочитать имя и вывести: Привет, <имя>!
    $ echo Виктор | python3 d1_01.py
    Привет, Виктор!
"""

def main():
    s=input()
    print(f"Привет, {s}!")

if __name__ == "__main__":
    main()
