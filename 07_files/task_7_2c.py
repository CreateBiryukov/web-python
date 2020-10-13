# -*- coding: utf-8 -*-
"""
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ignore = ["duplex", "alias", "Current configuration"]
import sys
f = open(sys.argv[1], 'r')
t = open(sys.argv[2], 'w')
l = f.readlines()
for m in l:
    if True:
        do_ignore = False
        for i in ignore:
            if n.find(i) >= 0:
                do_ignore = True
                break
        if not do_ignore:   
        t.write(m)