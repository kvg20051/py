"""Задача 6. Надёжный клиент
    $ python3 d4_06.py <URL>
Напишите функцию fetch_json(url), которая возвращает разобранный
JSON или завершает программу с понятной ошибкой. Ответ печатать
через json.dumps(data, ensure_ascii=False, indent=2).

    $ python3 d4_06.py https://jsonplaceholder.typicode.com/users/1
    { ...данные пользователя... }

    $ python3 d4_06.py https://jsonplaceholder.typicode.com/users/9999
    HTTP 404: https://jsonplaceholder.typicode.com/users/9999

    $ python3 d4_06.py https://no-such-host.invalid/
    ошибка сети: ...

    $ python3 d4_06.py http://10.255.255.1/
    таймаут: http://10.255.255.1/

Правила:
  - ошибки — в stderr, код выхода 1;
  - timeout=5;
  - порядок except: сначала Timeout и HTTPError,
    в конце общий RequestException.
"""
