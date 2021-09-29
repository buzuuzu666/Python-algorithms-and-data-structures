# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание:
# Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду.
# Также укажите в комментариях версию Python и разрядность вашей ОС.


'''
Python 3.9
Windows 10 x64
'''

'''Lesson_3/work_2'''

import sys
import random

r = [random.randint(0, 99) for _ in range(10)]
print(f'Первый массив {r}')
index_even = []

for n in r:
    if n % 2 == 0:
        index_even.append(r.index(n))

print(f'Индексы чётных элементов первого массива: {index_even}')

sum_size = 0
sum_size += sys.getsizeof(r) + sys.getsizeof(index_even) + sys.getsizeof(n)
print('===\nВыделено памяти:',sum_size,'байт\n===')


'''Lesson_3/work_3'''

ra = [random.randint(0, 99) for _ in range(10)]
print(f'Массив случайных чисел {r}\n'
      f'Максимальное число: {max(r)}. Минимальное число: {min(r)} ')

max = ra[0]
min = ra[0]

for i in ra:
    if i > max:
        max = i
    elif i < min:
        min = i

min_index = ra.index(min)
max_index = ra.index(max)
ra[min_index], ra[max_index] = ra[max_index], ra[min_index]
print(f'Массив после изменения элементов {ra}')

sum_size_1 = 0
sum_size_1 += sys.getsizeof(ra) + sys.getsizeof(max) + sys.getsizeof(min) + sys.getsizeof(i)
print('===\nВыделено памяти:',sum_size_1,'байт\n===')




'''Lesson_1/work_1'''
# Вариант решения 1

a = '999'
x = int(a[0])
y = int(a[1])
z = int(a[2])

sum_l = x + y + z
mult = x * y * z
print('Сумма:', sum_l, '\nСтепень:', mult)

sum_size_2 = 0
sum_size_2 += sys.getsizeof(a) + sys.getsizeof(x) + sys.getsizeof(y) + sys.getsizeof(z) \
              + sys.getsizeof(sum_l) + sys.getsizeof(mult)


# Вариант решения 2

num = int(999)

c = num % 10
ab = num // 10
b = ab % 10
a = ab // 10
num_1 = a + b + c
num_2 = a * b * c

print(f"Сумма цифр: {a} + {b} + {c} = {num_1}. \n"
      f"Произведение: {a} * {b} * {c} = {num_2}")


sum_size_3 = 0
sum_size_3 += sys.getsizeof(num) + sys.getsizeof(c) + sys.getsizeof(ab) + sys.getsizeof(b) + sys.getsizeof(a) \
              + sys.getsizeof(num_1) + sys.getsizeof(num_2)
print('===\nРешение 1 Выделено памяти:',sum_size_2,'байт\nРешение 2 Выделено памяти:',sum_size_3,'байт\n===')