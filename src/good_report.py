import requests
import json
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, ParseMode, InlineKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler)
import requests
from src import signup, login, Bot, utils, perfil, tips, handlers, news
from src.CustomCalendar import CustomCalendar
from datetime import date
import time



def good_report(update, context):
    
    print("Good report!")

    # update.callback_query.edit_message_text("Obrigado por nos informar sobre seu estado de saúde.\n\nTenha um bom dia!")
    update.message.reply_text("Obrigado por nos informar sobre seu estado de saúde.\n\nTenha um bom dia!")

    headers =  {'Accept' : 'application/vnd.api+json', 'Content-Type' : 'application/json', 'Authorization' : str(context.user_data['AUTH_TOKEN'])}
    
    json = {
        "survey" : {
            "symptom" : []
        }
    }

    requests.post(url=f'http://localhost:3001/users/{context.user_data["id"]}/surveys', headers=headers, json=json)

    # news.run(update, context)
    handlers.menu(update, context)

    return -1 # END
