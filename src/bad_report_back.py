from telegram import ReplyKeyboardMarkup
import requests
import json
from src import getters, diario, location, utils

CHOOSING, TYPING_REPLY = range(2)
required_data = set()

sintomas = diario.sintomas

# markup = ReplyKeyboardMarkup(   sintomas,
#                                 resize_keyboard=True,
#                                 one_time_keyboard=True)

#Inicia a area de report
def start(update, context):

    print("\nBad report start context: ", context.user_data)

    context.user_data['Symptoms'] = list()

    update.callback_query.edit_message_text(
        "Obrigado por nos informar!"
        )

    user_data = context.user_data

    user_data['Keyboard'] = sintomas

    markup = ReplyKeyboardMarkup(user_data['Keyboard'], one_time_keyboard=True, resize_keyboard=True)

    context.bot.send_message(
        text='Selecione os sintomas que sentiu nas últimas 24 horas!',
        chat_id=update.effective_chat.id,
        reply_markup=markup
    )

    # markup = ReplyKeyboardMarkup(sintomas, one_time_keyboard=True, resize_keyboard=True)
    # update.message.reply_text(
    #     "Selecione os sintomas que sentiu nas últimas 24 horas!",
    #     reply_markup=markup)



    return CHOOSING



def regular_choice(update, context):

    text = update.message.text
    context.user_data['choice'] = text
    print("Regular choice: ", context.user_data)
    
    print("Regular choice text: ", text)

    if text == 'Prosseguir':

        getters.get_location(update, context)

        return TYPING_REPLY

    else:
        context.user_data['Symptoms'].append(text)
        print("Entrou no if do regu")
        return TYPING_REPLY

    # return TYPING_REPLY

def received_information(update, context):
    print("Received information: ", context.user_data)

    category = update_received_information(context, update)
    head = validation_management(context.user_data, category)
    update_missing_info(context.user_data)

    feedback = head + "{}\n\nVocê pode me dizer os outros dados ou alterar os já inseridos.\n\n".format(utils.dict_to_str(context.user_data))

    if len(required_data) > 0:
        feedback = feedback + "Ainda falta(m):\n{}".format(utils.set_to_str(required_data))
    utils.received_information_reply(update, context, feedback)


    # head = validation_management(context.user_data, category)
    # footer = update_missing_info(context.user_data)

    # feedback = head + "{}".format(utils.dict_to_str(context.user_data)) + footer

    # Se as informações estiverem completas essa estrutura não é adicionada
    # if len(required_data) > 0:
    #     feedback = feedback + "Ainda falta(m):\n{}".format(utils.set_to_str(required_data))

    # utils.received_information_reply(update, context, feedback)

    print("RECEIVED INFORMATION: ", category)


    return CHOOSING

def update_received_information(context, update):
    # Adiciona a informação enviada pelo user à sua respectiva chave
    category = context.user_data['choice']
    del context.user_data['choice']

    if 'Localização' in category or 'Prosseguir' in category:
        print("Update in localization: ", category)
        location.reverseGeo(update.message.location, context)
    else:
        context.user_data[category] = update.message.text

    return category

def validation_management(user_data, category):
    # Validação de dados
    validation = utils.validations_login(user_data)

    utils.update_check_mark( user_data['Keyboard'], category, validation)

    if validation:
        return "Perfeito, entrada aceita\n"
    else:
        return "Entrada inválida. Tem certeza que digitou corretamente?\n"

def update_missing_info(user_data):
    # Estrutura que mostra as informações que ainda faltam ser inseridas
    utils.update_required_data(user_data, required_data)
    utils.unreceived_info(user_data, required_data, {'Dor de Cabeça', 'Prosseguir', 'Voltar'})

    # Caso todas as informações tenham sido adicionadas
    if len(required_data) == 0:
        utils.form_filled(user_data['Keyboard'])
    elif ['Done'] in user_data['Keyboard']:
        utils.undone_keyboard(user_data['Keyboard'])



def next(update, context):




    return 







def get_symptoms(update, context):

    headers = {'Accept' : 'application/vnd.api+json', 'Content-Type' : 'application/json', 'Authorization' : str(context.user_data['AUTH_TOKEN'])}

    r = requests.get(url="http://localhost:3001/symptoms", headers=headers)

    symptoms = json.loads(r.content)['symptoms']

    print("\nBad report symptoms context: ", context.user_data)

    print("Get symptoms: ", symptoms)

    for symptom in symptoms:
        sintomas.append(symptom)





def get_loc(update, context):
    print("\nGet loc context: ", context.user_data)
    getters.get_location(update, context.user_data)
    # print("\nGet loc context: ", )
    return CHOOSING






def done(update, context):


    headers =  {'Accept' : 'application/vnd.api+json', 'Content-Type' : 'application/json', 'Authorization' : str(context.user_data['AUTH_TOKEN'])}

    print("Bad report context surveys: ", context.user_data)


    json_entry = {
        "survey" : {
                "latitute" : context.user_data['latitude'],
                "longitude": context.user_data['longitude'],
                "symptom": context.user_data['Symptoms']
        }
    }

    url = f"http://localhost:3001/users/{context.user_data['id']}/surveys"

    req = requests.post(headers=headers, json=json_entry, url=url)

    print("Bad report surveys: ", req)

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