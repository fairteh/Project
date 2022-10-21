from telegram_bot import bot


while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception:
        pass
