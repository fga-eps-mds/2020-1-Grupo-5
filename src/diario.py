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
            
            resposta = context.user_data
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


# # Opções de entrada de informação do menu de login
# def regular_choice(update, context):

#     # update.message.text = utils.remove_check_mark(update.message.text)

#     # Adiciona uma chave com o valor de 'Email' ou 'Senha' de acordo com a escolha do user
#     text = update.message.text
#     context.user_data['choice'] = text

#     # De acordo com a escolha chama uma função
#     if "Sim, estou bem." in text:
#         print("Sim regular choice")
#         good_report(update, context)
#         # getters.get_Email(update, context)

#     elif "Não, não estou bem." in text:
#         # getters.get_Pass(update, context)        
#         None
#     # return TYPING_REPLY



# # def good_report(update, context):
# #     update.message.reply_text("Obrigado por nos informar sobre seu estado de saúde.\n\nTenha um bom dia!")


# def good_report(update, context):
    
#     # update.callback_query.edit_message_text("Obrigado por nos informar sobre seu estado de saúde.\n\nTenha um bom dia!")
#     update.message.reply_text("Obrigado por nos informar sobre seu estado de saúde.\n\nTenha um bom dia!")

#     headers =  {'Accept' : 'application/vnd.api+json', 'Content-Type' : 'application/json', 'Authorization' : str(context.user_data['AUTH_TOKEN'])}
    
#     json = {
#         "survey" : {
#             "symptom" : []
#         }
#     }

#     requests.post(url=f'http://localhost:3001/users/{context.user_data["id"]}/surveys', headers=headers, json=json)

#     handlers.menu(update, context)

#     return -1 # END

#     # update.callback_query.edit_message_text(


# def notify_assignees(context):

#     sim = InlineKeyboardButton(text="Sim",callback_data='bad_report')
#     nao = InlineKeyboardButton(text="Não", callback_data='good_report')

#     chat_id=context.job.context

#     # Mensagem teste
#     context.bot.send_message(
#         chat_id=chat_id,
#         text="Sentiu sintomas hoje?",
#         reply_markup=InlineKeyboardMarkup([[sim, nao]], 
#                                         resize_keyboard=True))




# #Mensagens não reconhecidas
# def unknown(update, context):
#     resposta = "Não entendi. Tem certeza de que digitou corretamente?\n\nRetornando ao menu."
#     context.bot.send_message(
#         chat_id=update.effective_chat.id, 
#         text=resposta,
#     )
#     handlers.menu(update, context)


# def daily_report(update, context):
#     if utils.is_logged(context.user_data):
        
#         context.bot.send_message(
#             chat_id=update.effective_chat.id,
#             text="Ativado notificações diárias")
        
#         day_in_sec = 10# Dia em segundos
        
#         # CHAMA DE ACORDO COM UM TEMPO A FUNÇÃO "notify_assignees"
#         context.job_queue.run_repeating(notify_assignees, day_in_sec, context=update.message.chat_id)
    
#     else:
#         unknown(update, context)

# def cancel_daily(update, context):
#     if utils.is_logged(context.user_data):
#         context.bot.send_message(
#             chat_id=update.effective_chat.id,
#             text="Notificações diárias desativadas"
#         )

#         context.job_queue.stop()
#     else:
#         unknown(update, context)
