import requests, json
from telegram import ReplyKeyboardMarkup, KeyboardButton, Update, Bot
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler, CallbackQueryHandler, Dispatcher)
from src import utils, handlers

#States
CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

#Teclado de entradas do Login
reply_keyboard = [['Email', 'Senha']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
required_data = set()

#Inicia o login
def start(update, context):
    
    if utils.is_logged(context.user_data):
        handlers.unknown(update, context)
        return ConversationHandler.END
    
    else:
        #Mensagem de inicio do login
        update.message.reply_text(
            "Faça login enviando suas informações:",
            reply_markup=markup)

        return CHOOSING

#Opçoes de entrada de informação do menu de login
def regular_choice(update, context):
 
    #Pega as informações adcionadas 
    user_data = context.user_data

    #Adciona uma chave com o valor de 'Email' ou 'Senha' de acordo com a escolha do user
    text = update.message.text
    user_data['choice'] = text

    #De acordo com a escolha, chama uma função
    if "Email" in text:
        get_Email(update, context)

    if "Senha" in text:
        get_Pass(update, context)

    return TYPING_REPLY

#Função que adciona done ao terminar de adcionar todas informações
def form_filled():
    if not ['Done'] in reply_keyboard:
        reply_keyboard.append(['Done'])
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)


#Caso a pessoa tenha adcionado todas as informações e 
#Depois adcionou uma inválida novamente, ele retira o
#Botão de done
def undone_keyboard():
    reply_keyboard.remove(['Done'])
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)


#Send current received information from user
def received_information(update, context):

    #Get data of user
    user_data = context.user_data
    text = update.message.text

    #Adciona a informação enviada pelo user à sua respectiva chave
    category = user_data['choice']
    user_data[category] = text
    
    del user_data['choice']
       
    #Validação de dados
    validation = utils.validations_login(user_data)

    if not validation:
        head = "Entrada inválida, tem certeza que digitou corretamente?\n"

    else:
        head = "Perfeito, entrada aceita\n"

    #Estrutura que mostra informações que ainda faltam ser inseridas
    if len(user_data) > 0:
        for key in user_data:
            if key in required_data:
                required_data.remove(key)

    unreceived_info(context)

    #Caso todas informações tenham sido adcionadas, 
    if len(required_data) == 0:
        form_filled()

    else:
        if ['Done'] in reply_keyboard:
            undone_keyboard()
    
    #Envia o feedback ao user
    update.message.reply_text(  head + 
                                "{} Você pode me dizer os outros dados ou alterar os"
                                " já inseridos.\n\n".format(utils.dict_to_str(user_data)), reply_markup=markup)

    #Se as informações  estiverem completas, essa estrutura não é enviada
    if len(required_data) > 0:
        update.message.reply_text("Ainda falta(m):\n"
                                  "{}".format(utils.set_to_str(required_data)))

    return CHOOSING


def unreceived_info(context):
    all_items = {'Email', 'Senha'}
    for item in all_items:
        if not item in context.user_data:
            required_data.add(item)


#Funcao que recebe a senha do user
def get_Pass(update, context):
    text = update.message.text
    context.user_data['choice'] = text
    update.message.reply_text(
        'Digite uma senha valida, com pelo menos 8 caracteres!'
    )

    return TYPING_REPLY


#Funcao que recebe a senha do user
def get_Email(update, context):
    text = update.message.text
    context.user_data['choice'] = text
    update.message.reply_text(
        'Digite um email valido!'
    )

    return TYPING_REPLY


#Termina o login e envia ao servidor da API do guardiões
def done(update, context):

    #Estrutura necessária para não permitir a finalização incorreta de um login
    #Caso o usario tenha adcionado todas as infos, ele aceita a entrada
    if len(context.user_data) == 2:
        reply_keyboard.remove(['Done'])
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
             
        request_login(update, context)

    else:   
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Falha ao fazer login, não adcionou todos dados necessários!"
        )

        return ConversationHandler.END

    
#Função que executa a request de login
def request_login(update, context):

    json_entry = {
        "user" : {
            "email" : context.user_data.get('Email'),
            "password" : context.user_data.get('Senha')
        }
    }

    headers = {'Accept' : 'application/vnd.api+json', 'Content-Type' : 'application/json'}


    #Faz a tentativa de cadastro utilizando o json e os headers inseridos
    r = requests.post("http://127.0.0.1:3001/user/login", json=json_entry, headers=headers)
    
    #Log de sucesso ou falha no cadastro
    if r.status_code == 200: # Sucesso

        user = json.loads(r.content)['user'] # Pega os dados do usuario logado

        #Token de autorização de sessão
        context.user_data['AUTH_TOKEN'] = r.headers['Authorization']

        context.user_data['Username'] = user['user_name']

        context.user_data['user_id'] = user['id']

        del context.user_data['Senha']

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"{context.user_data['Username']} seja bem vindo(a) ao DoctorS Bot, o chat bot integrado ao Guardiões da Saúde."
        )
    
    else: #Falha
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Seu login falhou!\n\nTem certeza que digitou os dados corretamente?"
        )

    #Chama o menu novamente
    handlers.menu(update, context)

    return ConversationHandler.END