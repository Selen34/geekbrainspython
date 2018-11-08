# task 8
# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки
# и записывать ее в ее последнюю ячейку. В конце следует вывести полученную матрицу.

x = 5
y = 4
matrix = [0] * y
for row in range(y):
    matrix[row] = [0] * x
    tmp = 0
    for column in range(x - 1):
        matrix[row][column] = int(input(f'ENTER ITEM {column}:{row} '))
        tmp += matrix[row][column]
    matrix[row][x - 1] = tmp
for row in range(y):
    print(matrix[row])
