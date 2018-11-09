# task 3
# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

size = int(input('ENTER ARRAY SIZE: '))
arr = [randint(-100, 100) for _ in range(size)]

min_idx = 0
max_idx = size - 1
min_num = arr[0]
max_num = arr[size - 1]
for i in range(size):
    if arr[i] > max_num:
        max_num = arr[i]
        max_idx = i
    if arr[i] < min_num:
        min_num = arr[i]
        min_idx = i

print ('MIN:', min_num, 'IDX:', min_idx)
print ('MAX:', max_num, 'IDX:', max_idx)
print ('INPUT: ', arr)
arr[min_idx] = max_num
arr[max_idx] = min_num
print ('OUTPUT:', arr)
