#!/usr/bin/python
print("Введите возводимое в степень число и саму степень.")
a = float(input())
n = int(input())
result = 1.0

for i in range(abs(n)):
    result *= a

if n < 0:
    result = 1 / result

print(result)
