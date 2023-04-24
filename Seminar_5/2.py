# Дан список случайных чисел. Создайте список, в который попадают числа, 
# описывающие случайную возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.

numbers = [1, 5, 2, 3, 4, 6, 1, 7]

increasing_subsequences = []
current_subsequence = []

for i in range(len(numbers)-1):
    if numbers[i] < numbers[i+1]:
        current_subsequence.append(numbers[i])
    else:
        current_subsequence.append(numbers[i])
        increasing_subsequences.append(current_subsequence)
        current_subsequence = []

if current_subsequence and current_subsequence[-1] < numbers[-1]:
    current_subsequence.append(numbers[-1])
    increasing_subsequences.append(current_subsequence)

longest_increasing_subsequence = max(increasing_subsequences, key=len)

print(longest_increasing_subsequence)
