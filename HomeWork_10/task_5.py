"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess

for sites in ['yandex.ru', 'youtube.com']:
    args = ['ping', sites]
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        #    print(line)
        print(line.decode('cp866').encode('utf-8').decode('utf-8'))
