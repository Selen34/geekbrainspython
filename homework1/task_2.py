# This is a 2nd task
# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.
a = 5
b = 6
print('AND', a & b)
print('OR', a | b)
print('XOR', a ^ b)
print('NOT A', ~a)
print('NOT B', ~b)
print('RIGHT BIT-SHIFT', b >> 2)
print('LEFT BIT-SHIFT', b << 2)