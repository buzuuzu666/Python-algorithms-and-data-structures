# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


import random

r = [random.randint(0, 99) for _ in range(10)]
print(f'Массив случайных чисел {r}\n'
      f'Максимальное число: {max(r)}. Минимальное число: {min(r)} ')

max = r[0]
min = r[0]

for i in r:
    if i > max:
        max = i
    elif i < min:
        min = i

min_index = r.index(min)
max_index = r.index(max)
r[min_index], r[max_index] = r[max_index], r[min_index]
print(f'Массив после изменения элементов {r}')



