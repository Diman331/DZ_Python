import numpy as np

# Создание случайного массива из 10 элементов в диапазоне от 0 до 9
arr = np.random.randint(0, 10, size=10)

# Подсчет уникальных элементов и их количества
unique_elements, counts = np.unique(arr, return_counts=True)

# Получение общего количества уникальных элементов
count_unique_elements = len(unique_elements)

print("Массив:", arr)
print("Количество уникальных элементов:", count_unique_elements)
print("Уникальные элементы и их количество:")
for element, count in zip(unique_elements, counts):
    print(element, ":", count)
