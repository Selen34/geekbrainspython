# task 1
# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны любому из чисел в диапазоне от 2 до 9.

gist = [0] * 10
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            gist[j] += 1

for i in range(2, 10):
    print('NUMBER:', i, ' SUM:', gist[i])
