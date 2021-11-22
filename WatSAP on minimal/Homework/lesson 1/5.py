# Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.
import subprocess
import chardet
import os
import time

def thisping(args):
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    print(subproc_ping)
    for line in subproc_ping.stdout:
        print(line.decode('cp866'))


args = ['ping', 'youtube.com']
norma = ['ping', 'yandex.ru']
thisping(args)
time.sleep(3)
thisping(norma)
