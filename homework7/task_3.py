# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найти в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше ее.

from random import randint
m = 5
size = 2 * 5 + 1
array = [randint(0, 100) for _ in range(size)]
print(array)

idx = 0
for i in range(size):
    maxs = 0
    mins = 0
    for j in range(size):
        if array[i] != array[j]:
            if array[j] > array[i]:
                maxs += 1
            else:
                mins += 1
    if (mins == maxs):
        idx = i
        break

print('IDX:', idx, ' MEDIANA: ', array[idx])

# медиану нашли, проверим визуально что это она после сортировки
n = 1
stop = True
while n < len(array):
    for i in range(len(array) - 1):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
            stop = False
    if stop:
        break
    else:
        stop = True
    n += 1

print(array)
