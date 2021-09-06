# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.

import string
from random import randint, uniform


strt = int(input('enter the start number'))
end = int(input('enter the ending number'))
smv = list(string.ascii_letters)


print(f'Случайное целое число: {randint(strt, end)}\n'
      f'Случайное вещественное число: {uniform(strt, end):.2f}\n'
      f'Случайный символ: {smv[randint(strt, end)]}')