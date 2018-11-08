# task 7
# 7. В одномерном массиве целых чисел определить два наименьших элемента.
#  Они могут быть как равны между собой (оба являться минимальными), так и различаться.

from random import randint
size = 10
noise = 20
arr = [randint(0, noise) for _ in range(size)]
min1 = noise * 2
idx1 = 0
min2 = noise * 2
for i in range(size):
    if arr[i] < min1:
        min1 = arr[i]
        idx1 = i
for i in range(size):
    if arr[i] < min2 and i != idx1:
        min2 = arr[i]
print (arr)
print ('NUMBERS ARE: ', min1, min2)
