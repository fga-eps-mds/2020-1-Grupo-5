from telegram import ReplyKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler)
import requests
import src.utils as utils
import time


#Envia o menu para o usuario
def start(update, context):
    reply_keyboard = [['Login','Registrar'],
                      ['Sobre','Finalizar']]

    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)

    resposta = ("Bem vindo ao DoctorS Bot, selecione a opção desejada.\n\n"
                "Caso deseje voltar ao menu, digite /menu ou /start.\n")

    update.message.reply_text(
        resposta, reply_markup=markup
    )

#Cadastra novo user
def signup_handler(update, context):
    signup(update,context)
        
#Login de usuario
def login(update, context):
    resposta = 'Ainda não foi implementada a função de login!\n\nEm breve implementaremos essa função!'

    context.bot.send_message(chat_id=update.effective_chat.id, text=resposta)

#Envia informaçoes sobre o bot
def sobre(update, context):
    resposta = 'O DoctorS é um Telegram Bot criado para ajudar a população no combate ao novo Corona Vírus(SARS-CoV-2).'
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=resposta
    )
    

def finalizar(update, context):
    resposta = """Já vai? Tudo bem, sempre que quiser voltar, digite /menu ou /start e receberá o menu inicial.\n\nObrigado por usar o DoctorS!"""

    context.bot.send_message(chat_id=update.effective_chat.id,
    text=resposta)

#Mensagens não reconhecidas
def unknown(update, context):
    resposta = "Não entendi. Tem certeza de que digitou corretamente?"
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=resposta,
    )




