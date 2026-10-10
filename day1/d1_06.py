#!/usr/bin/env python3
"""Задача 06. FizzBuzz

Числа 1..100: делится на 3 — Fizz, на 5 — Buzz, на оба — FizzBuzz,
иначе само число. Каждое значение в своей строке.
"""

def main():
    for n in range(1,101):
        if n%3==0 and n%5==0:
            print("FizzBuzz")
        elif n%3 == 0:
            print("Fizz")
        elif n%5 == 0:
            print("Buzz")
        else:
            print(n)

if __name__ == "__main__":
    main()
