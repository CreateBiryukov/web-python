# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

f = open('/home/std/python2020/pyneng-examples-exercises/exercises/07_files/ospf.txt', 'r')
l = f.readlines() 
p = 'Prefix                {}\nAD/Metric             {}\nNext-Hop              {}\nLast update           {}\nOutbound Interface    {}\n'
for s in l:
    s = s.split()
    pref = s[1]
    ad = s[2].strip('[]')
    nh = s[4].strip(',')
    lu = s[5].strip(',')
    oi = s[6]
    print (p.format(pref, ad, nh, lu, oi))