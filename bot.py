import logging
from telegram.ext import (Updater, CommandHandler, MessageHandler, 
                    Filters, ConversationHandler, RegexHandler)
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)

TOKEN = "915778771:AAHbrbLAl51meJf5Pz3siZ4QIGjiJMTcvB0"

updater = Updater(token = TOKEN, use_context = True)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
    main_menu_keyboard = [['Трудоустройство'] , ['Законодательство'], ['Консультация']]
    reply_markup = ReplyKeyboardMarkup(main_menu_keyboard)
    
    context.bot.send_message(chat_id=update.effective_chat.id, 
        text="Здравствуйте, я бот который бла бла",
        reply_markup=reply_markup)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def work(update, context):
    work_menu_keyboard = [['HeadHunter'] , ['Olx.kz'], ['Центр занятости г.Нур-Султан'], ['Назад']]
    reply_markup = ReplyKeyboardMarkup(work_menu_keyboard)
    
    context.bot.send_message(chat_id=update.effective_chat.id, 
        text="Выберите один из желаемых вариантов",
        reply_markup=reply_markup)

work_handler = MessageHandler(Filters.regex('Трудоустройство'), work)
dispatcher.add_handler(work_handler)

def hh(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
        text="Перейдите по этой ссылке https://hh.kz/")

hh_handler = MessageHandler(Filters.regex('HeadHunter'), hh)
dispatcher.add_handler(hh_handler)

def olx(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
        text="Перейдите по этой ссылке https://olx.kz/")

olx_handler = MessageHandler(Filters.regex('Olx.kz'), olx)
dispatcher.add_handler(olx_handler)

def center(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
        text="Перейдите по этой ссылке http://cz.astana.kz/")

center_handler = MessageHandler(Filters.regex('Центр занятости г.Нур-Султан'), center)
dispatcher.add_handler(center_handler)

def rules(update, context):
    rules_menu_keyboard = [['Ссылка на список документов'] , ['Перечень документов'], ['Назад']]
    reply_markup = ReplyKeyboardMarkup(rules_menu_keyboard)
    
    context.bot.send_message(chat_id=update.effective_chat.id, 
        text="Выберите один из желаемых вариантов",
        reply_markup=reply_markup)

rules_handler = MessageHandler(Filters.regex('Законодательство'), rules)
dispatcher.add_handler(rules_handler)

def docsURL(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
        text="http://adilet.zan.kz/rus/docs/U1600000387#z10")

docsURL_handler = MessageHandler(Filters.regex('Ссылка на список документов'), docsURL)
dispatcher.add_handler(docsURL_handler)

def docsList(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
        text="Перечень документов")

docsList_handler = MessageHandler(Filters.regex('Перечень документов'), docsList)
dispatcher.add_handler(docsList_handler)


def consult(update, context):
    consult_menu_keyboard = [['iKomek'] , ['Юридическая консультация'], ['Назад']]
    reply_markup = ReplyKeyboardMarkup(consult_menu_keyboard)
    
    context.bot.send_message(chat_id=update.effective_chat.id, 
        text="Выберите один из желаемых вариантов",
        reply_markup=reply_markup)

consult_handler = MessageHandler(Filters.regex('Консультация'), consult)
dispatcher.add_handler(consult_handler)

def iKomek(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
        text="http://astana.gov.kz/ru/ikomek/about")

iKomek_handler = MessageHandler(Filters.regex('iKomek'), iKomek)
dispatcher.add_handler(iKomek_handler)

def jConsult(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
        text="Юридическая консультация")

jConsult_handler = MessageHandler(Filters.regex('Юридическая консультация'), jConsult)
dispatcher.add_handler(jConsult_handler)

def back(update, context):
    start(update, context)

back_handler = MessageHandler(Filters.regex('Назад'), back)
dispatcher.add_handler(back_handler)

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)



updater.start_polling()