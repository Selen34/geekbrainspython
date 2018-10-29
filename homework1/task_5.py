# this is a 5th task
# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
a = input('ENTER A: ')
b = input('ENTER B: ')
na = ord(a) - ord('a') + 1
nb = ord(b) - ord('a') + 1
d = nb - na
print('POS A ', na)
print('POS B ', nb)
print('DIV ', d)
