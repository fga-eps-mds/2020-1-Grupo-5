from telegram import ReplyKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler)
import requests
from src import signup, login, Bot, utils
from src.CustomCalendar import CustomCalendar
from datetime import date
import time



#Envia o menu para o usuario
def start(update, context):

    if utils.is_logged(context.user_data):
        reply_keyboard = [['Minhas informações','Sobre'],
                          ['Sobre','Logout'],
                          ['Ajuda']]
    
    else:
        reply_keyboard = [['Login','Registrar'],
                      ['Sobre','Finalizar'],
                      ['Ajuda']]

    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)

    resposta = ("Bem vindo ao DoctorS Bot, selecione a opção desejada.\n\n"
                "Caso deseje voltar ao menu, digite /menu ou /start.\n")

    context.bot.send_message(
        chat_id=update.effective_chat.id, text=resposta, reply_markup=markup
    )

def menu(update, context):
    if utils.is_logged(context.user_data):
        reply_keyboard = [['Minhas informações','Sobre'],
                          ['Sobre','Logout'],
						  ['Ajuda']]
    
    else:
        reply_keyboard = [['Login','Registrar'],
                      ['Sobre','Finalizar'],
						 ['Ajuda']]

    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
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
        resposta = f"Já vai?\n\nAté a próxima {context.user_data['Username']}!"
        
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

#Envia informaçoes sobre o bot
def sobre(update, context):
    resposta = 'O DoctorS é um Telegram Bot criado para ajudar a população no combate ao novo Corona Vírus(SARS-CoV-2).'
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=resposta
    )
    
#Informações sobre as funcionalidades
def ajuda(update, context):
	#Lista de funcionalidades
    resposta = 'O DoctorS possui as seguintes funcionalidades:\n\n - Cadastro: Crie uma nova conta de usuário\n\n - Login: Entre em sua conta, caso você ainda não possua uma, use a função de cadastro\n\n - Logout: Saia de sua conta\n\n - Reportar estado físico: Informe seu estado de saúde, recomendado uso diário\n\n - Alterar informações pessoais: Altere as informações da sua conta'
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=resposta
    )
    resposta = ('Informações gerais:\n\n'
                '-Para navegar nos menus clique em algum dos botões de navegação. Se o teclado de sugestões desaparecer basta clicar no ícone de teclado ao lado do campo de digitação.\n\n'
                '- Nos menus de cadastro e login, quando uma informação válida for inserida, aparecerá no botão correspondente uma marca indicando que ela foi validada.\n\n'
                '- Quando todas as informações forem inseridas aparecerá um botão "Done". Clique nele para prosseguir com o cadastro ou login.\n\n'
                '- Para apagar os dados inseridos e retornar ao menu anterior utilize o botão cancelar caso esteja disponível.\n\n'
    )
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=resposta
    )
	#Mais informações
    resposta = 'Para informações mais detalhadas acesse: {inserir link aqui}'
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
