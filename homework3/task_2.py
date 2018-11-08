# task 2
# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6
# (или 0, 3, 4, 5 – если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

from random import randint

size = int(input('ENTER ARRAY SIZE: '))
arr = [randint(0, 1000) for _ in range(size)]
output = []
for i in range(size):
    if arr[i] % 2 == 0:
        output.append(i)
print('ARRAY:  ', arr)
print('INDEXES:', output)
