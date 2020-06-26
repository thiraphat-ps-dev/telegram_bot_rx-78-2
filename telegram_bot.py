import googletrans
from googletrans import Translator
import telebot

from gtts import gTTS 
  
import os 
  # -*- coding: utf-8 -*-
def telegram_bot():
    bot = telebot.TeleBot("937087621:AAGAK-h5DmH3BJy2-a1lCKgad6-aJPyGqag")


    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message, "สวัสดีครับนายท่าน มีอะไรให้ผมช่วยไหมครับ?")
        


    @bot.message_handler(commands=['translate', 'Translate'])
    def echo_msg(message):
        bot.register_next_step_handler(message, callback=extract_msg)

    @bot.message_handler(commands=['texttospeech', 'Texttospeech'])
    def echo_msg(message):
        bot.register_next_step_handler(message, callback=extract_msg_to_sound)


    def extract_msg(message):
        translator = Translator()
        lang = translator.detect(message.text)
        if lang.lang == 'th':
            translator = Translator()
            result = translator.translate(message.text, src='th', dest='en')
            bot.reply_to(message, result.text)
            myobj = gTTS(text=result.text, lang='en', slow=False) 
        else:
            translator = Translator()
            result = translator.translate(message.text, src='en', dest='th')
            bot.reply_to(message, result.text)
            myobj = gTTS(text=result.text, lang='th', slow=False) 

        myobj.save('texttospeech.mp3') 
        # os.system('afplay output.mp3')
        audio = open('texttospeech.mp3', 'rb')
        bot.send_audio(887732214,audio)

    def extract_msg_to_sound(message):
        translator = Translator()
        lang = translator.detect(message.text)
        myobj = gTTS(text=message.text, lang=lang.lang, slow=True) 
        myobj.save('texttospeech.mp3') 
        # os.system('afplay output.mp3')
        audio = open('texttospeech.mp3', 'rb')
        bot.send_audio(887732214,audio)


    bot.polling()
