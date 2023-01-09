import os, sys

from telegram.ext import *
import responses
import telegram.bot

API_KEY = 'API_KEY'

PARAMETER_INFO = "Bitte gib auch die benötigten Parameter an!\nMögliche Parameter für die einzelnen Befehle findest du unter /help"


class TelegramBot:
    def __init__(self):
        self.updater = Updater(API_KEY, use_context=True)
        self.dp = self.updater.dispatcher

        self.dp.add_handler(CommandHandler("start", self.start))
        self.dp.add_handler(CommandHandler("help", self.help_command))
        self.dp.add_handler(CommandHandler("image", self.image_command, pass_args=True))
        self.dp.add_handler(CommandHandler("cache_time", self.cache_time, pass_args=True))
        self.dp.add_handler(CommandHandler("cache_size", self.cache_size, pass_args=True))
        self.dp.add_handler(CommandHandler("cache_delete_elements", self.cache_delete_elements, pass_args=True))

        self.dp.add_handler(MessageHandler(Filters.photo, self.translate))
        self.dp.add_handler(MessageHandler(Filters.text, self.handle_message))

        self.dp.add_error_handler(self.error)

        self.bot = telegram.Bot(token=API_KEY)

        self.responses = responses.Responses()

    def start(self, update, context):
        update.message.reply_text(
            "Hallo! Ich bin ein ChatGPT Telegram Bot. Schreibe einfach etwas um zu Starten oder nutze /help für Hilfe!")

    def help_command(self, update, context):
        update.message.reply_text("Schreibe einfach etwas und ChatGPT wird dir antworten!\n\n"
                                  "Weitere AI Befehle:\n\n"
                                  "/image [Bildbeschreibung] - DALL·E generiert ein Bild mit der Beschreibung\n\n"
                                  "/translate [Sprache] [Bild] - GPT-3 übersetzt ein Bild von der angegebenen Sprache ins Deutsche\n\n"
                                  "Cache Settings:\n\n"
                                  "/cache_time [Zeit in Min] - Setzen der Zeit nach der der Cache gelöscht wird\n\n"
                                  "/cache_size [Größe] - Setze die maximale Größe des Caches\n\n"
                                  "/cache_delete_elements [Anzahl] - Anzahl der Elemente die nach überschreiten der Cache Größe gelöscht werden\n\n")

    def cache_time(self, update, context):
        if context.args:
            self.responses.cache_time = int(context.args[0]) * 60
            self.responses.cache_time = int(self.responses.cache_time)
            update.message.reply_text(
                "Der Cache wird jetzt nach " + str(self.responses.cache_time / 60) + " Minuten gelöscht!")
        else:
            update.message.reply_text(PARAMETER_INFO)

    def cache_size(self, update, context):
        if context.args:
            self.responses.cache_size = context.args[0]
            self.responses.cache_size = int(self.responses.cache_size)
            update.message.reply_text(
                "Der Cache wird jetzt nach " + str(self.responses.cache_size) + " Elementen geleert!")
        else:
            update.message.reply_text(PARAMETER_INFO)

    def cache_delete_elements(self, update, context):
        if context.args:
            self.responses.cache_delete_elements = context.args[0]
            self.responses.cache_delete_elements = int(self.responses.cache_delete_elements)
            update.message.reply_text(
                "Nach überschreiten der Cache Größe werden jetzt die ersten " + str(
                    self.responses.cache_delete_elements) + " Elemente gelöscht!")
        else:
            update.message.reply_text(PARAMETER_INFO)

    def image_command(self, update, context):
        if context.args:
            prompt = context.args
            string_list = [str(s) for s in prompt]
            result = ' '.join(string_list)
            self.bot.send_photo(chat_id=update.message.chat.id, photo=self.responses.dalle(result))
        else:
            update.message.reply_text(PARAMETER_INFO)

    def translate(self, update, context):
        language_adj = ""
        if str(update.message.caption).lower().startswith("/translate"):
            language = update.message.caption.lower().split(" ")[1]
            if language:
                match language:
                    case "latein":
                        language_adj = "lateinischen"
                    case "englisch":
                        language_adj = "englischen"
                    case "französisch":
                        language_adj = "französischen"
                    case "spanisch":
                        language_adj = "spanischen"
                    case _:
                        update.message.reply_text("Sprache nicht gefunden!")
                if update.message.photo:
                    file_id = update.message.photo[-1].file_id
                    new_file = context.bot.get_file(file_id)
                    new_file.download("image.jpg")

                for file in os.listdir("./"):
                    if file.endswith(".jpg") or file.endswith(".png"):
                        print("[INFO] Bild gefunden: " + file + "\n[INFO] Übersetzung wird geladen...")
                        update.message.reply_text(self.responses.send_text(self.responses.get_text(file), language_adj))
            else:
                update.message.reply_text(PARAMETER_INFO)

    def handle_message(self, update, context):
        text = str(update.message.text).lower()
        response = self.responses.chatgpt(text)
        update.message.reply_text(response)

    def error(self, update, context):
        print(f"Update {update} caused error {context.error}")

    def main(self):
        self.updater.start_polling(1)
        self.updater.idle()


if __name__ == '__main__':
    print(r""" 
  ___                      _    ___   ____        _   
 / _ \ _ __   ___ _ __    / \  |_ _| | __ )  ___ | |_ 
| | | | '_ \ / _ \ '_ \  / _ \  | |  |  _ \ / _ \| __|
| |_| | |_) |  __/ | | |/ ___ \ | |  | |_) | (_) | |_ 
 \___/| .__/ \___|_| |_/_/   \_\___| |____/ \___/ \__|
      |_|                                                                                          
   """)
    telegram_bot = TelegramBot()
    telegram_bot.main()
