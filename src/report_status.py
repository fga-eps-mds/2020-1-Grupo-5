from telegram import ReplyKeyboardMarkup
import requests
import json
from src import getters, location, utils
#libraries
import numpy as np
from datetime import datetime


def start(update, context):

    data = get_survey(context.user_data)['surveys']

    # Data inicial
    day_init = (str(data[0]['created_at']).split("T"))[0]
    d1 = datetime.strptime(str(day_init), '%Y-%m-%d')
    d2 = datetime.today()
    tot_days = abs((d2 - d1).days + 1)
    good = 0
    bad = 0

    for survey in data:
        if survey['symptom']:
            bad += 1
        else:
            good += 1

    notResp = abs(tot_days - good - bad)
    
    textSendLegend = imageRel(context.user_data, good, bad, notResp)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=str(textSendLegend)
    )

def get_survey(user_data):

    headers =  {'Accept' : 'application/vnd.api+json', 'Content-Type' : 'application/json', 'Authorization' : str(user_data['AUTH_TOKEN'])}
    url = f"http://localhost:3001/users/{user_data['id']}/surveys"
    r = requests.get(url=url, headers=headers)
    
    surveys = r.json()

    # Log de sucesso ou falha no cadastro
    if r.status_code == 200: # Sucesso
        print("Sucess request get survey")

        return surveys

    else:
        print("Failed to get survey")

def get_percentage(value, allvals):
    absolute = ((value/np.sum(allvals))*100)
    # fazendo legenda do gráfico com % e kg
    return "{:d} dias, {:.1f}%.".format(value, absolute)

def imageRel(user_data, sim, nao, notResp):
    
    data = [sim, nao, notResp]
    colors = ['#66FF66', '#FF6666','#9999FF']
    my_values = []
    legendaText = []
    c = []
    recipe = ['😃 - Você esteve bem ', '🤧 - Você esteve mal ', '\n😞 - Infelizmente você se esqueceu de nós em ']

    cont = 0

    for n in data:
        if not(n == 0):
            legendaText.append(recipe[cont] + get_percentage(n, data))
            my_values.append(data[cont])
            c.append(colors[cont])

        cont += 1

    textSendLegend = 'Olá, ' + user_data['user_name'] + '! Lembre-se sempre de cuidar de sua saúde.\n\n'

    for text in legendaText:
        textSendLegend = textSendLegend + text + '\n'

    return textSendLegend