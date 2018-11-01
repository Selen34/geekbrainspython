# task_6
# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться,
# больше или меньше загаданного введенное пользователем число.
# Если за 10 попыток число не отгадано, то вывести его.

import random

rnd = random.randint(0, 100)
i = 10
is_answer = False
while i > 0:
    n = int(input('ENTER NUM: '))
    if n == rnd:
        print('YES')
        is_answer = True
        break
    elif n > rnd:
        print ('greater')
    else:
        print ('less')
    i -= 1
if not is_answer:
    print ('ANSWER IS: ', rnd)
