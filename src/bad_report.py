from telegram import ReplyKeyboardMarkup
import requests
import json
from src import getters

CHOOSING, SEND_LOC = range(2)

sintomas = ["Dor de Cabeça"]

def get_symptoms(update, context):
    headers = {'Accept' : 'application/vnd.api+json', 'Content-Type' : 'application/json', 'Authorization' : str(context.user_data['AUTH_TOKEN'])}

    r = requests.get(url="http://localhost:3001/symptoms", headers=headers)

    symptoms = json.loads(r.content)['symptoms']
    
    for symptom in symptoms:
        sintomas.append(symptom)

markup = ReplyKeyboardMarkup([['Dor de Cabeça'],
                               ['Done']],
        resize_keyboard=True,
        one_time_keyboard=True)

def start(update, context):
    context.user_data['Symptoms'] = list()

    update.callback_query.edit_message_text(
        "Obrigado por nos informar!"
        )

    context.bot.send_message(
        text='Selecione os sintomas que sentiu nas últimas 24 horas!',
        chat_id=update.effective_chat.id,
        reply_markup=markup
    )

    return CHOOSING

def get_loc(update, context):
    getters.get_location(update, context)

    return CHOOSING


def regular_choice(update, context):


    if update.message.text:
        context.user_data['Symptoms'].append(update.message.text)


    else:
        local = update.message.location
        context.user_data['latitude'] = local.latitude
        context.user_data['longitude'] = local.longitude
    
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{context.user_data['Symptoms']}, selecione mais sintomas abaixo.",
        reply_markup=markup
    )

    return CHOOSING


def done(update, context):


    headers =  {'Accept' : 'application/vnd.api+json', 'Content-Type' : 'application/json', 'Authorization' : str(context.user_data['AUTH_TOKEN'])}

    json_entry = {
        "survey" : {
                "latitute" : context.user_data['latitude'],
                "longitude": context.user_data['longitude'],
                "symptom": context.user_data['Symptoms']
        }
    }

    url = f"http://localhost:3001/users/{context.user_data['id']}/surveys"

    req = requests.post(headers=headers, json=json_entry, url=url)

    if req.status_code == 200:
        print('Bad report feito')

    else:
        print(req)

    return -1 # END

def cancel(update, context):
    print("Voltar")

    return -1 # END

def bad_entry(update, context):
    print('Bad_entry')
    
    return -1 # END