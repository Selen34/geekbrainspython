# This is a 1st task
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
num = int(input('Enter num:'))
d1 = num//100
td2 = (num - d1*100)
d2 = td2//10
d3 = td2 - d2*10
print ('sum', d1 + d2 + d3)
print ('mult', d1 * d2 * d3)