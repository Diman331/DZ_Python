# Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают
# Список уникальных элементов [1, 4, 2, 3, 6, 7]

import random

numbers = [random.randint(1, 10) for i in range(10)]
num_duplicates = len(numbers) - len(set(numbers))
unique_numbers = list(set(numbers))

print(f"{numbers} -> {num_duplicates} элемента совпадают")
print("Список уникальных элементов:", unique_numbers)
