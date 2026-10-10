#!/usr/bin/env python3
"""Задача 03. Чётность

Прочитать целое число, вывести «чётное» или «нечётное».
"""

def main():
    n=int(input())
    if n%2 == 0:
        print("чётное")
    else:
        print("нечётное")

if __name__ == "__main__":
    main()
