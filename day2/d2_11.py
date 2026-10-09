"""Задача 11. Подозрительные запросы

    $ python3 d2_11.py < data/nginx.log

Сканеры ищут типовые уязвимые пути. Список признаков задать
в коде:
    SUSPICIOUS = [".env", "wp-login", "phpmyadmin", "server-status"]

Вывести «IP путь» для запросов, путь которых содержит любой
из признаков (any() + генератор):
    203.0.113.10 /wp-login.php
    203.0.113.11 /.env
    203.0.113.12 /phpmyadmin
    192.168.1.157 /server-status
"""

import sys


def main():
    pass  # ваш код


if __name__ == "__main__":
    main()
