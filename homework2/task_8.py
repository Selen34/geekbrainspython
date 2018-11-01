# task_8
#  Посчитать, сколько раз встречается определенная цифра
# в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать,
# задаются вводом с клавиатуры.

num = int(input('ENTER NUM OF NUMBERS: '))
digit = int(input('ENTER DIGIT: '))
count = 0
for i in range(num):
    n = int(input('ENTER NUMBER: '))
    if n == digit:
        count += 1
        continue
    else:
        while n != 0:
            if n % 10 == digit:
                count += 1
            n = n // 10
print('COUNT: ', count)