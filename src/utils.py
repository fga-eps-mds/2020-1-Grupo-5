import json, requests
from validate_email import validate_email
from src import handlers
from telegram.ext import ConversationHandler

def is_logged(user_data):
    if user_data.get('AUTH_TOKEN'):
        return True

    return False

#Funcao que retorna uma string de um SET
def set_to_str(data):

    remain_data = list()
    
    for value in data:
        remain_data.append('{}.'.format(value))

    return "\n".join(remain_data).join(['\n', '\n'])    


#Passa dict para string
def dict_to_str(user_data):
    
    lst = list()

    for key, value in user_data.items():
        if key != 'Keyboard':
            lst.append('{} - {}'.format(key, value))

    return "\n".join(lst).join(['\n', '\n'])
    

def cancel(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Cancelando!\nRetornando automaticamente ao menu!"
    )
    context.user_data.clear()
    handlers.menu(update, context)
    return ConversationHandler.END

def bad_entry(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Opção inválida, tente utilizar os botões!\nRetornando ao menu."
    )
    context.user_data.clear()

    handlers.menu(update, context)

    return ConversationHandler.END

def validaNome(nome):
    if len(nome) >= 8:
        return True

    return False

def validaSenha(senha):
    if len(senha) >= 8:
        return True

    return False

def validaEmail(email):

    if validate_email(email):
        return True

    return False

def validaGenero(genero):
    if str(genero).lower() in ['homem cis', 'homem homossexual', 'mulher cis', 'mulher homossexual', 'outro']:
        return True

    return False

def validaRaca(raca):
    if str(raca).lower() in ['branco', 'negro', 'pardo', 'indigena', 'amarelo', 'outro']:
        return True

    return False

def validaTrabalho(trabalho):
    if str(trabalho).lower() in ['sim', 'não', 'nao']:
        return True

    return False


def validations_login(user_data):
    if "Email" in user_data and not validaEmail(user_data['Email']):
            user_data.pop("Email")
            return False

    if "Senha" in user_data and not validaSenha(user_data['Senha']):
            user_data.pop("Senha")
            return False
    
    return True

def validations_signup(user_data):
    
    if "Username" in user_data and not validaNome(user_data['Username']):
            user_data.pop("Username")
            return False

    if "Email" in user_data and not validaEmail(user_data['Email']):
            user_data.pop("Email")
            return False
    
    if "Senha" in user_data and not validaSenha(user_data['Senha']):
            user_data.pop("Senha")
            return False

    if "Genero sexual" in user_data and not validaGenero(user_data['Genero sexual']):
            user_data.pop('Genero sexual')
            return False

    if "Raça" in user_data and not validaRaca(user_data['Raça']):
            user_data.pop('Raça')
            return False
    
    if "Trabalho" in user_data and not validaTrabalho(user_data['Trabalho']):
            user_data.pop("Trabalho")
            return False

    return True

def request_informations(context):
    
    print("Entrou!")

    print(context)

    json_entry = {
        "user" : {
            "email" : context['Email'],
            "password" : context['Senha']
        }
    }

    headers = {'Accept' : 'application/vnd.api+json', 'Content-Type' : 'application/json'}

    #Faz a tentativa de cadastro utilizando o json e os headers inseridos
    r = requests.post("http://127.0.0.1:3001/user/login", json=json_entry, headers=headers)
    
       #Log de sucesso ou falha no cadastro
    if r.status_code == 200: # Sucesso

        # print("user Antes:", user)

        user = json.loads(r.content)['user'] # Pega os dados do usuario logado

        user['AUTH_TOKEN'] = r.headers['Authorization']
        user['Senha'] = context['Senha']

        # print("User:", user)

        return user



    #     #Token de autorização de sessão
    #     context.user_data['AUTH_TOKEN'] = r.headers['Authorization']

    #     context.user_data['Username'] = user['user_name']

    #     context.user_data['user_id'] = user['id']

    #     del context.user_data['Senha'] # Remove a senha do usuário do cache para garantir segurança

    #     context.bot.send_message(
    #         chat_id=update.effective_chat.id,
    #         text=f"{context.user_data['Username']} seja bem vindo(a) ao DoctorS Bot, o chat bot integrado ao Guardiões da Saúde."
    #     )
    
    # else: #Falha
    #     context.bot.send_message(
    #         chat_id=update.effective_chat.id,
    #         text="Seu login falhou!\n\nTem certeza que digitou os dados corretamente?"
    #     )

    # #Chama o menu novamente
    # handlers.menu(update, context)
