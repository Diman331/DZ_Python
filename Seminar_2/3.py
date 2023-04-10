str1 = input('Введите первую строку: ')
str2 = input('Ввдедите вторую строку: ')

char_count = {}


for char in str1:
    count = str2.count(char)
    char_count[char] = count

for char, count in char_count.items():
    print(char, '-', count)