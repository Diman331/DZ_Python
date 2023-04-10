# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial_list(n):
    result = []
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
        result.append(factorial)
    return result

n = int(input("Введите число N: "))
print(factorial_list(n))