# Задача 1. Дано натуральное число N. Напишите метод, который вернёт список простых множителей числа N и количество этих множителей.
# 60 -> 2, 2, 3, 5

import math

n = int(input('Введите число N: '))

def prime_factors(n):
    factors = []
    count = 0
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            factors.append(i)
            n //= i
            count += 1
        else:
            i += 1
    if n > 1:
        factors.append(n)
        count += 1
    return factors, count
factors, count = prime_factors(n)
print("Простые множители числа {}: {}".format(n, factors))
print("Количество простых множителей числа {}: {}".format(n, count))