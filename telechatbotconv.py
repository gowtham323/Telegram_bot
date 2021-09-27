import os
from typing import IO
import telebot
import yfinance as yf
from PIL import Image
import io

def Main():
    bot = telebot.TeleBot(
            "2029622795:AAE-iwOHCymvbB320D-BL81MbJ02PDZz4jM", parse_mode=None)


    @bot.message_handler(commands=['Greet'])
    def greet(message):
        bot.reply_to(message, "Hey!, How is your day?")


    @bot.message_handler(commands=['wsb'])
    def get_stocks(message):
        response = yf.download(tickers='gme', period='2d', interval='1d')
        bot.send_message(message.chat.id, response)


    @bot.message_handler(content_types=['photo'])
    def photo(message):
        print('message.photo =', message.photo)
        fileID = message.photo[-1].file_id
        print('fileID =', fileID)
        file_info = bot.get_file(fileID)
        print('file.file_path =', file_info.file_path)
        downloaded_file = bot.download_file(file_info.file_path)

        img = Image.open(io.BytesIO(downloaded_file))
        img = img.convert("L")
        img = img.save("img.jpg")
        with open("img.jpg", "rb") as open_img:
            bot.send_photo(message.chat.id, open_img)


    bot.set_webhook()
    bot.polling()

if __name__ == "__main__":
    Main()