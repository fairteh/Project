import telebot
from wiki import get_wiki_page

bot = telebot.TeleBot('5710388198:AAEuyumpHAiD8b0iufx2cOkDSOLsFDM2cg4')


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, get_wiki_page(message.text))

