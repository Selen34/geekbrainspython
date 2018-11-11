# task 1
# 1. Проанализировать скорость и сложность одного - трёх любых алгоритмов,
# разработанных в рамках домашнего задания первых трех уроков.

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
# NOTE: для упрощения тестирования считаем матрицу квадратной

#  python -m timeit -s "import task_1" "task_1.maxmin(10)"
# 1000 loops, best of 3: 304 usec per loop
#  python -m timeit -s "import task_1" "task_1.maxmin(20)"
# 1000 loops, best of 3: 1.17 msec per loop
#  python -m timeit -s "import task_1" "task_1.maxmin(30)"
# 100 loops, best of 3: 2.73 msec per loop
#  python -m timeit -s "import task_1" "task_1.maxmin(40)"
# 100 loops, best of 3: 4.68 msec per loop
#  python -m timeit -s "import task_1" "task_1.maxmin(50)"
# 100 loops, best of 3: 7.03 msec per loop
#  python -m timeit -n 100 -s "import task_1" "task_1.maxmin(100)"
# 100 loops, best of 3: 28.6 msec per loop
#  python -m timeit -s "import task_1" "task_1.maxmin(150)"
# 100 loops, best of 3: 65.5 msec per loop
#  python -m timeit -s "import task_1" "task_1.maxmin(200)"
# 100 loops, best of 3: 119 msec per loop

# cProfile.run('maxmin(100)')
# 10000    0.007    0.000    0.038    0.000 random.py:216(randint)
#     1    0.009    0.009    0.047    0.047 task_1.py:28(maxmin)

# cProfile.run('maxmin(200)')
# 40000    0.028    0.000    0.155    0.000 random.py:216(randint)
#     1    0.034    0.034    0.189    0.189 task_1.py:28(maxmin)

# алгоритм имеет ярко выраженную квадратичную сложность
# (можно наблюдать на графике)

import cProfile
from random import randint


def maxmin(n):
    noise = 1000
    row_size = n
    column_size = n
    matrix = [0] * row_size
    for row in range(row_size):
        matrix[row] = [0] * column_size
        for column in range(column_size):
            matrix[row][column] = randint(0, noise)
    output = [0] * column_size
    for column in range(column_size):
        row = 0
        output[column] = matrix[row][column]
        while row < row_size:
            if matrix[row][column] < output[column]:
                output[column] = matrix[row][column]
            row += 1
    max_num = output[0]
    for i in range(column_size):
        if output[i] > max_num:
            max_num = output[i]
    return max_num
