# Определить, какое число в массиве встречается чаще всего.


import random

r = [random.randint(0, 15) for _ in range(15)]
print(f'Массив: {r}')

max_index = 0
for i in r:
    if r.count(max_index) < r.count(i):
        max_index = r.index(i)

print(f'Число {r[max_index]}, встречается {r.count(max_index)} раз(а)')