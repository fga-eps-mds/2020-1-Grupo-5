import requests
import json
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, ParseMode, InlineKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler)
import requests
from src import signup, login, Bot, utils, perfil, tips, handlers
from src.CustomCalendar import CustomCalendar
from datetime import date
import time

CHOOSING, SEND_LOC = range(2)

# sintomas = [['Dor de Cabeça'], ['Localização'], ['Localização']]
sintomas =  [['Dor de Cabeça', 'Localização', 'Voltar']]

#Mensagens não reconhecidas
def unknown(update, context):
    resposta = "Não entendi. Tem certeza de que digitou corretamente?\n\nRetornando ao menu."
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=resposta,
    )
    handlers.menu(update, context)


def daily_report(update, context):
    if utils.is_logged(context.user_data):
        
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Ativado notificações diárias")
        
        day_in_sec = 10# Dia em segundos
        
        # CHAMA DE ACORDO COM UM TEMPO A FUNÇÃO "notify_assignees"
        context.job_queue.run_repeating(notify_assignees, day_in_sec, context=update.message.chat_id)
    
    else:
        unknown(update, context)




def cancel_daily(update, context):
    if utils.is_logged(context.user_data):
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Notificações diárias desativadas"
        )

        context.job_queue.stop()
    else:
        unknown(update, context)

#   FUNÇÃO CHAMADA QUE PERGUNTA SE ESTA BEM OU NÃO
def notify_assignees(context):

    sim = InlineKeyboardButton(text="Sim",callback_data='bad_report')
    nao = InlineKeyboardButton(text="Não", callback_data='good_report')

    chat_id=context.job.context

    # Mensagem teste
    context.bot.send_message(
        chat_id=chat_id,
        text="Sentiu sintomas hoje?",
        reply_markup=InlineKeyboardMarkup([[sim, nao]], 
                                        resize_keyboard=True)
    )
    
def good_report(update, context):
    
    update.callback_query.edit_message_text("Obrigado por nos informar sobre seu estado de saúde.\n\nTenha um bom dia!")
