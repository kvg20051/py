"""Задача 04. Нормализация пути

    $ python3 d2_04.py < data/nginx.log

Чтобы группировать запросы, путь приводят к шаблону:
  - query string отбрасывается: /search?q=nginx -> /search
  - числовые сегменты заменяются на {id}: /api/users/42 -> /api/users/{id}

Вывести только пути, которые изменились, в порядке появления:
    /products/123 -> /products/{id}
    /api/products/123 -> /api/products/{id}
    ...
    /search?q=nginx -> /search

Подсказка: partition("?"), split("/"), isdigit(), "/".join(...).
"""

import sys


def main():
    pass  # ваш код


if __name__ == "__main__":
    main()
