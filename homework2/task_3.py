# task 3
# Сформировать из введенного числа обратное по порядку входящих в него цифр
# и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.

n = int(input('ENTER NUMBER: '))
while n != 0:
    print (f'{n % 10}', end='')
    n = n // 10
print('')
