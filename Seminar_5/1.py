import random

numbers = [random.randint(1, 10) for i in range(10)]
filtered_numbers = list(filter(lambda x: x > 5, numbers))

print(f'{numbers} -> {filtered_numbers}')
