from telegram import ReplyKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler)
import requests
from src import signup, login, Bot, utils, perfil
from src.CustomCalendar import CustomCalendar
from datetime import date
import time



#Envia o menu para o usuario
def start(update, context):

    if utils.is_logged(context.user_data):
        reply_keyboard = [['Minhas informações','Sobre'],
                          ['Sobre','Logout']]
    
    else:
        reply_keyboard = [['Login','Registrar'],
                      ['Sobre','Finalizar']]

    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)

    resposta = ("Bem vindo ao DoctorS Bot, selecione a opção desejada.\n\n"
                "Caso deseje voltar ao menu, digite /menu ou /start.\n")

    context.bot.send_message(
        chat_id=update.effective_chat.id, text=resposta, reply_markup=markup
    )

    link = "https://scontent-gig2-1.xx.fbcdn.net/v/t1.0-9/103274216_112293347182974_7934951402525681679_o.png?_nc_cat=101&ccb=2&_nc_sid=85a577&_nc_ohc=DfmCZ9ndG5cAX-Mq4qP&_nc_ht=scontent-gig2-1.xx&oh=0566da2b649761aa3348d1f8c89c640a&oe=5FBA8F35"
    # context.bot.send_photo(chat_id=chat_id, photo=open('tests/test.png', 'rb'))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=link)





def menu(update, context):
    if utils.is_logged(context.user_data):
        reply_keyboard = [['Minhas informações','Meu perfil'],
                          ['Sobre','Logout']]
    
    else:
        reply_keyboard = [['Login','Registrar'],
                      ['Sobre','Finalizar']]
    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
    resposta = "Selecione a opção desejada!"

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=resposta,
        reply_markup=markup
    )



#Retorna as informações dos usuarios
def get_user_info(update, context):
    if utils.is_logged(context.user_data):
        user_data = context.user_data
        resposta = "Nome: "+user_data['user_name']+ "\nEmail: " +  user_data['Email']
        
        context.bot.send_message(chat_id=update.effective_chat.id, text=resposta)

    else:
        unknown(update, context)


def edit_user_info(update, context):
    if utils.is_logged(context.user_data):
        user_data = context.user_data

        resposta = context.user_data
        perfil.requestEdit(update, resposta)        


    else:
        unknown(update, context)





#Cadastra novo user
def signup_handler():
    return ConversationHandler(
            entry_points=[MessageHandler(Filters.text("Registrar"), signup.start)],
            states={
                signup.CHOOSING: [MessageHandler(Filters.regex(Bot.SIGNUP_ENTRY_REGEX),
                                        signup.regular_choice)
                        ],
                signup.TYPING_REPLY: [
                    MessageHandler(Filters.text & ~(Filters.command | Filters.regex('^Done$')),
                                signup.received_information)],
            },
            fallbacks=[MessageHandler(Filters.regex('^Done$'), signup.done),
            MessageHandler(Filters.regex('^Cancelar$'), utils.cancel),
            MessageHandler(Filters.all & ~ Filters.regex('^Done|Cancelar$'), utils.bad_entry)]
            )

#Função de callback do calendário
def birthDayCallBack(update, context):

    result, key, step = CustomCalendar(locale='br', max_date=date.today()).process(update.callback_query.data)
    if not result and key:
        update.callback_query.edit_message_text(f"Selecione o {CustomCalendar.LSTEP[step]}",
                              reply_markup=key)
    elif result:
        
        context.user_data['Nascimento'] = result
        update.callback_query.edit_message_text(f'Selecionado: {result}')
        
        signup.requestSignup(update, context)


def logout(update, context):
    
    if utils.is_logged(context.user_data):
        resposta = f"Já vai?\n\nAté a próxima {context.user_data['user_name']}!"
        
        #Limpa a sessão do usuário
        context.user_data.clear()

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=resposta
        )

        menu(update,context)
    else:
        #Caso não esteja logado, não entra na função de logout
        unknown(update, context)

#Login de usuario
def login_handler():

    return ConversationHandler(
            entry_points=[MessageHandler(Filters.text("Login"), login.start)],
            states={
                login.CHOOSING: [MessageHandler(Filters.regex(Bot.LOGIN_ENTRY_REGEX),
                                        login.regular_choice)
                        ],
                login.TYPING_REPLY: [
                    MessageHandler(Filters.text & ~(Filters.command | Filters.regex('^Done$')),
                                login.received_information)],
            },
            fallbacks=[MessageHandler(Filters.regex('^Done$'), login.done),
            MessageHandler(Filters.regex('^Cancelar$'), utils.cancel),
            MessageHandler(Filters.all & ~ Filters.regex('^Done|Cancelar$'), utils.bad_entry)]
            )

#Login de usuario
def perfil_handler():
    return ConversationHandler(
            entry_points=[MessageHandler(Filters.text("Meu perfil"), perfil.start)],
            states={
                perfil.CHOOSING: [MessageHandler(Filters.regex(Bot.PERFIL_ENTRY_REGER),
                                        perfil.regular_choice)
                        ],
                perfil.TYPING_REPLY: [
                    MessageHandler(Filters.text & ~(Filters.command | Filters.regex('^Done$')),
                                perfil.received_information)],
            },
            fallbacks=[MessageHandler(Filters.regex('^Done$'), perfil.done),
            MessageHandler(Filters.regex('^Voltar$'), utils.cancel),
            MessageHandler(Filters.all & ~ Filters.regex('^Done|Voltar$'), utils.bad_entry)]
            )

#Envia informaçoes sobre o bot
def sobre(update, context):
    resposta = 'O DoctorS é um Telegram Bot criado para ajudar a população no combate ao novo Corona Vírus(SARS-CoV-2).'
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=resposta
    )
    

def finalizar(update, context):
    resposta = "Já vai? Tudo bem, sempre que quiser voltar, digite /menu ou /start e receberá o menu inicial.\n\nObrigado por usar o DoctorS!"
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=resposta
    )


#Mensagens não reconhecidas
def unknown(update, context):
    resposta = "Não entendi. Tem certeza de que digitou corretamente?\n\nRetornando ao menu."
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=resposta,
    )
    menu(update, context)
