# По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.

x1 = float(input('Введите координаты первой точки x1 '))
y1 = float(input('Введите координаты первой точки y1 '))
x2 = float(input('Введите координаты первой точки x2 '))
y2 = float(input('Введите координаты первой точки y2 '))
if x1 != x2:
    k = (y2 - y1)/(x2 - x1)
    b = (x2*y1 - x1*y2)/(x2 - x1)
    print(f'Уравнение прямой y = {k:.4f}x + {b:.4f}')
else:
    print(f'Уравнение прямой x = {x1:.4f}')