import requests
from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler
from src import utils, handlers, getters

ENTRY_REGEX = '^(Username|Raça|Genero sexual|Nascimento|Grupo de Risco|Trabalho|Mostrar informações|Voltar)$'

CHOOSING, TYPING_REPLY = range(2)

required_data = set()

#Inicia o cadastro
def start(update, context):
    user_data = context.user_data
    context = context.user_data
    user_data['Keyboard'] = [   ['Username', 'Raça'],
                                ['Genero sexual', 'Nascimento'],
                                ['Trabalho', 'Grupo de Risco'],
                                ['Mostrar informações', 'Voltar']   ]
    markup = ReplyKeyboardMarkup(user_data['Keyboard'], one_time_keyboard=True, resize_keyboard=True)

    update.message.reply_text(
        "Escolha qual informação deseja alterar!",
        reply_markup=markup
    )

    return CHOOSING

#Opçoes de entrada de informação do menu de login
def regular_choice(update, context):
    user_data = context.user_data

    #Adciona uma chave com o valor de 'Email' ou 'Senha' de acordo com a escolha do user
    text = update.message.text

    #De acordo com a escolha, chama uma função
    if "Username" in text:
        user_data['edit_item'] = 'user_name'
        getters.get_User(update, context)

    if "Raça" in text:
        user_data['edit_item'] = 'race'
        getters.get_Race(update, context)    

    if "Genero sexual" in text:
        user_data['edit_item'] = 'gender'
        getters.get_Gender(update, context)    

    if "Nascimento" in text:
        user_data['edit_item'] = 'birthdate'
        getters.get_birthday_edit(update, context)   
        
        return CHOOSING

    if "Grupo de Risco" in text:
        user_data['edit_item'] = 'risk_group'
        getters.get_Risco(update, context)    
          
    if "Trabalho" in text:
        user_data['edit_item'] = 'is_professional'
        getters.get_professional(update, context)

    if "Mostrar informações" in text:
        user_data['edit_item'] = 'none'
        user_data['edit_item'] = 'none'
        user_data['choice'] = 'none'
        utils.image(context.user_data)
        path = 'general/images/robo_save.png'
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open( path, 'rb'))

        return CHOOSING

    if "Voltar" in text:
        handlers.menu(update, context)
        return ConversationHandler.END

    return TYPING_REPLY

#Send current received information from user
def received_information(update, context):

    user_data = context.user_data
    text = update.message.text
    user_data['resp_item'] = text

    dictEdit = {}
    dictEdit[user_data['edit_item']] = user_data['resp_item']

    #Valida os dados inseridos
    validation = utils.validations_edition(dictEdit)

    if not validation:
        head = "Entrada inválida. Tem certeza que seguiu o formato necessário? Retornando ao menu de edição. \n"
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= str(head)
        )
    else:
        head = "Perfeito, ja temos esses dados:\n"
        requestEdit(update, context)

    keyboard =  [['Username', 'Raça'],
                ['Genero sexual', 'Nascimento'],
                ['Trabalho', 'Grupo de Risco'],
                ['Mostrar informações', 'Voltar']]

    markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(
        "Escolha qual informação deseja alterar!",
        reply_markup=markup
    )

    return CHOOSING

#Funcao que cadastra o usuario
def requestEdit(update, context):
    user_data = context.user_data

    edit_item = user_data['edit_item']
    resp_item = user_data['resp_item']

    del user_data['edit_item']
    del user_data['resp_item']

    user_data.update({str(edit_item) : str(resp_item)})

    #Transforma a resposta do trabalho legivel ao
    #banco de dados
    if user_data.get('is_professional') == 'Sim':
        user_data.update({'is_professional' : 'true'})

    if user_data.get('is_professional') == 'Não':
        user_data.update({'is_professional' : 'false'})

    if user_data.get('risk_group') == 'Sim':
        user_data.update({'risk_group' : 'true'})

    if user_data.get('risk_group') == 'Não':
        user_data.update({'risk_group' : 'false'})

    if user_data.get('group_id') == 'Sim':
        user_data.update({'group_id' : 'true'})

    if user_data.get('group_id') == 'Não':
        user_data.update({'group_id' : 'false'})

    #Json enviado a API do guardiões com informações
    #Retiradas da API do telegram
    json_entry = {
            "user_name": user_data.get('user_name'),
            "birthdate": str(user_data.get('Nascimento')),
            "country": user_data.get('country'),
            "gender": user_data.get('gender'),
            "race": user_data.get('race'),
            "school_unit_id": user_data.get('school_unit_id'),
            "identification_code": user_data.get('identification_code'),
            "is_professional": user_data.get('is_professional'),
            "risk_group": user_data.get('risk_group'),
            "state": user_data.get('state'),
            "city": user_data.get('city')
    }
    headers = {'Accept' : 'application/vnd.api+json', 'Content-Type' : 'application/json', 'Authorization' : str(user_data['AUTH_TOKEN'])}
    r = requests.patch("http://127.0.0.1:3001/users/" + str(user_data.get('id')) , json=json_entry, headers=headers)

    if r.status_code == 200: # Sucesso
        # update.message.reply_text("Você alterou a informação com sucesso, retornando ao menu de edição\n")  
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= "Você alterou a informação com sucesso, retornando ao menu de edição\n"
        )
        print("request perfil acept")

    else: #Falha
        # update.message.reply_text("Algo deu errado com a edição, retornando ao menu de edição\n")   
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= "Algo deu errado com a edição, retornando ao menu de edição\n"
        )
        print("request perfil fail")

def bad_entry(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Opção inválida, tente utilizar os botões!\nRetornando ao menu de edição."
    ) 
    start(update, context)
