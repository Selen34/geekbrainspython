# task 5
# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
from random import randint

#size = int(input('ENTER ARRAY SIZE: '))
size = 10
noise = 10
arr = [randint(-noise, noise) for _ in range(size)]
print (arr)
target = -(noise * 2)
idx = -1
for i in range(size):
    if arr[i] < 0 and arr[i] > target:
        target = arr[i]
        idx = i
if idx == -1:
    print ('There is no answer')
else:
    print ('Answer is: ', target, 'index:', idx)
