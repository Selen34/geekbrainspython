# task 1
# 1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Вывести на экран исходный и отсортированный массивы.

from random import randint
size = 20
array = [randint(-100, 100) for _ in range(size)]
print(array)

n = 1
stop = True
while n < len(array):
    for i in range(len(array) - 1):
        if array[i] < array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
            stop = False
    if stop:
        break
    else:
        stop = True
    n += 1
print(array)
