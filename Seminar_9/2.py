import numpy as np

# Создание случайного двумерного массива размером 5x5
arr = np.random.randint(low=0, high=10, size=(5, 5))

# Проверка наличия одинаковых строк
has_duplicate_rows = len(np.unique(arr, axis=0)) != arr.shape[0]

print(arr)
if has_duplicate_rows:
    print("В массиве есть одинаковые строки.")
else:
    print("В массиве нет одинаковых строк.")
