import requests
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler, CallbackQueryHandler)
from src import login, utils, handlers, getters


CHOOSING, TYPING_REPLY = range(2)

reply_keyboard = [['Username', 'Email'],
                  [ 'Senha', 'Raça'],
                  ['Trabalho', 'Genero sexual' ],
                  ['Cancelar']]

required_data = set()

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)

#Inicia o cadastro
def start(update, context):
    
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


#Send current received information from user
def received_information(update, context):
    
    #Get data of user
    user_data = context.user_data
    text = update.message.text

    category = user_data['choice']
    user_data[category] = text

    del user_data['choice']
    
    #Valida os dados inseridos
    validation = utils.validations_signup(user_data)

    #Adiciona ou retira a check mark do botão da categoria conforme validação da entrada
    for i, items in enumerate(reply_keyboard):
        for j, item in enumerate(items):
            if category in item:
                if validation and '✅' not in item:
                    reply_keyboard[i][j] = item + '✅'
                elif not validation and '✅' in item:
                    reply_keyboard[i][j] = item[:-1]

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

    unreceived_info(context)
    


    if len(required_data) > 0:
        footer = "\n\nVocê pode me dizer os outros dados ou alterar os já inseridos.\n\n"

        if ['Done'] in reply_keyboard:
            undone_keyboard()

    else:

        footer = "\n\nAgora que adcionou todos os dados, pode editar os inseridos ou clicar em Done para enviar o formulário!\n"
        form_filled()


    #Envia o feedback ao user
    update.message.reply_text(head +
                            "{}".format(utils.dict_to_str(user_data))
                            + footer, reply_markup=markup)

    #Se as informações  estiverem completas, essa estrutura não é enviada
    if len(required_data) > 0:
        update.message.reply_text("Ainda falta(m):\n"
                                  "{}".format(utils.set_to_str(required_data)))

    return CHOOSING


#Caso a pessoa tenha adcionado todas as informações e 
#Depois adcionou uma inválida novamente, ele retira o
#Botão de done
def undone_keyboard():
    reply_keyboard.remove(['Done'])
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)


#Função que adciona done ao terminar de adcionar todas informações
def form_filled():
    if not ['Done'] in reply_keyboard:
        reply_keyboard.append(['Done'])
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    

#Termina cadastro e envia ao servidor da API do guardiões
def done(update, context):


    #Estrutura necessária para não permitir a finalização incorreta de um cadastro
    #Caso o usario tenha adcionado todas as infos, ele aceita a entrada
    if len(context.user_data) == 6:
        
        #Reinicia o teclado removendo a opção de Done
        reply_keyboard.remove(['Done'])
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)

        getters.get_birthday(update, context)   #Recebe o aniversário e envia a request a API
                                        #Para registrar

    
    #Caso não, ele manda uma mensagem de falha no cadastro
    else:   
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Falha ao registrar, não adcionou todos dados necessários!"
        )

    
    return ConversationHandler.END

def unreceived_info(context):
    all_items = ("Username", "Email", "Senha","Raça", "Trabalho", "Genero sexual")
    for item in all_items:
        if not item in context.user_data:
            required_data.add(item)


#Opçoes de entrada de informação do menu de cadastro
def regular_choice(update, context):

    #Remove a check mark da entrada do usuário caso esteja presente
    if '✅' in update.message.text:
        update.message.text = update.message.text[:-1]

    user_data = context.user_data

    text = update.message.text
    user_data['choice'] = text

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
        
    return TYPING_REPLY

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
            "country": "Brazil",
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
