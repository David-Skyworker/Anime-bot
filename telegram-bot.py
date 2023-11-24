import telebot

anime_bot = telebot.TeleBot("6814815937:AAHFPDAsUL4OKlPXy70TvVy_NhBXOeuZrBg")


@anime_bot.message_handler(commands=["start"])
def start_bot(chat_info):
    anime_bot.send_message(chat_info.chat.id, "おはよう (охайё), добро пожаловать в нашу\n\t🎶🎵🎶 муз. группу <b>Жгут</b> 🎶🎵🎶",
                           parse_mode="html")
    anime_bot.send_message(chat_info.chat.id, "Ой, то есть, 🎸🎹🎧 <em>школьный клуб репетиций</em> 🎧🎹🎸, хе-хе...",
                           parse_mode="html")
    anime_bot.send_message(chat_info.chat.id, "...")
    anime_bot.send_message(chat_info.chat.id, "То есть...\n\nА, не бери в голову, короче, мы очень рады тебя приветствовать"
                                         " здесь, в нашем небольшом храме!")

@anime_bot.message_handler(commands=["help"])
def send_help_info(chat_info):
    anime_bot.send_message(chat_info.chat.id, "Помогу, чем смогу!")
    anime_bot.send_message(chat_info.chat.id, "Правда, пока что не чем...")


@anime_bot.message_handler()
def send_help_info(chat_info):
    anime_bot.send_message(chat_info.chat.id, "Я еще учусь, извини, если это что-то важное(")


anime_bot.polling(none_stop=True)
