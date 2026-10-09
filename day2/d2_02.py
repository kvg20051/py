"""Задача 02. Топ процессов

python3 d2_02.py < data/syslog.txt
Для syslog-формата (дата, хост, процесс[pid]: сообщение)
посчитать, сколько строк от каждого процесса. PID отбросить:
"postfix/smtpd[94240]:" → "postfix/smtpd".
Вывести 5 самых частых:
    systemd: 21
    postfix/anvil: 9
"""
