# This is a 4th task
# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ. Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

from random import random
import math
n_a = int(input('INT NUMBER FROM: '))
n_b = int(input('INT NUMBER TO: '))
f_a = float(input('FLOAT NUMBER FROM: '))
f_b = float(input('FLOAT NUMBER TO: '))
c_a = input('CHAR FROM: ')
c_b = input('CHAR TO: ')
n_r = math.floor(n_a + random()*(n_b - n_a))
f_r = f_a + random()*(f_b - f_a)
c_r = chr(math.floor(ord(c_a) + random()*(ord(c_b) - ord(c_a))))
print('int random: ', n_r)
print('float random: ', f_r)
print('char random: ', c_r)
