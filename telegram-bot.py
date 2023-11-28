import telebot
from telebot import types


class MyBot:
    def __init__(self):
        self.token = "6814815937:AAHFPDAsUL4OKlPXy70TvVy_NhBXOeuZrBg"
        self.bot = telebot.TeleBot("6814815937:AAHFPDAsUL4OKlPXy70TvVy_NhBXOeuZrBg")

        @self.bot.message_handler(commands=["start"])
        def start_bot(message):
            self.bot.send_message(message.chat.id, "おはよう (охайё), добро пожаловать в нашу\n\t🎶🎵🎶 муз. группу <b>Жгут</b> 🎶🎵🎶",
                                  parse_mode="html")
            self.bot.send_message(message.chat.id, "Ой, то есть, 🎸🎹🎧 <em>школьный клуб репетиций</em> 🎧🎹🎸,\nэхе-хе...",
                                  parse_mode="html")
            self.bot.send_message(message.chat.id, "...")
            self.bot.send_message(message.chat.id, "То есть...\n\nА, не бери в голову, короче, мы очень рады тебя приветствовать"
                                                 " здесь, в нашем небольшом храме!")

            self.set_main_menu_buttons(message)

        @self.bot.message_handler(commands=["sticker"])
        def send_sticker(message):
            self.bot.send_sticker(message.chat.id, sticker="CAACAgQAAxkBAAECKm1lZIpxEdo0ULeVLnqtgQ75_AF43AAC9wwAAtBU0VAJXmbeRL2ROjME")

        @self.bot.message_handler(commands=["help"])
        def send_help_info(message):
            self.bot.send_message(message.chat.id, "Помогу, чем смогу!")
            self.bot.send_message(message.chat.id, "Правда, пока что не чем...")

        @self.bot.message_handler()
        def send_help_info(message):
            self.bot.send_message(message.chat.id, "Я еще учусь, извини, если это что-то важное(")

    def run(self):
        self.bot.polling(none_stop=True)

    def set_main_menu_buttons(self, message):
        markup = types.ReplyKeyboardMarkup()

        btn1 = types.KeyboardButton("Дай стикеры")
        btn2 = types.KeyboardButton("Какие аниме ты знаешь?")
        btn3 = types.KeyboardButton("Что ты знаешь про Мику?")

        markup.row(btn1, btn2)
        markup.add(btn3)

        self.bot.send_sticker(message.chat.id, sticker="CAACAgQAAxkBAAECKm1lZIpxEdo0ULeVLnqtgQ75_AF43AAC9wwAAtBU0VAJXmbeRL2ROjME", reply_markup=markup)

    # test comment


if __name__ == "__main__":
    bot = MyBot()
    bot.run()



