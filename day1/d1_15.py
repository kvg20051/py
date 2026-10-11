#!/usr/bin/env python3

'''
9. Разбор лога
Дан список строк вида "2026-10-11 09:42:01 ERROR Disk full". Посчитать количество строк каждого уровня (INFO, WARNING, ERROR) и вывести все сообщения ERROR.
Тренирует: разбор строк, словари, фильтрацию.
'''

import sys

def main():
    for line in sys.stdin:
       parts = line.split()
#       print(parts[0], end=" ")
       print(parts[0])


if __name__=="__main__":
    main()
