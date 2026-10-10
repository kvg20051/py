#!/usr/bin/env python3
"""Задача 07. Сумма цифр
Прочитать число (может быть очень длинным), вывести сумму цифр.
Решите двумя способами: через % 10 и через перебор строки.
Выведите результат один раз.
"""

def main():
    m = input()
    k = 0
    for ch in m:
        k = k + int(ch)

    n = int(m)
    t = 0
    while True:
        if n == 0:
            break
        t = t + n%10
        n = n//10
    print(t)

if __name__=="__main__":
    main()
