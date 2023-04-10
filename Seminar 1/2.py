# Задача 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

import math

x1 = float(input("Введите координату x первой точки: "))
y1 = float(input("Введите координату y первой точки: "))
x2 = float(input("Введите координату x второй точки: "))
y2 = float(input("Введите координату y второй точки: "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Расстояние между двумя точками: ", round(distance, 2))