# Task_9
#Среди натуральных чисел, которые были введены,
# найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

max_num = 0
sum_num = 0
while True:
    n = int(input('ENTER NUM: '))
    if n == 0:
        break
    tmp = 0
    tn = n
    while tn % 10 != 0:
        tmp += tn % 10
        tn = tn // 10
    if tmp > sum_num:
        max_num = n
        sum_num = tmp
print ('MAX: ', max_num, ' SUM: ', sum_num)
