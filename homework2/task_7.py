# task_7
# Написать программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n – любое натуральное число.

n = int(input('ENTER N: '))
sum_num = 0
i = 1
while i <= n:
    sum_num += i
    i += 1
if sum_num == n * (n + 1) / 2:
    print('YES')
else:
    print('NO')
