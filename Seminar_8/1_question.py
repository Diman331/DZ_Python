import telebot
from telebot import types
import os

file_path = os.path.join(os.path.dirname(__file__), "obrashcheniya.txt")

# Устанавливаем токен вашего бота
TOKEN = '5844786281:AAGABgL1pQyZhRiqgrgei3nvxnn-MhyDiOk'

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Словарь для хранения статуса регистрации обращения каждого пользователя
registration_status = {}


@bot.message_handler(commands=['start'])
def handle_start(message):
    # Приветствие и предложение зарегистрировать обращение
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    register_button = types.KeyboardButton('Зарегистрировать обращение')
    markup.add(register_button)

    bot.reply_to(message, 'Добро пожаловать! Я бот техподдержки. '
                          'Чтобы зарегистрировать обращение, нажмите кнопку "Зарегистрировать обращение".',
                 reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    if message.text == 'Зарегистрировать обращение':
        # Проверяем статус регистрации обращения пользователя
        if registration_status.get(chat_id):
            bot.reply_to(message, 'У вас уже зарегистрировано обращение. '
                                  'Ожидайте ответа на ваше предыдущее сообщение.')
        else:
            registration_status[chat_id] = True
            bot.reply_to(message, 'Пожалуйста, напишите ваше обращение.')
    elif registration_status.get(chat_id):
        # Записываем обращение пользователя в файл
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(f'{message.message_id}: {chat_id}: {message.from_user.username}: {message.text}\n')

        # Сбрасываем статус регистрации обращения пользователя
        registration_status[chat_id] = False

        # Отвечаем пользователю
        bot.reply_to(message, f'Ваше обращение зарегистрировано под номером #{message.message_id} Мы свяжемся с вами в ближайшее время.')
    else:
        bot.reply_to(message, 'Пожалуйста, используйте кнопку "Зарегистрировать обращение" для отправки обращения.')


# Запускаем бота
bot.polling()
