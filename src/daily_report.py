from src import utils, handlers
from datetime import time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from requests import post

daily_messages = list()

def daily_report(update, context):
    if utils.is_logged(context.user_data):
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Ativado notificações diárias"
        )
        
        exclude_time = time(hour=2, minute=59, second=59) # 23:59:59
        daily_time = time(hour=15, minute=0, second=0) # 12:00:00

        context.job_queue.run_daily(callback=notify_assignees, time=daily_time, context=update.effective_chat.id)
        context.job_queue.run_daily(callback=delete_daily, time=exclude_time, context=update.effective_chat.id)
    else:
        handlers.unknown(update, context)

def delete_daily(context):
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

def notify_assignees(context):
    sim = InlineKeyboardButton(text="Sim",callback_data='bad_report')
    nao = InlineKeyboardButton(text="Não", callback_data='good_report')

    chat_id=context.job.context

    # Mensagem teste
    message = context.bot.send_message(
        chat_id=chat_id,
        text="Sentiu sintomas hoje?",
        reply_markup=InlineKeyboardMarkup([[sim, nao]], resize_keyboard=True)
    )
    
    daily_messages.append(message['message_id'])

def good_report(update, context):
    update.callback_query.edit_message_text("Obrigado por nos informar sobre seu estado de saúde.\n\nTenha um bom dia!")

    headers =  {'Accept' : 'application/vnd.api+json', 'Content-Type' : 'application/json', 'Authorization' : str(context.user_data['AUTH_TOKEN'])}   
    json = {
        "survey" : {
            "symptom" : []
        }
    }
    post(url=f'http://localhost:3001/users/{context.user_data["id"]}/surveys', headers=headers, json=json)
