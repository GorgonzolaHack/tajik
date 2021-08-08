# -*- coding: utf8 -*-
#1030811973
import telebot
import requests
from fake_useragent import UserAgent
from time import sleep
from telebot import types

UserAgent().chrome

bot = telebot.TeleBot("1936106080:AAEmIlPJyO0MldFs7avtMHFdEd6TAYQKyqU")

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Привет! Я Кабанчик онлайн! Я выучил таджицкий!")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

#   translator= Translator(to_lang="tg")
#   translation = translator.translate(message.text)
    page = (requests.get("https://ru.contdict.com/перевод/русский-таджикский/"+message.text, headers={'User-Agent': UserAgent().chrome})).text
    start = 68+(page.find('id="translit"'))
    end = page.find('<',start)
    translation = page[start:end]
    if translation == "":
        bot.send_message(message.chat.id, "Не нашёл перевода(")
        return
    bot.send_message(message.chat.id, translation)
bot.polling()
