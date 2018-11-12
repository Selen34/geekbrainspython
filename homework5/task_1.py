# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартала для каждого предприятия.
#  Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего
# и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
from collections import defaultdict
from collections import Counter

num = int(input('NUMBER OF FACTORIES: '))

factories = defaultdict(Counter)
average = 0
for i in range(num):
    name = input(f'{i}. NAME: ')
    quarter1 = int(input(f'{i}. quarter 1: '))
    quarter2 = int(input(f'{i}. quarter 2: '))
    quarter3 = int(input(f'{i}. quarter 3: '))
    quarter4 = int(input(f'{i}. quarter 4: '))
    factories[name] = Counter({
        'quarter1': quarter1,
        'quarter2': quarter2,
        'quarter3': quarter3,
        'quarter4': quarter4
    })
    average += sum(factories[name].values())

average = average/num
print('AVERAGE:', average)

print('MORE AVERAGE:')
for key in factories:
    if sum(factories[key].values()) > average:
        print(key)

print('LESS AVERAGE:')
for key in factories:
    if sum(factories[key].values()) < average:
        print(key)
