# День 4. Теория: REST API, JSON, requests

Oct 20, 2026 · @Victor

## 1. HTTP-запрос и ответ

Любое обращение к API — это пара «запрос → ответ» по HTTP, тому же протоколу, что у браузера и nginx из дня 1. Запрос говорит, **что** сделать и **с чем**, ответ — **чем всё кончилось** и **данные**.

Из чего состоит запрос:

- **URL** — адрес ресурса: `https://api.github.com/repos/python/cpython`. После `?` идут параметры: `?page=2&per_page=10`.
- **Метод** — действие: `GET`, `POST` и другие (раздел 2).
- **Заголовки** — служебные пары «имя: значение»: `Accept: application/json`, `Authorization: Bearer <токен>`, `User-Agent: ...`.
- **Тело** — данные, которые отправляем (есть у `POST`/`PUT`/`PATCH`, обычно JSON).

Из чего состоит ответ:

- **Код ответа** — число из трёх цифр.
- **Заголовки** — например, `Content-Type: application/json; charset=utf-8`.
- **Тело** — сами данные, в API почти всегда JSON.

Коды ответа делятся по первой цифре — те же группы, что вы считали в задаче 15:

| Группа | Смысл | Частые коды |
| --- | --- | --- |
| 2xx | успех | `200 OK`, `201 Created`, `204 No Content` |
| 3xx | перенаправление | `301`, `302`, `304 Not Modified` |
| 4xx | ошибка клиента — виноват запрос | `400` плохой запрос, `401` не авторизован, `403` нельзя, `404` нет ресурса, `429` слишком часто |
| 5xx | ошибка сервера — виноват сервер | `500`, `502 Bad Gateway`, `503` недоступен, `504` таймаут шлюза |

Практическое правило: на 4xx повторять тот же запрос бессмысленно, надо чинить запрос. На 5xx и `429` можно подождать и повторить.

## 2. REST: ресурсы и методы

REST — договорённость, как устроить API: данные — это **ресурсы** с адресами, а действие задаётся **HTTP-методом**, а не словом в адресе.

```
/users            — коллекция: все пользователи
/users/1          — один пользователь с id 1
/users/1/posts    — вложенная коллекция: посты пользователя 1
```

| Метод | Действие | Пример | Успешный ответ |
| --- | --- | --- | --- |
| `GET` | прочитать | `GET /users/1` | `200` + данные |
| `POST` | создать | `POST /posts` + тело | `201` + созданный объект |
| `PUT` | заменить целиком | `PUT /posts/1` + полное тело | `200` |
| `PATCH` | изменить часть полей | `PATCH /posts/1` + `{"title": "..."}` | `200` |
| `DELETE` | удалить | `DELETE /posts/1` | `200` или `204` |

Правильно `DELETE /posts/1`, а не `GET /deletePost?id=1`. `GET` никогда не должен ничего менять: его можно безопасно повторять, кэшировать и открывать в браузере.

**Параметры запроса** (query string) — фильтры и страницы для `GET`. Они идут после `?` и разделяются `&`:

```
GET /posts?userId=1            — посты пользователя 1
GET /comments?postId=5         — комментарии к посту 5
GET /repos/python/cpython/issues?state=open&per_page=5
```

**Без состояния.** Сервер не помнит прошлых запросов, поэтому всё нужное (токен, номер страницы) передаётся в каждом запросе заново.

