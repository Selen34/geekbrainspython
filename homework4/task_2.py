# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Первый - использовать алгоритм решето Эратосфена.
# Второй - без использования "решета".
# Проанализировать скорость и сложность алгоритмов.
import cProfile
def eratosfen(n):
    # 1229
    limit = 10000
    arr = [i for i in range(limit)]
    arr[1] = 0
    for i in range(2, limit):
        if arr[i] != 0:
            j = i + i
            while j < limit:
                arr[j] = 0
                j += i
    res = [i for i in arr if i != 0]
    return res[n - 1]

def is_simple(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def simple(n):
    if n < 3:
        return n + 1
    i = 2
    j = 3
    while i < n:
        j += 1
        if is_simple(j):
            i += 1
    return j

#  python -m timeit -n 100 -s "import task_2" "task_2.eratosfen(10)"
# 100 loops, best of 3: 5.46 msec per loop
#  python -m timeit -n 100 -s "import task_2" "task_2.eratosfen(20)"
# 100 loops, best of 3: 5.45 msec per loop
#  python -m timeit -n 100 -s "import task_2" "task_2.eratosfen(30)"
# 100 loops, best of 3: 5.46 msec per loop
#  python -m timeit -n 100 -s "import task_2" "task_2.eratosfen(40)"
# 100 loops, best of 3: 5.45 msec per loop
#  python -m timeit -n 100 -s "import task_2" "task_2.eratosfen(50)"
# 100 loops, best of 3: 5.5 msec per loop
#  python -m timeit -n 100 -s "import task_2" "task_2.eratosfen(100)"
# 100 loops, best of 3: 5.49 msec per loop
#  python -m timeit -n 100 -s "import task_2" "task_2.eratosfen(150)"
# 100 loops, best of 3: 5.45 msec per loop
#  python -m timeit -n 100 -s "import task_2" "task_2.eratosfen(200)"
# 100 loops, best of 3: 5.49 msec per loop
#  python -m timeit -n 100 -s "import task_2" "task_2.eratosfen(1000)"
# 100 loops, best of 3: 5.46 msec per loop

# python -m timeit -n 100 -s "import task_2" "task_2.simple(10)"
# 100 loops, best of 3: 28.6 usec per loop
# python -m timeit -n 100 -s "import task_2" "task_2.simple(20)"
# 100 loops, best of 3: 107 usec per loop
# python -m timeit -n 100 -s "import task_2" "task_2.simple(30)"
# 100 loops, best of 3: 209 usec per loop
# python -m timeit -n 100 -s "import task_2" "task_2.simple(40)"
# 100 loops, best of 3: 372 usec per loop
# python -m timeit -n 100 -s "import task_2" "task_2.simple(50)"
# 100 loops, best of 3: 572 usec per loop
# python -m timeit -n 100 -s "import task_2" "task_2.simple(100)"
# 100 loops, best of 3: 2.47 msec per loop
# python -m timeit -n 100 -s "import task_2" "task_2.simple(150)"
# 100 loops, best of 3: 6.08 msec per loop
# python -m timeit -n 100 -s "import task_2" "task_2.simple(200)"
# 100 loops, best of 3: 11.6 msec per loop
# python -m timeit -n 100 -s "import task_2" "task_2.simple(1000)"
# 100 loops, best of 3: 414 msec per loop

# cProfile.run('eratosfen(500)')
# 1    0.004    0.004    0.006    0.006 task_2.py:6(eratosfen)

# cProfile.run('simple(500)')
# 3568    0.089    0.000    0.089    0.000 task_2.py:20(is_simple)
#    1    0.001    0.001    0.091    0.091 task_2.py:26(simple)

# очевидно, что у алгоритма Эрастофена линейная сложность,
# но данная реализация имеет ограничение в поиске чисел
# т.к. требует начальной инициализации массива
# второй алгоритм болле быстрый на небольших значениях (почти до 200),
# но из за квадратичной сложности
# становится крайне неэффективным уже при числах больше 200.
# Однако, он не имеет ограничений в поиске т.к. не использует
# массив
