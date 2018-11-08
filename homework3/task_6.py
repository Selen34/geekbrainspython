# task 6
# В одномерном массиве найти сумму элементов,
#  находящихся между минимальным и максимальным элементами.
#  Сами минимальный и максимальный элементы в сумму не включать.

from random import randint

size = 10
noise = 20
arr = [randint(0, noise) for _ in range(size)]

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

sum_ = 0
begin_ = min_idx + 1
end_ = max_idx
if max_idx < min_idx:
    begin_ = max_idx + 1
    end_ = min_idx

for i in range(begin_, end_):
    sum_ += arr[i]

print (arr)
print ('MIN:', min_num, 'IDX:', min_idx)
print ('MAX:', max_num, 'IDX:', max_idx)
print ('SUM:', sum_)
