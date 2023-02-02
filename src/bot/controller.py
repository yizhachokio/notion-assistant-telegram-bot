import os

import i18n
import telebot


class Controller:

    def __init__(self):
        # setting up translation
        i18n.set('file_format', 'json')
        i18n.set('locale', 'en')
        i18n.load_path.append("res/translations")

        TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
        bot = telebot.TeleBot(TOKEN)

        @bot.message_handler(commands=['start', 'help'])
        def command_help(message):
            bot.reply_to(message, i18n.t("tr.start_help"))

        @bot.message_handler(func=lambda message: True,
                             content_types=['audio', 'video', 'document', 'text', 'location', 'contact', 'sticker'])
        def default_command(message):
            bot.reply_to(message, "tr.test")

        print("Bot has started!")
        bot.infinity_polling()