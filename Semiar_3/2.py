
fruits = ['абрикос', 'авокадо', 'апельсин', 'айва', 'банан', 'виноград', 'груша']

letter = input('Введите букву: ')

for fruit in fruits:
    if fruit.startswith(letter):
        print(fruit)
