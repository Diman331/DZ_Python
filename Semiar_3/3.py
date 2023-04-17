# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. 
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». 
# Если фраза ему неизвестна, он выводит соответствующую фразу.

dictionary = {'привет': 'Привет!', 'как тебя зовут': 'Меня зовут Бот. А тебя?', 'как дела': 'Нормально. А у тебя?'}
unknown = 'Извините, я не понимаю, о чем вы говорите.'

def find_answer(phrase):
    for key in dictionary:
        if key in phrase.lower():
            return dictionary[key]
    return unknown

print("Привет! Я бот. Чем я могу вам помочь?")
while True:
    phrase = input("> ")
    if not phrase:
        break
    answer = find_answer(phrase)
    print(answer)