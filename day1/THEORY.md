# День 1. Базовый синтаксис (для тех, кто знает Си)

Пробуйте каждый пример в интерактивном `python3`.

## 1. Переменные и типы

```python
n = 10          # int — без переполнения, хоть 2**1000
x = 3.14        # float (аналог double)
s = "привет"    # str — неизменяемая строка
ok = True       # bool: True / False — с большой буквы
nothing = None  # аналог NULL
type(n)         # <class 'int'>

int("42"), float("2.5"), str(42), int(3.9)   # 42 2.5 '42' 3
```

## 2. Арифметика — отличия от Си

```python
7 / 2     # 3.5  — деление ВСЕГДА даёт float
7 // 2    # 3    — целочисленное
-7 // 2   # -4   — округляет вниз, а не к нулю!
7 % 3     # 1
2 ** 10   # 1024
abs(-5), max(3, 8, 1), min(3, 8, 1), round(2.567, 2)
n += 1    # ++ и -- нет
```

## 3. Вывод и ввод

```python
print("a", "b", 3)            # a b 3
print("a", "b", sep=",")      # a,b
print("без перевода", end="")

name, age = "Виктор", 40
print(f"{name}, вам {age} лет")
print(f"{3.14159:.2f}")              # 3.14
print(f"{age:5d}|{name:>10}|")       # ширина / выравнивание

s = input()                          # строка без \n, всегда str
n = int(input())
a, b = map(int, input().split())     # "5 7" → 5, 7

import sys
for line in sys.stdin:               # как while read line в bash
    line = line.rstrip("\n")
```

## 4. Условия

```python
if x > 0:
    print("плюс")
elif x == 0:
    print("ноль")
else:
    print("минус")

if x > 0 and x < 10: ...
if not ok or n == 5: ...
if 0 < x < 10: ...                   # цепочка сравнений

# Ложь: 0, 0.0, "", [], {}, None
if not s:
    print("пусто")

res = "чётное" if n % 2 == 0 else "нечётное"   # тернарный оператор
```

## 5. Циклы

```python
for i in range(5): ...          # 0..4
for i in range(2, 10): ...      # 2..9
for i in range(10, 0, -2): ...  # 10 8 6 4 2

for ch in "abc": ...            # перебор элементов, не индексов
for i, ch in enumerate("abc"): ...

while i < 5:
    i += 1
    if i == 2:
        continue
    if i == 4:
        break
```

## 6. Функции

```python
def add(a, b):
    return a + b

def greet(name, greeting="Привет"):
    return f"{greeting}, {name}!"

greet("Виктор", greeting="Здравствуйте")

def min_max(a, b):
    return min(a, b), max(a, b)       # несколько значений (кортеж)

lo, hi = min_max(8, 3)
a, b = b, a                           # обмен без временной переменной

def main():
    ...

if __name__ == "__main__":
    main()
```

## Задачи

Условия — в начале каждого файла `d1_XX.py`.

- **A. Разминка (~1 ч):** 01–04
- **B. Циклы (~1,5 ч):** 05–08
- **C. Функции (~1,5 ч):** 09–11
- **D. stdin (~2 ч, главное для собеседования):** 12–14
- **Вечер (~1 ч):** перепишите 13 и 14 начисто за 20 минут каждую.
