import requests, json
from telegram import ReplyKeyboardMarkup, KeyboardButton, Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler, Dispatcher
from src import utils, handlers, getters, bad_report, diario, location, news


# Estados
CHOOSING, TYPING_REPLY = range(2)
# sintomas = diario.sintomas

required_data = set()


# Inicia o login
def start(update, context):
    
    print("\nBad report start context: ", context.user_data)

    context.user_data['Symptoms'] = list()
    user_data = context.user_data

    user_data['Keyboard']   =   [['Dor de cabeça', 'Bolhas na Pele', 'Mal-estar'],
                                ['Bolhas na Pele', 'Congestão Nasal', 'Náuseas'],
                                ['Diarréia', 'Dificuldade de respirar', 'Olhos vermelhos'],
                                ['Dor nas Articulações', 'Febre', 'Tosse'],
                                ['Dor no Estômago', 'Dor nos Músculos', 'Sangramentos'],
                                ['Dor nos Olhos', 'Calafrios', 'Vômito'],
                                ['Pele e olhos avermelhados', 'Manchas vermelhas no corpo'],
                                ['Localização','Voltar', 'Done']]

    markup = ReplyKeyboardMarkup(user_data['Keyboard'], one_time_keyboard=True, resize_keyboard=True)

    context.bot.send_message(
        text='Selecione os sintomas que sentiu nas últimas 24 horas!',
        chat_id=update.effective_chat.id,
        reply_markup=markup
    )

    return CHOOSING


# Opções de entrada de informação do menu de login
def regular_choice(update, context):

    update.message.text = utils.remove_check_mark(update.message.text)

    # Adiciona uma chave com o valor de 'Email' ou 'Senha' de acordo com a escolha do user
    text = update.message.text


    context.user_data['choice'] = text

    print("Regular choice: ", context.user_data)
    print("Regular choice text: ", text)

    # De acordo com a escolha chama uma função

    if "Localização" in text:

        getters.get_location(update, context)
        return TYPING_REPLY

    else:
        if not text in context.user_data['Symptoms']:
            context.user_data['Symptoms'].append(text)
        elif text in context.user_data['Symptoms']:
            context.user_data['Symptoms'].remove(text)

        print("Entrou no if do regu")
        category = update_received_information(context, update)
        head = validation_management(context.user_data, category)
        update_missing_info(context.user_data)

        feedback = head + "{}\n\nVocê pode me dizer os outros dados ou alterar os já inseridos.\n\n".format(utils.dict_to_str(context.user_data))
        if len(required_data) > 0:
            feedback = feedback + "Ainda falta(m):\n{}".format(utils.set_to_str(required_data))
        utils.received_information_reply(update, context, feedback)


        return CHOOSING   

    return TYPING_REPLY


# Envia as informações atualmente recebidas do usuário
def received_information(update, context):

    category = update_received_information(context, update)
    head = validation_management(context.user_data, category)
    update_missing_info(context.user_data)

    feedback = head + "{}\n\nVocê pode me dizer os outros dados ou alterar os já inseridos.\n\n".format(utils.dict_to_str(context.user_data))
    if len(required_data) > 0:
        feedback = feedback + "Ainda falta(m):\n{}".format(utils.set_to_str(required_data))
    utils.received_information_reply(update, context, feedback)

    return CHOOSING

def update_received_information(context, update):
    # Adiciona a informação enviada pelo user à sua respectiva chave
    category = context.user_data['choice']
    del context.user_data['choice']

    if 'Localização' in category or 'Prosseguir' in category:
        context.user_data['longitude'] = update.message.location.longitude
        context.user_data['latitude'] = update.message.location.latitude

        print("Update in localization: ", category)
        location.reverseGeo(update.message.location, context)
    # else:
    #     context.user_data[category] = update.message.text

    return category


def validation_management(user_data, category):
    # Validação de dados
    validation = utils.validations_login(user_data)

    utils.update_check_mark_report(user_data['Keyboard'], category, validation)

    if validation:
        return "Perfeito, entrada aceita\n"
    else:
        return "Entrada inválida. Tem certeza que digitou corretamente?\n"


