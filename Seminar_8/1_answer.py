import time
import telebot
import os

file_path = os.path.join(os.path.dirname(__file__), "obrashcheniya.txt")
print(file_path)
# Создаем экземпляр бота
bot = telebot.TeleBot('5844786281:AAGABgL1pQyZhRiqgrgei3nvxnn-MhyDiOk')

def read_messages_from_file():
    messages = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                messages.append(line)
    return messages


def send_reply(ID_message, ID_chat, reply_text):
    bot.send_message(chat_id=ID_chat, text= f' Ответ на обращение #{ID_message}:\n {reply_text}', reply_to_message_id=ID_message)

def remove_message_from_file(message):
    with open(file_path, 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if line.strip() != message:
                file.write(line)
        file.truncate()

def process_messages():
    # Считываем сохраненные сообщения из файла
    saved_messages = read_messages_from_file()
    
    for message in saved_messages:
        parts = [part.strip() for part in message.split(":")]
        ID_message = parts[0]
        ID_chat = parts[1]
        ID_user = parts[2]
        text_r = ":".join(parts[3:])
        
        # Выводим сообщение для ответа в консоль
        print(f'Отправить ответ на сообщение(ID: {ID_message}) от пользователя {ID_user}:')
        print(text_r)
        
        # Читаем введенный ответ из консоли
        reply_text = input('Введите ответ: ')
        
        # Отправляем ответ пользователю через бота
        send_reply(ID_message, ID_chat, reply_text)
        
        # Удаляем строку из файла после ответа
        remove_message_from_file(message)

def check_new_messages(interval):
    while True:
        new_messages = read_messages_from_file()
        if len(new_messages) > 0:
            print(f"Обнаружены новые сообщения ({len(new_messages)}):")
            process_messages()
        else:
            print("Новых сообщений не обнаружено.")
        time.sleep(interval)

if __name__ == '__main__':
    check_interval = 10  # Интервал проверки новых сообщений (в секундах)
    check_new_messages(check_interval)
