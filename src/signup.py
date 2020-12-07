from telegram import ReplyKeyboardMarkup
from requests import post
from telegram.ext import ConversationHandler
from src import login, utils, handlers, getters, location

ENTRY_REGEX = '^(Username|Username✅|Email|Email✅|Senha|Senha✅|Genero sexual|Genero sexual✅|Raça|Raça✅|Trabalho|Trabalho✅|Localização|Localização✅)$'

CHOOSING, TYPING_REPLY = range(2)

required_data = set()

# Inicia o cadastro
def start(update, context):
    user_data = context.user_data
    if utils.is_logged(user_data):
        handlers.unknown(update, context)
        return ConversationHandler.END
    else:
        user_data.clear()
        user_data['Keyboard'] = [   ['Username', 'Email'],
                                    ['Senha', 'Raça'],
                                    ['Trabalho', 'Genero sexual'],
                                    ['Localização', 'Cancelar'] ]
        # Mensagem de início de cadastro
        markup = ReplyKeyboardMarkup(user_data['Keyboard'], one_time_keyboard=True, resize_keyboard=True)
        update.message.reply_text(
            "Olá, é um prazer te conhecer! Eu sou o DoctorS Bot e estou aqui para facilitar a sua vida em tempos de pandemia.\n\n"
            "Para utilizar nosso sistema preciso que adicione todas essas informações listadas abaixo!\n\n"
            "Basta selecionar a opção que deseja adicionar e digitar!",
            reply_markup=markup
        )

        return CHOOSING


# Opções de entrada de informação do menu de cadastro
def regular_choice(update, context):
    update.message.text = utils.remove_check_mark(update.message.text)

    text = update.message.text
    context.user_data['choice'] = text

    if  "Username" in text:
        getters.get_User(update,context)     
    elif "Email" in text:
        getters.get_Email(update, context)
    elif "Senha" in text:
        getters.get_Pass(update, context)
    elif "Raça" in text:
        getters.get_Race(update, context)
    elif "Genero sexual" in text:
        getters.get_Gender(update, context)
    elif "Trabalho" in text:
        getters.get_professional(update, context)
    elif "Localização" in text:
        getters.get_location(update, context)

    return TYPING_REPLY

# Envia as informações atualmente recebidas do usuário
def received_information(update, context):
    category = update_received_information(context, update)
    head = validation_management(context.user_data, category)
    footer = update_missing_info(context.user_data)

    feedback = head + "{}".format(utils.dict_to_str(context.user_data)) + footer

    # Se as informações estiverem completas essa estrutura não é adicionada
    if len(required_data) > 0:
        feedback = feedback + "Ainda falta(m):\n{}".format(utils.set_to_str(required_data))

    utils.received_information_reply(update, context, feedback)

    return CHOOSING

def update_received_information(context, update):
    # Adiciona a informação enviada pelo user à sua respectiva chave
    category = context.user_data['choice']
    del context.user_data['choice']

    if 'Localização' in category:
        location.reverseGeo(update.message.location, context.user_data)
    else:
        context.user_data[category] = update.message.text

    return category

def validation_management(user_data, category):
    # Validação de dados
    validation = utils.validations_signup(user_data)

    utils.update_check_mark(user_data['Keyboard'], category, validation)

    # Se a última entrada não for válida, enviamos mensagem de entrada inválida
    if validation:
        return "Perfeito, já temos esses dados:\n"
    else:
        return "Entrada inválida. Tem certeza que seguiu o formato necessário?\n"

def update_missing_info(user_data):
    # Estrutura que mostra as informações que ainda faltam ser inseridas
    utils.update_required_data(user_data, required_data)

    utils.unreceived_info(user_data, required_data, ("Username", "Email", "Senha","Raça", "Trabalho", "Genero sexual"))
    
    if len(required_data) == 0 and 'Cidade' in user_data:
        utils.form_filled(user_data['Keyboard'])
        return "\n\nAgora que adicionou todos os dados, pode editar os já inseridos ou clicar em Done para enviar o formulário!\n"
    
    if ['Done'] in user_data['Keyboard']:
        utils.undone_keyboard(user_data['Keyboard'])

    return "\n\nVocê pode me dizer os outros dados ou alterar os já inseridos.\n\n"

# Termina o cadastro e envia ao servidor da API do guardiões
def done(update, context):
    # Estrutura necessária para não permitir a finalização incorreta de um cadastro
    # Caso o usuário tenha adicionado todas as infos, ele aceita a entrada
    # 7, pois devem existir 6 informações do usuário + teclado
    if len(context.user_data) == 10:
        # Reinicia o teclado removendo a opção de Done
        context.user_data['Keyboard'].remove(['Done'])
        getters.get_birthday(update, context)   # Recebe o aniversário e envia a request a API para registrar

    # Caso contrário, ele manda uma mensagem de falha no cadastro
    else:   
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Falha ao registrar, não adicionou todos os dados necessários!"
        )

    return ConversationHandler.END

# Função que cadastra o usuário
def requestSignup(update, context):
    # Pega todas as infos adicionadas
    user_data = context.user_data

    # Transforma a resposta do trabalho legível ao banco de dados
    if user_data.get('Trabalho') and 'sim' in user_data.get('Trabalho').lower():
        user_data.update({'Trabalho' : 'true'})
    else:
        user_data.update({'Trabalho' : 'false'})

    # Json enviado à API do guardiões com as informações retiradas da API do Telegram
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

    # Faz a tentativa de cadastro utilizando o json e os headers inseridos
    r = post("http://127.0.0.1:3001/user/signup", json=json_entry, headers=headers)
    
    # Log de sucesso ou falha no cadastro
    if r.status_code == 200: # Sucesso
        print("Successfull signup:")    
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"{user_data.get('Username')}, você foi cadastrado(a) com sucesso!"
        )
        login.request_login(update, context)        
    else: # Falha
        print("Signup Failed!")
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"{user_data.get('Username')}, seu cadastro falhou!"
        )
        handlers.menu(update, context)
    print(r.content)    