Для тренировки весь день используем [JSONPlaceholder](https://jsonplaceholder.typicode.com) — бесплатный учебный API: `/users`, `/posts`, `/comments`, `/todos`. Он принимает `POST`/`PUT`/`DELETE` и отвечает как настоящий, но ничего не сохраняет.

## 3. JSON и модуль json

JSON — текстовый формат данных, который почти один в один ложится на словари и списки из дня 2. Освоили `dict` и `list` — JSON уже знаете.

| JSON | Python |
| --- | --- |
| `{"key": 1}` объект | `dict` |
| `[1, 2, 3]` массив | `list` |
| `"text"` | `str` |
| `42`, `3.14` | `int`, `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

Отличия от Python: ключи только в **двойных** кавычках, нет комментариев и запятой после последнего элемента.

Модуль `json` переводит туда и обратно. Запомнить проще всего по букве `s` — *string*:

```python
import json

text = '{"name": "Leanne", "age": 30, "tags": ["admin", "dev"]}'
data = json.loads(text)          # строка → dict
print(data["tags"][0])           # admin

out = json.dumps(data, ensure_ascii=False, indent=2)   # dict → строка

with open("user.json", encoding="utf-8") as f:
    data = json.load(f)          # файл → dict (без s)
```

`ensure_ascii=False` нужен, чтобы русские буквы писались как есть, а не `\u0412...`. `indent=2` делает вывод читаемым.

**Вложенные структуры.** Ответ API — обычно дерево. Идёте по нему шаг за шагом: `["ключ"]` для словаря, `[номер]` для списка.

```python
user = {
    "id": 1,
    "name": "Leanne Graham",
    "address": {"city": "Gwenborough", "geo": {"lat": "-37.3159"}},
}
print(user["address"]["city"])           # Gwenborough
print(user["address"]["geo"]["lat"])    # -37.3159  (строка, не число!)
```

**Список словарей** — самая частая форма ответа: `GET /users` вернёт список, где каждый элемент — словарь. Обрабатывается обычным `for` и знакомыми приёмами дня 2:

```python
for u in users:
    print(u["id"], u["name"])

cities = set()
for u in users:
    cities.add(u["address"]["city"])
```

Правило проверок прежнее: поля может не быть. Где не уверены, берите `u.get("email", "-")` вместо `u["email"]`.

## 4. Библиотека requests

`requests` — стандартный де-факто способ делать HTTP-запросы из Python. Она не входит в стандартную библиотеку, её ставят отдельно:

```
$ python3 -m pip install requests
# на Ubuntu/Debian с системным Python: sudo apt install python3-requests
# или в виртуальном окружении: python3 -m venv .venv && . .venv/bin/activate
```

**GET-запрос.** Одна строка — и в руках объект ответа `r`:

```python
import requests

r = requests.get("https://jsonplaceholder.typicode.com/users/1", timeout=10)
print(r.status_code)              # 200
print(r.headers["Content-Type"])  # application/json; charset=utf-8
user = r.json()                   # тело → dict (внутри это json.loads)
print(user["email"])
```

Что есть у ответа: `r.status_code` — код, `r.ok` — `True` для кодов меньше 400, `r.json()` — тело как Python-данные, `r.text` — тело строкой, `r.headers` — заголовки, `r.url` — итоговый адрес.

**Параметры — словарём `params`**, а не склейкой строк. `requests` сам соберёт `?userId=1&_limit=5` и правильно экранирует пробелы и русские буквы:

```python
r = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1, "_limit": 5},
    timeout=10,
)
print(r.url)   # .../posts?userId=1&_limit=5
posts = r.json()
```

**Заголовки — словарём `headers`.** Многие API (GitHub в их числе) хотят осмысленный `User-Agent`, а для закрытых данных — токен:

```python
headers = {"User-Agent": "py-week-course", "Accept": "application/json"}
r = requests.get("https://api.github.com/repos/python/cpython", headers=headers, timeout=10)
repo = r.json()
print(repo["stargazers_count"], repo["open_issues_count"])
```

Токены не пишут в код. Их берут из переменной окружения: `os.environ.get("GITHUB_TOKEN")`.

**`timeout` — всегда.** Без него `requests` может ждать ответа вечно, и скрипт молча зависнет. 5–10 секунд — разумно.

**POST — создать.** Данные передают через `json=`: библиотека сама превратит словарь в JSON и поставит нужный заголовок:

```python
new = {"title": "Отчёт по логам", "body": "total: 1234", "userId": 1}
r = requests.post("https://jsonplaceholder.typicode.com/posts", json=new, timeout=10)
print(r.status_code)   # 201
print(r.json())        # тот же объект + выданный сервером "id": 101
```

Аналогично `requests.put(...)`, `requests.patch(...)`, `requests.delete(...)`.

## 5. Ошибки

У сетевого запроса две разные беды, и ловят их по-разному: **сервер ответил, но с ошибкой** (код 4xx/5xx) и **ответа нет вообще** (нет сети, DNS, таймаут).

**Сервер ответил с ошибкой.** `requests` в этом случае **не бросает исключение**: `r.status_code == 404` — это обычный ответ. Если сразу звать `r.json()`, получите странные данные или ошибку разбора. Поэтому код проверяют до разбора тела:

```python
r = requests.get(url, timeout=10)
if r.status_code == 404:
    print("не найдено", file=sys.stderr)
    sys.exit(1)
r.raise_for_status()   # для любых других 4xx/5xx бросит HTTPError
data = r.json()
```

**Ответа нет.** Тогда исключение бросает уже сам `requests.get`:

| Исключение | Когда |
| --- | --- |
| `requests.exceptions.ConnectionError` | нет сети, неверный адрес, сервер не принимает соединение |
| `requests.exceptions.Timeout` | не уложились в `timeout` |
| `requests.exceptions.HTTPError` | бросил `raise_for_status()` на 4xx/5xx |
| `requests.exceptions.JSONDecodeError` | тело — не JSON (например, HTML-страница ошибки) |
| `requests.exceptions.RequestException` | родитель всех перечисленных — ловит всё сразу |

Типичная обёртка — функция, которая либо возвращает данные, либо аккуратно завершает программу, как в задаче 13 и в `d2_06`:

```python
import sys
import requests

