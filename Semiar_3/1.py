# Задача 1. Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

N = int(input('Введите число N: '))
fibonacci = [1, 1]
for i in range(2, N):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

print(fibonacci)