#!/usr/bin/python
g = 9.8
x = int(input("Введите начальное положение: "))
t = int(input("Введите время движения: "))
v = int(input("Введите начальную скорость: "))
L = x + v * t + ((g * t * t) / 2)
print("Расстояние = ", L)
