import requests
import json
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, ParseMode, InlineKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler)
import requests
from src import signup, login, Bot, utils, perfil, tips, handlers, getSaude
from src.CustomCalendar import CustomCalendar
from datetime import date
import time

CHOOSING, SEND_LOC = range(2)

# sintomas = [['Dor de Cabeça'], ['Localização'], ['Localização']]
sintomas =  [['Dor de cabeça', 'Bolhas na Pele', 'Mal-estar'],
            ['Bolhas na Pele', 'Congestão Nasal', 'Náuseas'],
            ['Diarréia', 'Dificuldade de respirar', 'Olhos vermelhos'],
            ['Dor nas Articulações', 'Febre', 'Tosse'],
            ['Dor no Estômago', 'Dor nos Músculos', 'Sangramentos'],
            ['Dor nos Olhos', 'Calafrios', 'Vômito'],
            ['Pele e olhos avermelhados', 'Manchas vermelhas no corpo'],
            ['Localização','Voltar', 'Done']]


def start(update, context):
    
    if utils.is_logged(context.user_data):

        if getSaude.verif_status_report(update, context):

            update.message.reply_text(
                "Notamos que hoje já foi realizado o report.\nRetornando ao menu.")

            handlers.menu(update, context)

        else:
            user_data = context.user_data
            
            # resposta = context.user_data
            context = context.user_data

            user_data['Keyboard'] = [['Sim, estou bem.', 'Não, não estou bem.']]

            markup = ReplyKeyboardMarkup(user_data['Keyboard'], one_time_keyboard=True, resize_keyboard=True)

            update.message.reply_text(
                "Olá, como você está se sentindo?",
                reply_markup=markup)

        # return CHOOSING
    else:

        handlers.unknown(update, context)
        return ConversationHandler.END

