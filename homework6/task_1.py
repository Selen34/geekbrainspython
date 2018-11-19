# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Для анализа возьмите любые 1-3 ваших программы. Результаты анализа вставьте в виде комментариев к коду.
# P.S. Напишите в комментариях версию Python и разрядность ОС.

from sys import getsizeof
from collections import defaultdict
from random import randint

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
pool = defaultdict(int)
# begin
noise = 10
row_size = 5
column_size = 5
matrix = [0] * row_size
# add to pool
pool[id(noise)] = getsizeof(noise)
pool[id(row_size)] = getsizeof(row_size)
pool[id(column_size)] = getsizeof(column_size)
pool[id(matrix)] = getsizeof(matrix)
# init matrix
for row in range(row_size):
    # add to pool
    pool[id(row)] = getsizeof(row)
    matrix[row] = [0] * column_size
    for column in range(column_size):
        matrix[row][column] = randint(0, noise)
        # add to pool
        pool[id(column)] = getsizeof(column)
        pool[id(matrix[row][column])] = getsizeof(matrix[row][column])
        # print('ID:', id(matrix[row][column]))
for row in range(row_size):
    print(matrix[row])

# compute
output = [0] * column_size
# add to pool
pool[id(output)] = getsizeof(output)
for column in range(column_size):
    row = 0
    output[column] = matrix[row][column]
    # add to pool
    pool[id(row)] = getsizeof(row)
    # add to pool
    pool[id(output[column])] = getsizeof(output[column])
    while row < row_size:
        if matrix[row][column] < output[column]:
            output[column] = matrix[row][column]
        row += 1
print()
print(output)

max_num = output[0]
# add to pool
pool[id(max_num)] = getsizeof(max_num)
for i in range(column_size):
    if output[i] > max_num:
        max_num = output[i]
print('MAX NUM:', max_num)
# end
print('*' * 50)
print('MOST ALLOCATED MEMORY: ', sum(pool.values()))
# Проанализировав ID объектов, которые были выделены в процессе работы программы, а так же содержимое словаря pool
# можно заметить что объем памяти был выделен меньше чем <количество элементов> * <размер матрицы>
# Это благодаря тому, что некоторые элементы ссылались на один и тот же объект
# В данном случе использовались малые числа (до 255), для которых в питоне уже заранее выделены объекты
# Поэтому матрица содержала просто ссылки на них

# Python 3.6.4 :: Anaconda, Inc.
# System Version: macOS 10.14.1 (18B75)
# Kernel Version: Darwin 18.2.0
# RELEASE_X86_64 x86_64
