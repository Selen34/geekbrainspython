# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.

from collections import deque
from collections import defaultdict

hextoint = defaultdict(int)
hextoint['0'] = 0
hextoint['1'] = 1
hextoint['2'] = 2
hextoint['3'] = 3
hextoint['4'] = 4
hextoint['5'] = 5
hextoint['6'] = 6
hextoint['7'] = 7
hextoint['8'] = 8
hextoint['9'] = 9
hextoint['A'] = 10
hextoint['B'] = 11
hextoint['C'] = 12
hextoint['D'] = 13
hextoint['E'] = 14
hextoint['F'] = 15
inttohex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

def sumhex(num1, num2):
    size = max([len(num1), len(num2)]) * 10
    mem = deque(maxlen=size)
    out = deque(maxlen=size)
    register1 = deque(maxlen=size)
    register2 = deque(maxlen=size)

    #init before sum
    for i in range(size):
        mem.append(0)
        out.append(0)
        register1.append(0)
        register2.append(0)

    for i in num1:
        register1.append(hextoint[i])

    for i in num2:
        register2.append(hextoint[i])

    # sum
    for i in range(size-1, 0, -1):
        tmp = mem[i] + register1[i] + register2[i]
        if tmp > 15:
            mem[i - 1] = 1
            tmp = tmp - 16
        out[i] = tmp

    while len(out) > 0 and out[0] == 0:
        out.popleft()

    # convert
    for i in range(len(out)):
        out[i] = inttohex[out[i]]
    return out

def multihex(num1, num2):
    register = deque()
    for i in num2:
        register.append(hextoint[i])
    count = 0
    st = 0
    for i in range(len(register) - 1, -1, -1):
        count += register[i] * (16 ** st)
        st += 1
    count -= 1
    answer = num1
    for i in range(count):
        answer = sumhex(answer, num1)
    return answer


print('NOTE: INPUT ONLY IN UPPER CASE. LIMIT - FFFFFFFF')
n1 = deque(input('ENTER NUM 1 in HEX: '))
n2 = deque(input('ENTER NUM 2 in HEX: '))

summ = sumhex(n1, n2)
mult = multihex(n1, n2)

print('SUM IS ', summ)
print('MULTI IS', mult)

print('*' * 50)
print('human-readable:')
answer = ''
for i in summ:
    answer += i
print('SUM:', answer)
answer = ''
for i in mult:
    answer += i
print('MULTI:', answer)
