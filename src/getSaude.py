from telegram import ReplyKeyboardMarkup
import requests
import json
from src import getters, diario, location, utils
#libraries
import matplotlib as matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import squarify # pip install squarify (algorithm for treemap)&lt;/pre&gt;
from datetime import datetime


def start(update, context):

    data = get_survey(update, context)['surveys']


    print("\n")
    print("Data survey: ", data)
    print("\n")

    # Data inicial
    day_init = (str(data[0]['created_at']).split("T"))[0]
    d1 = datetime.strptime(str(day_init), '%Y-%m-%d')
    d2 = datetime.today()
    tot_days = abs((d2 - d1).days + 1)

    print("tot_days: ", tot_days)

    print("Day: ", day_init)

    # x = map(interable_function_surveys, data)

    good = 0
    bad = 0

    for survey in data:
        if survey['symptom']:
            bad += 1
        else:
            good += 1

    notResp = abs(tot_days - good - bad)
    
    textSendLegend = imageRel(update, context, good, bad, notResp)



    path = 'general/images/relGraf.png'
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open( path, 'rb'))
   
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=str(textSendLegend)
    )

# def interable_function_surveys(list_surveys):

#     print("Interable:")
#     print("Survey interable status: ", list_surveys)




def get_symptoms(update, context):

    headers = {'Accept' : 'application/vnd.api+json', 'Content-Type' : 'application/json', 'Authorization' : str(context.user_data['AUTH_TOKEN'])}

    r = requests.get(url="http://localhost:3001/symptoms", headers=headers)

    symptoms = json.loads(r.content)['symptoms']

    print("\nBad report symptoms context: ", context.user_data)

    print("Get symptoms r: ", r)
    print("Get symptoms: ", symptoms)

    # for symptom in symptoms:
    #     sintomas.append(symptom)



def get_survey(update, context):

    headers =  {'Accept' : 'application/vnd.api+json', 'Content-Type' : 'application/json', 'Authorization' : str(context.user_data['AUTH_TOKEN'])}

    url = f"http://localhost:3001/users/{context.user_data['id']}/surveys"

    r = requests.get(url=url, headers=headers)
    # r = requests.head(url=url, headers=headers)

    print("r: ", r)

    # surveys = json.loads(r.content)
    surveys = r.json()

    # context.user_data['AUTH_TOKEN'] = r.headers['Authorization']

    print("\nSurvey: ", surveys)

    # Log de sucesso ou falha no cadastro
    if r.status_code == 200: # Sucesso
        # surveys = json.loads(r.content)['surveys'] # Pega os dados do usuário logado
        print("Survey status code: ", surveys)
        if surveys['surveys']:
            if surveys['surveys'][0]:
                print("Survey status code: ", surveys['surveys'][0])
                print("Survey status code: ", surveys['surveys'][0]['id'])

                print("size Survey status code: ", len(surveys['surveys']))

    get_survey_week(update, context)

    return surveys
    # requests.post(headers=headers, json=json_entry, url=url)

def verif_status_report(update, context):

    data = get_survey(update, context)['surveys']

    for survey in data:

        day_init = (str(survey['created_at'])).split("T")
        print("Day init: ", day_init[0])
        d1 = datetime.strptime(str(day_init[0]), '%Y-%m-%d')
        d2 = datetime.today()
        if str(day_init[0]) in str(d2):


            print("Day d1: ", d1)
            print("Day d2: ", d2)

        # if d1 == d2:

            print("Já foi reportado!")
            return True
    
    return False

def get_survey_week(update, context):

    headers =  {'Accept' : 'application/vnd.api+json', 'Authorization' : str(context.user_data['AUTH_TOKEN'])}

    url = f"http://localhost:3001/users/{context.user_data['id']}/surveys/"

    r = requests.get(url=url, headers=headers)
    # r = requests.head(url=url, headers=headers)

    print("\n week r: ", r)

    # surveys = json.loads(r.content)
    surveys = r.json()

    # context.user_data['AUTH_TOKEN'] = r.headers['Authorization']

    print("Survey week: ", surveys)

    # Log de sucesso ou falha no cadastro
    if r.status_code == 200: # Sucesso
        # surveys = json.loads(r.content)['surveys'] # Pega os dados do usuário logado
        print("Survey status code week: ", surveys)




def func(value, allvals):
    absolute = ((value/np.sum(allvals))*100)
    # fazendo legenda do gráfico com % e kg
    return "{:d} dias, {:.1f}%.".format(value, absolute)

def imageRel(update, context, sim, nao, notResp):
    

    data = [sim, nao, notResp]
    colors = ['#66FF66', '#FF6666','#9999FF']
    my_values = []
    legendaText = []
    c = []
    # recipe = [' Você esteve bem ', '❌ Você esteve mal ', '\n- Infelizmente você se esqueceu de nós em ']
    recipe = ['😃 - Você esteve bem ', '🤧 - Você esteve mal ', '\n😞 - Infelizmente você se esqueceu de nós em ']

    cont = 0

    for n in data:
        if not(n == 0):
            legendaText.append(recipe[cont] + func(n, data))
            my_values.append(data[cont])
            c.append(colors[cont])

        cont += 1

    squarify.plot(sizes=my_values, alpha=.80, color=c,pad=True, text_kwargs=dict(fontsize=9, color="#5c2f33"))

    print("Legenda: ", legendaText)
    # plt.gca().legend(legendaText)

    print("Name: ", context.user_data['user_name'])
    # legendaText = "Olá, " + str(context.user_data['user_name']) + '!\n' + legendaText

    textSendLegend = 'Olá, ' + context.user_data['user_name'] + '! Lembre-se sempre de cuidar de sua saúde.\n\n'

    for text in legendaText:
        textSendLegend = textSendLegend + text + '\n'



    # Removendo os eixos
    plt.axis('off')

    # Ajustando o gráfico
    plt.tight_layout()
    fig = plt.gcf()
    # plt.show()
    fig.savefig('general/images/relGraf.png', transparent = True)
    plt.close()

    return textSendLegend