"""Задача 5. Экспорт в CSV
    $ python3 d4_05.py users.csv
Сохраните всех пользователей (GET /users) в CSV:

    id,name,email,city,company
    1,Leanne Graham,Sincere@april.biz,Gwenborough,Romaguera-Crona
    ...

Правила:
  - company — это user["company"]["name"];
  - запись через csv.DictWriter, файл открывать с newline="";
  - после записи вывести в stderr: saved 10 rows to users.csv;
  - без аргумента писать CSV в stdout
    (подсказка: DictWriter принимает sys.stdout вместо файла).
"""
