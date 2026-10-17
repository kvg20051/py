#!/usr/bin/env python

"""Задача 14. Ошибки в логе

python3 d1_14.py < data/test.log
Вывести:
    total: <всего строк>
    INFO: <n>
    WARN: <n>
    ERROR: <n>
    first error: <время>
    last error: <время>
Без словарей — только циклы и split().
"""

import sys

def main():
    for line in sys.stdin:
        parts = line.split()
        print(parts[0], end=" ")


if __name__=="__main__":
    main()

