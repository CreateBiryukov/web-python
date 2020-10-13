# -*- coding: utf-8 -*-
"""
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ignore = ["duplex", "alias", "Current configuration"]
t = open('config_sw1_cleared.txt', 'w')
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
            t.write(m)     
