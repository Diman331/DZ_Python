import numpy as np

# Генерация случайного размера массива (от 2 до 5)
size = np.random.randint(2, 6)

# Создание случайного двумерного массива заданного размера
arr = np.random.randint(low=0, high=10, size=(size, size))

# Вывод изначального массива
print("Изначальный массив:")
print(arr)

# Нахождение индексов максимального и минимального элементов
max_index = np.unravel_index(arr.argmax(), arr.shape)
min_index = np.unravel_index(arr.argmin(), arr.shape)

# Вывод индексов максимального и минимального элементов
print("Индекс максимального элемента:", max_index)
print("Индекс минимального элемента:", min_index)

# Вывод элементов главной диагонали в виде одномерного массива
diagonal_elements = np.diag(arr)
print("Элементы главной диагонали:", diagonal_elements)