def fetch_json(url, params=None):
    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.Timeout:
        print(f"таймаут: {url}", file=sys.stderr)
    except requests.exceptions.HTTPError:
        print(f"HTTP {r.status_code}: {url}", file=sys.stderr)
    except requests.exceptions.RequestException as e:
        print(f"ошибка сети: {e}", file=sys.stderr)
    sys.exit(1)
```

Порядок `except` важен: сначала частные исключения, в конце общий `RequestException`. Python берёт первый подходящий блок, и общий, поставленный первым, перехватит всё.

**Повтор при временных сбоях.** На `429`, `502`, `503`, `504` и таймаут разумно подождать и попробовать ещё раз-два. Простой вариант — цикл с `time.sleep`:

```python
import time

for attempt in range(3):
    try:
        r = requests.get(url, timeout=10)
        if r.status_code not in (429, 502, 503, 504):
            break
    except requests.exceptions.Timeout:
        pass
    time.sleep(2 ** attempt)   # 1, 2, 4 секунды
```

## 6. Сохранение результата: JSON и CSV

Записывают так же через `with open`, только с режимом `"w"` — файл создастся или перезапишется. JSON подходит, чтобы сохранить данные как есть, CSV — чтобы открыть таблицу в Excel или LibreOffice.

**JSON** — одной строкой через `json.dump` (без `s`, раз пишем в файл):

```python
import json

with open("users.json", "w", encoding="utf-8") as f:
    json.dump(users, f, ensure_ascii=False, indent=2)
```

**CSV** — модуль `csv` из стандартной библиотеки. Для списка словарей удобнее всего `DictWriter`: задаёте столбцы, и он пишет каждую строку из словаря.

```python
import csv

rows = []
for u in users:
    rows.append({
        "id": u["id"],
        "name": u["name"],
        "email": u["email"],
        "city": u["address"]["city"],   # вложенное поле — в плоский столбец
    })

with open("users.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "name", "email", "city"])
    writer.writeheader()
    writer.writerows(rows)
```

Две детали. `newline=""` обязателен для `csv`, иначе на Windows появятся пустые строки между записями. Запятые и кавычки внутри значений `csv` экранирует сам — не собирайте CSV через `",".join(...)`.

Результат выглядит так:

```csv
id,name,email,city
1,Leanne Graham,Sincere@april.biz,Gwenborough
2,Ervin Howell,Shanna@melissa.tv,Wisokyburgh
```

Куда выводить, решает пользователь, как в `d2_06`: имя файла приходит из `sys.argv`, а без аргумента результат печатается в `stdout`, откуда его можно перенаправить: `python3 d4_05.py > users.csv`.

## 7. Шпаргалка по задачам дня 4

Все задачи работают с JSONPlaceholder (`https://jsonplaceholder.typicode.com`), так что ключи и токены не нужны.

| Задача | Что сделать | Что нужно | Разделы |
| --- | --- | --- | --- |
| d4\_01 Первый запрос | `GET /users/1`, вывести код ответа, имя, email и город | `requests.get`, `timeout`, `r.json()`, вложенный ключ | 1, 3, 4 |
| d4\_02 Список пользователей | `GET /users`, вывести `id name city` по строке на каждого | список словарей, `for` | 3, 4 |
| d4\_03 Задачи пользователя | `python3 d4_03.py 5` — сколько у пользователя 5 задач в `/todos` выполнено и сколько нет | `sys.argv`, `params={"userId": ...}`, счётчики | 2, 4 |
| d4\_04 Топ комментаторов | по `/comments` найти 5 email с наибольшим числом комментариев | `counts.get(k, 0) + 1`, `sorted` + `[:5]` из дня 2 | 3, 4 |
| d4\_05 Экспорт в CSV | сохранить пользователей в `users.csv` (`id,name,email,city`), имя файла — из аргумента | `csv.DictWriter`, `newline=""` | 6 |
| d4\_06 Надёжный клиент | `fetch_json(url)` с обработкой `404`, таймаута и ошибки сети; проверить на `/users/9999` и на несуществующем домене | `raise_for_status`, `except`, `stderr`, `sys.exit(1)` | 5 |
| d4\_07 Создать пост | `POST /posts` с заголовком из аргумента, вывести код (`201`) и выданный `id` | `requests.post(..., json=...)` | 2, 4 |

Правило дня 1 остаётся главным и тут: **сначала проверить, что ответ пришёл и код хороший, потом разбирать JSON, потом использовать поля**.
