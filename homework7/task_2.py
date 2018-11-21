# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

from random import randint
size = 15
array = [randint(0, 50) for _ in range(15)]
print(array)


def merge(arr, left, middle, right):
    part1 = 0
    part2 = 0
    output = [0] * (right - left)

    while left + part1 < middle and middle + part2 < right:
        if arr[left + part1] < arr[middle + part2]:
            output[part1 + part2] = arr[left + part1]
            part1 += 1
        else:
            output[part1 + part2] = arr[middle + part2]
            part2 += 1
    while left + part1 < middle:
        output[part1 + part2] = arr[left + part1]
        part1 += 1
    while middle + part2 < right:
        output[part1 + part2] = arr[middle + part2]
        part2 += 1
    for k in range(part1 + part2):
        arr[left + k] = output[k]


i = 1
while i < size:
    j = 0
    while j < size - i:
        merge(array, j, j + i, min(j + 2 * i, size))
        j += 2 * i
    i *= 2

print(array)
