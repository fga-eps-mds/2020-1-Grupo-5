import requests, json
from telegram import ReplyKeyboardMarkup, KeyboardButton, Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler, Dispatcher
from src import utils, handlers, getters, bad_report, diario, location, news


# Estados
CHOOSING, TYPING_REPLY = range(2)

required_data = set()


# Inicia o login
def start(update, context):
    
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

    # De acordo com a escolha chama uma função

    if "Localização" in text:

        getters.get_location(update, context)
        return TYPING_REPLY

    else:
        if not text in context.user_data['Symptoms']:
            context.user_data['Symptoms'].append(text)
        elif text in context.user_data['Symptoms']:
            context.user_data['Symptoms'].remove(text)

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
        location.reverseGeo(update.message.location, context)

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

        handlers.menu(update, context)

        return -1 # END

def get_loc(update, context):

    getters.get_location(update, context.user_data)

    return CHOOSING

def bad_entry(update, context):

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Opção inválida, tente utilizar os botões!"
    )

    return CHOOSING

def back(update, context):

    diario.start(update, context)

    return -1 # END
