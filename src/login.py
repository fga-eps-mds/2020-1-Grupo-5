import requests, json
from telegram import ReplyKeyboardMarkup, KeyboardButton, Update, Bot
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler, CallbackQueryHandler, Dispatcher)
from src import utils, handlers, getters, news
import _thread as thread

# Estados
CHOOSING, TYPING_REPLY = range(2)

required_data = set()


# Inicia o login
def start(update, context):
    user_data = context.user_data
    user_data['Keyboard'] = [['Email', 'Senha'],
                            ['Cancelar']]

    if utils.is_logged(user_data):
        handlers.unknown(update, context)
        return ConversationHandler.END
    else:
        # Mensagem de início do login
        markup = ReplyKeyboardMarkup(user_data['Keyboard'], one_time_keyboard=True, resize_keyboard=True)
        update.message.reply_text(
            "Faça login enviando suas informações!\n\n"
            "Selecione o botão que desejar e informe o dado selecionado.",
            reply_markup=markup)

        return CHOOSING


# Opções de entrada de informação do menu de login
def regular_choice(update, context):

    update.message.text = utils.remove_check_mark(update.message.text)

    # Adiciona uma chave com o valor de 'Email' ou 'Senha' de acordo com a escolha do user
    text = update.message.text
    context.user_data['choice'] = text

    # De acordo com a escolha chama uma função
    if "Email" in text:
        getters.get_Email(update, context)

    elif "Senha" in text:
        getters.get_Pass(update, context)        

    return TYPING_REPLY


# Envia as informações atualmente recebidas do usuário
def received_information(update, context):

    category = update_received_information(context.user_data, update.message.text)
    head = validation_management(context.user_data, category)
    update_missing_info(context.user_data)

    feedback = head + "{}\n\nVocê pode me dizer os outros dados ou alterar os já inseridos.\n\n".format(utils.dict_to_str(context.user_data))
    if len(required_data) > 0:
        feedback = feedback + "Ainda falta(m):\n{}".format(utils.set_to_str(required_data))
    utils.received_information_reply(update, context, feedback)

    return CHOOSING


def update_received_information(user_data, text):
    # Adiciona a informação enviada pelo user à sua respectiva chave
    category = user_data['choice']
    del user_data['choice']
    user_data[category] = text

    return category


def validation_management(user_data, category):
    # Validação de dados
    validation = utils.validations_login(user_data)

    utils.update_check_mark(user_data['Keyboard'], category, validation)

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


#Termina o login e envia ao servidor da API do guardiões
def done(update, context):

    # Estrutura necessária para não permitir a finalização incorreta de um login
    # Caso o usuário tenha adicionado todas as infos, ele aceita a entrada
    # 3, pois devem existir 2 informações do usuário + teclado
    if len(context.user_data) == 3: # Login + Email enviados
        context.user_data['Keyboard'].remove(['Done'])
             
        request_login(update, context)

    else:   
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Falha ao fazer login, não adicionou todos os dados necessários!"
        )
    
    return ConversationHandler.END

    
# Função que executa a request de login
def request_login(update, context):

    json_entry = {
        "user" : {
            "email" : context.user_data.get('Email'),
            "password" : context.user_data.get('Senha')
        }
    }

    headers = {'Accept' : 'application/vnd.api+json', 'Content-Type' : 'application/json'}


    # Faz a tentativa de cadastro utilizando o json e os headers inseridos
    r = requests.post("http://127.0.0.1:3001/user/login", json=json_entry, headers=headers)
    

    # Log de sucesso ou falha no cadastro
    if r.status_code == 200: # Sucesso
        user = json.loads(r.content)['user'] # Pega os dados do usuário logado

        context.user_data.clear()

        context.user_data.update(user)
        
        del context.user_data['app']
        # Token de autorização de sessão
        context.user_data['AUTH_TOKEN'] = r.headers['Authorization']

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"{context.user_data['user_name']} seja bem vindo(a) ao DoctorS Bot, o chatbot integrado ao Guardiões da Saúde."
        )

        link = "https://scontent-gig2-1.xx.fbcdn.net/v/t1.0-9/103274216_112293347182974_7934951402525681679_o.png?_nc_cat=101&ccb=2&_nc_sid=85a577&_nc_ohc=DfmCZ9ndG5cAX-Mq4qP&_nc_ht=scontent-gig2-1.xx&oh=0566da2b649761aa3348d1f8c89c640a&oe=5FBA8F35"
        # context.bot.send_photo(chat_id=chat_id, photo=open('tests/test.png', 'rb'))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=link)

    else: # Falha
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Seu login falhou!\n\nTem certeza que digitou os dados corretamente?"
        )

# ____________________________

    # a = news.Th(1)
    # a.run(update, context) 
    thread.start_new_thread(news.run, (update, context))
# ____________________________


    #Chama o menu novamente
    handlers.menu(update, context)
