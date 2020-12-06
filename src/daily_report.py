from src import utils, handlers
from datetime import time, date
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from requests import post
import requests

daily_messages = list()
reported_chat_ids = set()
sim = InlineKeyboardButton(text="Sim",callback_data='bad_report')
nao = InlineKeyboardButton(text="Não", callback_data='good_report')

def daily_report(update, context):
    if utils.is_logged(context.user_data):
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Ativado notificações diárias"
        )
        
        exclude_time = time(hour=18, minute=13, second=59) # 23:59:59
        daily_time = time(hour=18, minute=12, second=0) # 12:00:00

        context.job_queue.run_daily(callback=notify_assignees, time=daily_time, context=update.effective_chat.id)
        context.job_queue.run_daily(callback=delete_daily, time=exclude_time, context=update.effective_chat.id)
    else:
        handlers.unknown(update, context)

def delete_daily(context):
    reported_chat_ids.clear()
    for message in daily_messages:
        try:
            context.bot.delete_message(chat_id=context.job.context ,message_id=message)
            daily_messages.remove(message)
            return
        except:
            pass

def cancel_daily(update, context):
    if utils.is_logged(context.user_data):
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Notificações diárias desativadas"
        )
        context.job_queue.stop()
    else:
        handlers.unknown(update, context)

def report_requested(update, context):
    if utils.is_logged(context.user_data):
        update.message.reply_text(
            text="Sentiu sintomas hoje?",
            reply_markup=InlineKeyboardMarkup([[sim, nao]], resize_keyboard=True)
        )
    else:
        update.message.reply_text("Por favor, faça login ou cadastre-se para relatar o seu estado de saúde.")

def notify_assignees(context):
    chat_id=context.job.context

    if chat_id in reported_chat_ids:
        print('user has already reported today')
        return

    # Mensagem teste
    message = context.bot.send_message(
        chat_id=chat_id,
        text="Sentiu sintomas hoje?",
        reply_markup=InlineKeyboardMarkup([[sim, nao]], resize_keyboard=True)
    )
    
    daily_messages.append(message['message_id'])

def good_report(update, context):
    update.callback_query.answer()
    headers =  {'Accept' : 'application/vnd.api+json', 'Content-Type' : 'application/json', 'Authorization' : str(context.user_data['AUTH_TOKEN'])}   
    json = {
        "survey" : {
            "symptom" : []
        }
    }
    r = post(url=f'http://localhost:3001/users/{context.user_data["id"]}/surveys', headers=headers, json=json)
    if r.status_code == 201:
        update.callback_query.edit_message_text("Obrigado por nos informar sobre seu estado de saúde.\n\nTenha um bom dia!")
    else:
        update.callback_query.edit_message_text("Algo deu errado. Lembre-se que só pode reportar seu estado de saúde uma vez por dia.")

    reported_chat_ids.add(update.effective_chat.id)
