from telegram import ReplyKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler)
import requests
import src.utils as utils
import src.signup as signup
import src.login as login
import time


#Envia o menu para o usuario
def start(update, context):

    if utils.is_logged(context.user_data):
        reply_keyboard = [['Minhas informações','Sobre'],
                          ['Sobre','Logout']]
    
    else:
        reply_keyboard = [['Login','Registrar'],
                      ['Sobre','Finalizar']]

    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)

    resposta = ("Bem vindo ao DoctorS Bot, selecione a opção desejada.\n\n"
                "Caso deseje voltar ao menu, digite /menu ou /start.\n")

    context.bot.send_message(
        chat_id=update.effective_chat.id, text=resposta, reply_markup=markup
    )

def menu(update, context):
    if utils.is_logged(context.user_data):
        reply_keyboard = [['Minhas informações','Sobre'],
                          ['Sobre','Logout']]
    
    else:
        reply_keyboard = [['Login','Registrar'],
                      ['Sobre','Finalizar']]

    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    resposta = "Selecione a opção desejada!"

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=resposta,
        reply_markup=markup
    )



def get_user_info(update, context):
    if utils.is_logged(context.user_data):
        user_data = context.user_data
        resposta = "Nome: "+user_data['Username']+ "\nEmail: " +  user_data['Email']
        
        context.bot.send_message(chat_id=update.effective_chat.id, text=resposta)

    else:
        unknown(update, context)


#Cadastra novo user
def signup_handler():
    return ConversationHandler(
            entry_points=[MessageHandler(Filters.text("Registrar"), signup.start)],
            states={
                signup.CHOOSING: [MessageHandler(Filters.regex('^(Username|Email|Senha|Genero sexual|Raça|Trabalho)$'),
                                        signup.regular_choice)
                        ],
                signup.TYPING_CHOICE: [
                    MessageHandler(Filters.text & ~(Filters.command | Filters.regex('^Done$')),
                                signup.regular_choice)],
                signup.TYPING_REPLY: [
                    MessageHandler(Filters.text & ~(Filters.command | Filters.regex('^Done$')),
                                signup.received_information)],
            },
            fallbacks=[MessageHandler(Filters.regex('^Done$'), signup.done),
            MessageHandler(Filters.regex('^Cancelar$'), cancelSignup)],
            allow_reentry=True
            )
            
def cancelSignup(update, context):
    signup.clearInfo(context)
    menu(update, context)
            
def logout(update, context):
    
    if utils.is_logged(context.user_data):
        resposta = f"Já vai?\n\nAté a próxima {context.user_data['Username']}!\n\nPara ver o menu digite /menu ou /start!"
        
        #Limpa a sessão do usuário
        context.user_data.clear()

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=resposta
        )

    else:
        #Caso não esteja logado, não entra na função de logout
        unknown(update, context)

#Login de usuario
def login_handler():
    return ConversationHandler(
            entry_points=[MessageHandler(Filters.text("Login"), login.start)],
            states={
                login.CHOOSING: [MessageHandler(Filters.regex('^(Email|Senha)$'),
                                        login.regular_choice)
                        ],
                login.TYPING_CHOICE: [
                    MessageHandler(Filters.text & ~(Filters.command | Filters.regex('^Done$')),
                                login.regular_choice)],
                login.TYPING_REPLY: [
                    MessageHandler(Filters.text & ~(Filters.command | Filters.regex('^Done$')),
                                login.received_information)],
            },
            fallbacks=[MessageHandler(Filters.regex('^Done$'), login.done),
            MessageHandler(Filters.regex('^Cancelar$'), cancelLogin)],
            allow_reentry=True
            )

def cancelLogin(update, context):
    login.clearInfo(context)
    menu(update, context)

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
    resposta = "Não entendi. Tem certeza de que digitou corretamente?\n\nRetornando ao menu."
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=resposta,
    )

    menu(update, context)