def update_missing_info(user_data):
    # Estrutura que mostra as informações que ainda faltam ser inseridas
    utils.update_required_data(user_data, required_data)
    utils.unreceived_info(user_data, required_data, {'Email', 'Senha'})

    # Caso todas as informações tenham sido adicionadas
    if len(required_data) == 0:
        utils.form_filled(user_data['Keyboard'])
    elif ['Done'] in user_data['Keyboard']:
        utils.undone_keyboard(user_data['Keyboard'])
    
def done(update, context):
    keyboard = context.user_data['Keyboard']

    print("Keyboard:", keyboard[7])

    markup = ReplyKeyboardMarkup(context.user_data['Keyboard'], one_time_keyboard=True, resize_keyboard=True)

    if not 'Localização✅' in keyboard[7]:

        context.bot.send_message(    
            chat_id=update.effective_chat.id,
            text="Por favor envie sua localização antes de prosseguir!",
            reply_markup=markup

        )
        return CHOOSING
    elif not context.user_data['Symptoms']:
        
        context.bot.send_message(    
            chat_id=update.effective_chat.id,
            text="Selecione ao menos um sintoma, ou volte para sinalizar que está bem.",
            reply_markup=markup

        )
        return CHOOSING  
    
    else:
        headers =  {'Accept' : 'application/vnd.api+json', 'Content-Type' : 'application/json', 'Authorization' : str(context.user_data['AUTH_TOKEN'])}
        print("Bad report context surveys: ", context.user_data)

        json_entry = {
            "survey" : {
                    "symptom": context.user_data['Symptoms'],
                    "latitude": context.user_data['latitude'],
                    "longitude": context.user_data['longitude'],
            }
        }

        url = f"http://localhost:3001/users/{context.user_data['id']}/surveys"

        requests.post(headers=headers, json=json_entry, url=url)

        resposta = "Obrigado por nos informar o seu estado de saúde.\n\nEsperamos que tudo fique bem, mantenha-se sempre hidratado e isolado.\n\nImportante lembrar que caso precise de alguma ajuda, temos o botão de ajuda no menu abaixo."
        
        context.bot.send_message(
            chat_id= update.effective_chat.id,
            text = resposta
        )

        context.user_data.pop('Symptoms', None)

        # news.run(update, context)
        handlers.menu(update, context)

        return -1 # END

def get_loc(update, context):
    print("\nGet loc context: ", context.user_data)
    getters.get_location(update, context.user_data)
    # print("\nGet loc context: ", )
    return CHOOSING


# def bad_entry(update, context):
#     print('Bad_entry')
    
#     return -1 # END

def bad_entry(update, context):

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Opção inválida, tente utilizar os botões!"
    )
    # context.user_data.clear()

    # handlers.menu(update, context)

    return CHOOSING




def back(update, context):
    print("Voltar")
    diario.start(update, context)
    return -1 # END













# def done(update, context):


#     headers =  {'Accept' : 'application/vnd.api+json', 'Content-Type' : 'application/json', 'Authorization' : str(context.user_data['AUTH_TOKEN'])}

#     print("Bad report context surveys: ", context.user_data)


#     json_entry = {
#         "survey" : {
#                 "latitute" : context.user_data['latitude'],
#                 "longitude": context.user_data['longitude'],
#                 "symptom": context.user_data['Symptoms']
#         }
#     }

#     url = f"http://localhost:3001/users/{context.user_data['id']}/surveys"

#     req = requests.post(headers=headers, json=json_entry, url=url)

#     print("Bad report surveys: ", req)

#     if req.status_code == 200:
#         print('Bad report feito')

#     else:
#         print(req)

#     return -1 # END







# def get_symptoms(update, context):

#     headers = {'Accept' : 'application/vnd.api+json', 'Content-Type' : 'application/json', 'Authorization' : str(context.user_data['AUTH_TOKEN'])}

#     r = requests.get(url="http://localhost:3001/symptoms", headers=headers)

#     symptoms = json.loads(r.content)['symptoms']

#     print("\nBad report symptoms context: ", context.user_data)

#     print("Get symptoms: ", symptoms)

#     for symptom in symptoms:
#         sintomas.append(symptom)




# def update_received_information(user_data, text):
#     # Adiciona a informação enviada pelo user à sua respectiva chave
#     category = user_data['choice']
#     del user_data['choice']
#     # user_data[category] = text

#     return category
