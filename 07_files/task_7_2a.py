# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "Current configuration"]
f = open(sys.argv[1], 'r')
l = f.readlines() 
for m in l:
    if not (m.startswith('!') or m.strip(' ') == ''):
        do_ignore = False
        for i in ignore:
            if m.find(i) >= 0:
                do_ignore = True
                break
        if not do_ignore:        
            print (m, end='')
