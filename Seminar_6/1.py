# Дано натуральное число N. Найдите значение выражения: N + NN + NNN
# N может быть любой длины.
# N = 132 -> 132 + 132132 + 132132132 = 132264396

n = input('Введите число N: ')
nn = n + n
nnn = n + nn
n, nn, nnn = map(int, [n, nn, nnn])
result = n + nn + nnn
print(f'{n} + {nn} + {nnn} = {result}')