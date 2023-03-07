from datetime import datetime
import telebot 
import time 

bot=telebot.TeleBot("6282321784:AAEOKdwxXHK0fqzbtUi_CdDKH872phoUD94")

@bot.message_handler(func=lambda m : True)
def time(message):
    if message.text=="الوقت":
        bot.reply_to(message,f"ألان بتوقيت العراق\n{oo}\n{ww}")

now = datetime.now()
oo = (now.strftime('الساعة:  %I:%M:%S'))

now = datetime.now()
ww = (now.strftime("التاريخ:  20%y/%m/%d"))

print(f' {oo}   {ww} ')

bot.infinity_polling()