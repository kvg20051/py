#!/usr/bin/env python3
"""Задача 04. Високосный год
Год високосный, если делится на 4, но не на 100, либо делится на 400.
Вывести YES или NO.
"""

def main():
    y = int(input())
    if y%4 == 0 and y%100!=0:
        print("YES")
    elif y%400 == 0:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
