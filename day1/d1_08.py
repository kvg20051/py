"""Задача 08. Простые числа

Функция is_prime(n) -> bool.
Вывести все простые числа до 100 в одну строку через пробел.
"""

def is_prime(n):
    if n < 2:
        return False          # 0 и 1 не простые
    for d in range(2, n):
        if n%d==0:             # d делит n нацело
            return False      # нашли делитель — ответ уже известен
    return True              # цикл закончился, делителей не нашли


def main():
    for n in range(1, 101):
        if is_prime(n):
            print(n, end=" ")
    print()

if __name__=="__main__":
    main()
