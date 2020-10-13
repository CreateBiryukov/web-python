# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
#ip = (input('ввесди IP-сети в формате: 10.1.1.0/24 '))
# n = input('Введите IP-сети в формате: 10.1.1.0/24: ')
import sys 
ip = sys.argv[1]
network = ip[:ip.find('/')] 
bin_network = network.split('.')

pr_mask= ip[ip.find('/')::] 
mask = ip[ip.find('/')+1::] 
bin_mask = int(mask)
bin_mask = '1' * bin_mask
bin_mask = "{:<032}".format(bin_mask)

bn1 = int(bin_network[0])
bn2 = int(bin_network[1])
bn3 = int(bin_network[2])
bn4 = int(bin_network[3])

bm1=int(bin_mask[0:8], 2)
bm2=int(bin_mask[8:16], 2)
bm3=int(bin_mask[16:24], 2)
bm4=int(bin_mask[24:32], 2)

bn1 = bn1 & bm1
bn2 = bn2 & bm2
bn3 = bn3 & bm3
bn4 = bn4 & bm4

print_network = '''
 Network:
 {0:<10} {1:<10} {2:<10} {3:<10}
 {0:<010b} {1:<010b} {2:<010b} {3:<010b}
 '''
print_mask = '''
 Mask:
 {4:<}
 {0:<10} {1:<10} {2:<10} {3:<10}
 {0:<10b} {1:<10b} {2:<10b} {3:<10b}
 ''' 
print(bm4)
print(print_network.format(bn1, bn2, bn3, bn4))
print(print_mask.format(bm1, bm2, bm3, bm4, pr_mask))