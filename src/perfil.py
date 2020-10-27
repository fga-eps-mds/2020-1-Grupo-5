import requests
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler, CallbackQueryHandler)
from src import login, utils, handlers, getters

CHOOSING, TYPING_REPLY = range(2)

required_data = set()

#Inicia o cadastro
def start(update, context):
    user_data = context.user_data
    
    resposta = context.user_data
    context = context.user_data

    user_data['Keyboard'] = [['Username', 'Raça'],
                            ['Genero sexual', 'Nascimento'],
                            ['Trabalho', 'Grupo de Risco'],
                            ['Mostrar informações', 'Voltar']]
    markup = ReplyKeyboardMarkup(user_data['Keyboard'], one_time_keyboard=True, resize_keyboard=True)

    update.message.reply_text(
        "Escolha qual informação deseja alterar!",
        reply_markup=markup)

    return CHOOSING



#Opçoes de entrada de informação do menu de login
def regular_choice(update, context):
    user_data = context.user_data


    #Adciona uma chave com o valor de 'Email' ou 'Senha' de acordo com a escolha do user
    text = update.message.text
    # user_data['choice'] = text



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
        getters.get_birthday(update, context)    

    if "Grupo de Risco" in text:
        user_data['edit_item'] = 'risk_group'
        getters.get_Risco(update, context)    
          

    if "Trabalho" in text:
        user_data['edit_item'] = 'is_professional'
        getters.get_professional(update, context)

    if "Mostrar informações" in text:
        resposta = context.user_data
        user_data['edit_item'] = 'none'
        user_data['choice'] = 'none'

        returnText = ""
        returnText = utils.image(resposta)
        path = 'src/images/robo_save.png'
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open( path, 'rb'))


        return CHOOSING


    if "Voltar" in text:
        handlers.menu(update, context)
        return ConversationHandler.END


    return TYPING_REPLY


#Send current received information from user
def received_information(update, context):
    user_data = context.user_data


    edit_item = user_data['edit_item']



    #Get data of user
    # user_data = context.user_data

    text = update.message.text
    user_data['resp_item'] = text
    del user_data['choice']

    requestEdit(update, context)


    keyboard =  [['Username', 'Raça'],
                ['Genero sexual', 'Nascimento'],
                ['Trabalho', 'Grupo de Risco'],
                ['Mostrar informações', 'Voltar']]

    markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(
        "Escolha qual informação deseja alterar!",
        reply_markup=markup)

    return CHOOSING





#Caso a pessoa tenha adcionado todas as informações e 
#Depois adcionou uma inválida novamente, ele retira o
#Botão de done
def undone_keyboard(context):
    context.user_data['Keyboard'].remove(['Done'])


#Função que adciona done ao terminar de adcionar todas informações
def form_filled(context):
    user_data = context.user_data
    if not ['Done'] in user_data['Keyboard']:
        user_data['Keyboard'].append(['Done'])
    

#Termina cadastro e envia ao servidor da API do guardiões
def done(update, context):


    #Estrutura necessária para não permitir a finalização incorreta de um cadastro
    #Caso o usario tenha adcionado todas as infos, ele aceita a entrada
    #7, pois devem existir 6 informações do usuário + teclado
    if len(context.user_data) == 7:
        
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
def requestEdit(update, context):

    user_data = context.user_data

    edit_item = user_data['edit_item']
    resp_item = user_data['resp_item']

    del user_data['edit_item']
    del user_data['resp_item']

    user_data.update({str(edit_item) : str(resp_item)})

    #Pega todas as infos adcionadas

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
            "birthdate": str(user_data.get('birthdate')),
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
        update.message.reply_text("Você alterou a informação com sucesso, retornando ao menu de edição\n")  

    else: #Falha
        update.message.reply_text("Algo deu errado com a edição, retornando ao menu de edição\n")  

         
