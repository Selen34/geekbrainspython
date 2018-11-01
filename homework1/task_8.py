# this is a 8th task
# Определить, является ли год, который ввел пользователем, високосным или невисокосным.
year = int(input('ENTER YEAR: '))
if year % 400 == 0:
    print ('Leap year')
else:
    if year % 100 == 0:
        print ('Not leap year')
    elif year % 4 == 0:
        print ('Leap year')
    else:
        print ('Not leap year')
