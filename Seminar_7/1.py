def custom_map(func, iterable):
    return (func(item) for item in iterable)

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]

result = custom_map(square, numbers)

print(list(result))
