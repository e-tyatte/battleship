import telebot
from openai import OpenAI
from gtts import gTTS
import os

# Замените на ваш токен Telegram-бота
TELEGRAM_BOT_TOKEN = "Вставить токен"

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

client = OpenAI(
    api_key="Вставить ключ",
    base_url="https://api.proxyapi.ru/openai/v1",
)

def initialize_game():
    initial_message = "Мы начинаем игру в морской бой. Расставь свои корабли и сделай первый ход."
    return initial_message

def make_move(move):
    messages = [
        {"role": "system", "content": "Ты играешь в морской бой."},
        {"role": "user", "content": f"Мой ход: {move}"},
    ]

    # Убедитесь, что используете правильную модель
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Исправленное название модели
        messages=messages
    )
    return response.choices[0].message.content

def text_to_speech(text, filename="response.mp3"):
    tts = gTTS(text, lang='ru')
    tts.save(filename)
    return filename

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    initial_message = initialize_game()
    bot.reply_to(message, initial_message)

    # Отправляем аудио
    audio_file = text_to_speech(initial_message)
    with open(audio_file, 'rb') as audio:
        bot.send_voice(message.chat.id, audio)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_move = message.text

    if user_move.lower() == "exit":
        response = "Игра окончена."
    else:
        response = make_move(user_move)

    bot.reply_to(message, response)

    # Отправляем аудио
    audio_file = text_to_speech(response)
    with open(audio_file, 'rb') as audio:
        bot.send_voice(message.chat.id, audio)

if __name__ == "__main__":
    bot.polling()