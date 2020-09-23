import requests
import json
from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
import utils
from customCalendar import CustomCalendar
from datetime import date


CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

LSTEP = {'y': 'ano', 'm': 'mês', 'd': 'dia'}

reply_keyboard = [['Username', 'Email','Senha'],
                  [ 'Dia nascimento','Mes nascimento', 'Ano nascimento'],
                  ['Raça', 'Trabalho', 'Genero sexual' ]]

race_options = [['Branco', 'Negro', 'Pardo'],
                ['Indigena', 'Amarelo', 'Outro']]

gender_options = [['Homem Cis', 'Mulher Cis'],
                  ['Homem Homossexual', 'Mulher Homossexual'],
                  ['Outro']]

yes_no = [['Sim', 'Não']]

required_data = { "Username", "Email", "Senha", "Dia nascimento", "Mes nascimento", "Ano nascimento",
            "Raça", "Trabalho", "Genero sexual"}

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

race_markup = ReplyKeyboardMarkup(race_options, one_time_keyboard=True)

gender_markup = ReplyKeyboardMarkup(gender_options, one_time_keyboard=True)

yes_no_markup = ReplyKeyboardMarkup(yes_no, one_time_keyboard=True)


#Inicia o cadastro

def start(update, context):

    #Mensagem de inicio de cadastro
    update.message.reply_text(
        "Olá, é um prazer te conhecer! Eu sou o DoctorS Bot e estou aqui para facilitar sua vida em tempos de pandemia. "
        "\n\nPara utilizar nosso sistema, preciso que adcione todas essas informações!",
        reply_markup=markup)

    return CHOOSING


#Send current received information from user
def received_information(update, context):

    #Get data of user
    user_data = context.user_data
    text = update.message.text

    category = user_data['choice']
    user_data[category] = text
    
    del user_data['choice']

    #Valida os dados inseridos
    validation = utils.validations(user_data, required_data)
       
    #Estrutura que mostra informações que ainda faltam ser inseridas
    if len(user_data) > 0:
        for key in user_data:
            if key in required_data:
                required_data.remove(key)

    #Se a ultima entrada não for valida, enviamos mensagem de entrada
    #Invalida
    if not validation:
        head = "Entrada inválida. Tem certeza que seguiu o formato necessário?\n"

    else:
        head = "Perfeito, ja temos esses dados:\n"


    #Envia o feedback ao user
    update.message.reply_text(head +
                            "{} Você pode me dizer os outros dados ou alterar os"
                            " já inseridos.\n\n".format(dict_to_str(user_data)), reply_markup=markup)

    #Se as informações  estiverem completas, essa estrutura não é enviada
    if len(required_data) > 0:
        update.message.reply_text("Ainda falta(m):\n"
                                  "{}".format(set_to_str(required_data)))

    return CHOOSING


#Termina cadastro e envia ao servidor da API do guardiões
def done(update, context):

    #Pega todas as infos adcionadas
    user_data = context.user_data

    #Transforma a resposta do trabalho em legivel ao
    #banco de dados
    if user_data.get('Trabalho') and 'sim' in user_data.get('Trabalho').lower():
        user_data.update({'Trabalho' : 'true'})

    else:
        user_data.update({'Trabalho' : 'false'})


    #Json enviado a API do guardiões com informações
    #Retiradas da API do telegram
    json_entry = {
        "user" : {
            "email": user_data.get('Email'),
            "user_name": user_data.get('Username'),
            "birthdate": f"{user_data.get('Ano nascimento')}-{user_data.get('Mes nascimento')}-{user_data.get('Dia nascimento')}",
            "country": "Brazil",
            "gender": user_data.get('Genero sexual'),
            "race": user_data.get('Raça'),
            "is_professional": user_data.get('Trabalho'),
            "picture": "default",
            "password": user_data.get('Senha'),
            "is_god": "false"
        }
    }

    
    #Limpa caso tenha a key 'choice' no dict user_data
    if 'choice' in user_data:
        del sorted_user_data['choice']

    #Envia a mensagem de cadastro
    update.message.reply_text("Nós cadastraremos com esses dados:"
                        "{}".format(dict_to_str(user_data)))


    #Faz a tentativa de cadastro utilizando o json e os headers inseridos
    r = requests.post("http://127.0.0.1:3001/user/signup", json=json_entry, headers={'Accept' : 'application/vnd.api+json', 'Content-Type' : 'application/json'})
    

    #Loggin de sucesso ou falha no cadastro
    if r.status_code == 200:
        update.message.reply_text("Cadastro efetuado com sucesso!")
        print("Successfull signup:")
    
    else:

        print("Signup Failed!")

        update.message.reply_text("Falha no cadastro!")

    print(r.content)

    user_data.clear()
    

    return ConversationHandler.END



