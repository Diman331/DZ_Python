# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

N = int(input('Введите число N: ')) # количество элементов в списке
lst = list(range(-N, N+1)) # создание списка из N элементов, заполненных числами из промежутка [-N, N]
lst = lst[-2:] + lst[:-2] # сдвиг всех элементов списка на 2 позиции вправо
print(lst) # вывод списка на экран
