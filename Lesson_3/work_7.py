# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.


import random

r = [random.randint(0, 20) for _ in range(15)]
print(f'Массив: {r}')

min_index_1 = 0
min_index_2 = 1

sort_list = []
sort_list.extend(r)
sort_list.sort()

print(f'Два наименьших элемента: {sort_list[0]} и {sort_list[1]}')