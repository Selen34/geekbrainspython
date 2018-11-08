# task 9
# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import randint
noise = 10
row_size = 5
column_size = 5
matrix = [0] * row_size
# init matrix
for row in range(row_size):
    matrix[row] = [0] * column_size
    for column in range(column_size):
        matrix[row][column] = randint(0, noise)
for row in range(row_size):
    print(matrix[row])

# compute
output = [0] * column_size
for column in range(column_size):
    row = 0
    output[column] = matrix[row][column]
    while row < row_size:
        if matrix[row][column] < output[column]:
            output[column] = matrix[row][column]
        row += 1
print()
print(output)

max_num = output[0]
for i in range(column_size):
    if output[i] > max_num:
        max_num = output[i]

print('MAX NUM:', max_num)
