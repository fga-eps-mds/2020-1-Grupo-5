import requests
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler, CallbackQueryHandler)
from src import login, utils, handlers, getters, location

CHOOSING, TYPING_REPLY = range(2)

required_data = set()


#Inicia o cadastro
def start(update, context):
    user_data = context.user_data
    user_data['Keyboard'] = [['Username', 'Email'],
                            ['Senha', 'Raça'],
                            ['Trabalho', 'Genero sexual'],
                            ['Localização', 'Cancelar']]
    markup = ReplyKeyboardMarkup(user_data['Keyboard'], one_time_keyboard=True, resize_keyboard=True)

    if utils.is_logged(context.user_data):
        handlers.unknown(context, update)
        return ConversationHandler.END
    
    else:
        #Mensagem de inicio de cadastro
        update.message.reply_text(
            "Olá, é um prazer te conhecer! Eu sou o DoctorS Bot e estou aqui para facilitar sua vida em tempos de pandemia.\n\n"
            "Para utilizar nosso sistema, preciso que adcione todas essas informações listadas abaixo!\n\n"
            "Basta selecionar a opção que deseja adcionar e digitar!",
            reply_markup=markup)

        return CHOOSING


#Opçoes de entrada de informação do menu de cadastro
def regular_choice(update, context):

    update.message.text = utils.remove_check_mark(update.message.text)

    text = update.message.text
    context.user_data['choice'] = text

    if  "Username" in text:
        getters.get_User(update,context)
        
    if "Email" in text:
        getters.get_Email(update, context)

    if "Senha" in text:
        getters.get_Pass(update, context)

    if "Raça" in text:
        getters.get_Race(update, context)

    if "Genero sexual" in text:
        getters.get_Gender(update, context)

    if "Trabalho" in text:
        getters.get_professional(update, context)

    if "Localização" in text:
        getters.get_location(update, context)
        
    return TYPING_REPLY


#Send current received information from user
def received_information(update, context):
    
    category = update_received_information(context, update)
    head = validation_management(context.user_data, category)
    footer = update_missing_info(context.user_data)
    received_information_reply(update, context, head, footer)

    return CHOOSING


def update_received_information(context, update):
    #Adciona a informação enviada pelo user à sua respectiva chave
    category = context.user_data['choice']
    del context.user_data['choice']

    if 'Localização' in category:
        location.reverseGeo(update.message.location, context)
    else:
        context.user_data[category] = update.message.text

    return category


def validation_management(user_data, category):
    #Validação de dados
    validation = utils.validations_signup(user_data)

    utils.update_check_mark(user_data['Keyboard'], category, validation)

    # Se a ultima entrada não for valida, enviamos mensagem de entrada invalida
    if validation:
        return "Perfeito, ja temos esses dados:\n"
    else:
        return "Entrada inválida. Tem certeza que seguiu o formato necessário?\n"


def update_missing_info(user_data):
    # Estrutura que mostra informações que ainda faltam ser inseridas
    utils.update_required_data(user_data, required_data)

    utils.unreceived_info(user_data, required_data, ("Username", "Email", "Senha","Raça", "Trabalho", "Genero sexual"))
    
    if len(required_data) == 0:
        utils.form_filled(user_data['Keyboard'])
        return "\n\nAgora que adcionou todos os dados, pode editar os inseridos ou clicar em Done para enviar o formulário!\n"
    
    if ['Done'] in user_data['Keyboard']:
        utils.undone_keyboard(user_data['Keyboard'])

    return "\n\nVocê pode me dizer os outros dados ou alterar os já inseridos.\n\n"


def received_information_reply(update, context, head, footer):
    markup = ReplyKeyboardMarkup(context.user_data['Keyboard'], one_time_keyboard=True, resize_keyboard=True)

    #Envia o feedback ao user
    update.message.reply_text(head + "{}".format(utils.dict_to_str(context.user_data)) + footer, reply_markup=markup)

    #Se as informações  estiverem completas, essa estrutura não é enviada
    if len(required_data) > 0:
        update.message.reply_text("Ainda falta(m):\n"
                                  "{}".format(utils.set_to_str(required_data)))


#Termina cadastro e envia ao servidor da API do guardiões
def done(update, context):


    #Estrutura necessária para não permitir a finalização incorreta de um cadastro
    #Caso o usario tenha adcionado todas as infos, ele aceita a entrada
    #7, pois devem existir 6 informações do usuário + teclado
    if len(context.user_data) == 10:
        
        #Reinicia o teclado removendo a opção de Done
        context.user_data['Keyboard'].remove(['Done'])

        getters.get_birthday(update, context)   #Recebe o aniversário e envia a request a API
                                        #Para registrar

    
    #Caso não, ele manda uma mensagem de falha no cadastro
    else:   
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Falha ao registrar, não adcionou todos dados necessários!"
        )

    
    return ConversationHandler.END


#Funcao que cadastra o usuario
def requestSignup(update, context):
    #Pega todas as infos adcionadas
    user_data = context.user_data

    #Transforma a resposta do trabalho legivel ao
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
            "birthdate": str(user_data.get('Nascimento')),
            "country": user_data.get('País'),
            "state": user_data.get('Estado'),
            "city": user_data.get('Cidade'),
            "gender": user_data.get('Genero sexual'),
            "race": user_data.get('Raça'),
            "is_professional": user_data.get('Trabalho'),
            "picture": "default",
            "password": user_data.get('Senha'),
            "is_god": "false"
        }
    }

    headers = {'Accept' : 'application/vnd.api+json', 'Content-Type' : 'application/json'}


    #Faz a tentativa de cadastro utilizando o json e os headers inseridos
    r = requests.post("http://127.0.0.1:3001/user/signup", json=json_entry, headers=headers)
    

    #Log de sucesso ou falha no cadastro
    if r.status_code == 200: # Sucesso
        print("Successfull signup:")
        
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"{user_data.get('Username')}, você foi cadastrado com sucesso!"
        )

        login.request_login(update, context)        

    else: #Falha
        
        print("Signup Failed!")
        
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"{user_data.get('Username')}, seu cadastrado falhou!"
        )

    print(r.content)    
