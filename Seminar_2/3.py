# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

str1 = input('Введите первую строку: ')
str2 = input('Ввдедите вторую строку: ')

char_count = {}


for char in str1:
    count = str2.count(char)
    char_count[char] = count

for char, count in char_count.items():
    print(char, '-', count)