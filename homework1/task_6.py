# This is a 6th task
# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
num = int(input('ENTER POS: '))
a = chr(ord('a') + num - 1)
print('CHAR: ', a)