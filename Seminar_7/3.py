import telebot
import random

bot = telebot.TeleBot("ваш_токен")

secret_number = random.randint(1, 1000)

guesses = 0

@bot.message_handler(commands=['start'])
def start(message):
    global secret_number, guesses
    secret_number = random.randint(1, 1000)
    guesses = 0
    bot.send_message(message.chat.id, "Привет! Я загадал число от 1 до 1000. Попробуй угадать!")

@bot.message_handler(func=lambda message: True)
def guess_number(message):
    global secret_number, guesses

    try:
        guess = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите целое число.")
        return

    guesses += 1

    if guess == secret_number:
        bot.send_message(message.chat.id, f"Поздравляю, вы угадали число {secret_number}! Количество ходов: {guesses}")
    elif guess < secret_number:
        bot.send_message(message.chat.id, "Загаданное число больше.")
    else:
        bot.send_message(message.chat.id, "Загаданное число меньше.")

bot.polling()