#Funcao que retorna uma string de um SET
def set_to_str(data):

    remain_data = list()
    
    for value in data:
        remain_data.append('{}.'.format(value))

    return "\n".join(remain_data).join(['\n', '\n'])    


#Passa dict para string
def dict_to_str(user_data):
    
    facts = list()

    for key, value in user_data.items():
        facts.append('{} - {}'.format(key, value))

    return "\n".join(facts).join(['\n', '\n'])



#Opçoes de entrada de informação do menu de cadastro
def regular_choice(update, context):

    if len(required_data) == 1:
        reply_keyboard.append(['Done'])
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    
    
    user_data = context.user_data

    text = update.message.text
    user_data['choice'] = text


    if  "Username" in text:
        get_User(update,context)
        
    if "Email" in text:
        get_Email(update, context)

    if "Senha" in text:
        get_Pass(update, context)

    if "Mes nascimento" in text:
        get_birthmonth(update, context)
    
    if "Dia nascimento" in text:
        get_birthday(update, context)

    if "Ano nascimento" in text:
        get_birthyear(update, context)

    if "Raça" in text:
        get_Race(update, context)

    if "Genero sexual" in text:
        get_Gender(update, context)

    if "Trabalho" in text:
        get_professional(update, context)

    return TYPING_REPLY


#Funcao que recebe o usuario
def get_User(update, context):
    text = update.message.text
    context.user_data['choice'] = text
    update.message.reply_text(
        'Digite um nome válido, com mais de 8 caracteres!'
    )

    return TYPING_REPLY


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


#Funcao que recebe a Raça do usuario
def get_Race(update, context):
    text = update.message.text
    context.user_data['choice'] = text
    update.message.reply_text(
        'Selecione sua raça.', reply_markup=race_markup
    )

    return CHOOSING
    


#Funcao que recebe o genero do usuario
def get_Gender(update, context):
    text = update.message.text
    context.user_data['choice'] = text
    update.message.reply_text(
        'Selecione seu genero.', reply_markup=gender_markup
    )

    return CHOOSING

#Função de callback do calendário
def cal(update, context):
    query = update.callback_query
    result, key, step = CustomCalendar(locale='br', max_date=date.today()).process(query.data)
    if not result and key:
        query.edit_message_text(f"Selecione o {LSTEP[step]}",
                              reply_markup=key)
    elif result:
        query.edit_message_text(f"Você selecionou {result}")

#Funcao que recebe o dia de nascimento
def get_birthday(update, context):
    calendar, step = CustomCalendar(locale='br', max_date=date.today()).build()
    update.message.reply_text(f"Selecione o {LSTEP[step]}",
                            reply_markup=calendar)
    return CHOOSING

#Funcao que recebe o mes de nascimento
def get_birthmonth(update, context):
    text = update.message.text
    context.user_data['choice'] = text
    update.message.reply_text(
        'Digite o mes em que nasceu.(01-12)'
    )

    return TYPING_REPLY


#Funcao que recebe o ano de nascimento
def get_birthyear(update, context):
    text = update.message.text
    context.user_data['choice'] = text
    update.message.reply_text(
        'Digite o ano em que nasceu'
    )

    return TYPING_REPLY



#Funcao que recebe se o usario trabalha ou não
def get_professional(update, context):
    text = update.message.text
    context.user_data['choice'] = text
    update.message.reply_text(
        'Você trabalha?', reply_markup=yes_no_markup
    )

    return CHOOSING
