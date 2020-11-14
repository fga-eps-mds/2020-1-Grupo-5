import json, requests
from validate_email import validate_email
from src import handlers, perfil
from telegram.ext import ConversationHandler
from telegram import ReplyKeyboardMarkup
from PIL import Image, ImageDraw, ImageFont
from googlesearch import search
# pip install google

import re
import time


def is_logged(user_data):

    if user_data.get('AUTH_TOKEN'):
        return True

    return False


# Função que retorna uma string de um SET
def set_to_str(data):

    remain_data = list()
    
    for value in data:
        remain_data.append('{}.'.format(value))

    return "\n".join(remain_data).join(['\n', '\n'])    


# Passa dict para string
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

<<<<<<< HEAD
def bad_entry_edit(update, context):

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Opção inválida, tente utilizar os botões!\nRetornando ao menu de edição."
    )
    
    perfil.start(update, context)
=======
>>>>>>> 8ea4057d4a83d18386243b696c2c61014d236b25

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

def validaRisco(risco):

    if str(risco).lower() in ['sim', 'não', 'nao']:
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

def validations_edition(user_data):

    if "user_name" in user_data and not validaNome(user_data['user_name']):
        return False

    if "gender" in user_data and not validaGenero(user_data['gender']):
        return False

    if "race" in user_data and not validaRaca(user_data['race']):
        return False
    
    if "is_professional" in user_data and not validaTrabalho(user_data['is_professional']):
        return False

    if "risk_group" in user_data and not validaRisco(user_data['risk_group']):
        return False

    # if "birthdate" in user_data and not validaNascimento(user_data['birthdate']):
    #     return False

    return True

def image(entradaTexto):

    # get an image
    base = Image.open('general/images/robo.jpg').convert('RGBA')

    # make a blank image for the text, initialized to transparent text color
    txt = Image.new('RGBA', base.size, (0,0,0,0))
    fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 21, encoding='Adobe Standard')

    # get a drawing context
    d = ImageDraw.Draw(txt)

    # Organiza o texto a ser printado
    printText = geraString(entradaTexto)

    # Posição inicial do texto na imagem
    d.text((10,30), str(printText), font=fnt, fill=(0,0,0,255))
    out = Image.alpha_composite(base, txt)
    out.save("general/images/robo_save.png")

    return printText
    # out.show()

def geraString(text):

    texto = "Atualmente essas são as suas informações: " + "\n"

    # De acordo com a escolha chama uma função
    if "user_name" in text:
        texto =  texto  + "\n" + 'Username' + ": " + str(text['user_name'])

    if "race" in text:
        texto =  texto  + "\n" + 'Raça' + ": " + str(text['race'])

    if "gender" in text:
        texto =  texto  + "\n" + 'Genero sexual' + ": " + str(text['gender'])

    if "birthdate" in text:
        texto =  texto  + "\n" + 'Nascimento' + ": " + str(text['birthdate'])
  
    if "risk_group" in text:
        if text['risk_group'] == 'true' or text['risk_group'] == True:
            texto =  texto  + "\n" + 'Grupo de Risco' + ": Sim"
        else:
            texto = texto + "\n" + 'Grupo de Risco' + ": Não"

    if "is_professional" in text:
        if text['is_professional'] == 'true' or text['is_professional'] == True:
            texto =  texto  + "\n" + 'Trabalho' + ": Sim"
        else:
            texto = texto + "\n" + 'Trabalho' + ": Não"
  
    return texto

<<<<<<< HEAD
def sendNews(update, context):

    regex = r"[Ff]acebook|[Tt]witer|[Ii]nstagram|[Ll]inked[Ii]n|[Aa]rticle"
    res = []

    # for resultado in search('"noticias saúde" news', stop=10):
    for resultado in search("saude plantão news", stop=10):
        res.append(resultado)

    resultadoPrint = ""

    for resultado in res:

        if not re.search(regex, resultado):
            if len(resultado) > len(resultadoPrint):
                resultadoPrint = resultado

    context.bot.send_message(   chat_id=update.effective_chat.id,
                                text= str(resultadoPrint))
=======

# Remove a check mark do final da palavra caso esteja presente
def remove_check_mark(text):
    if '✅' == text[-1]:
        text = text[:-1]
    return text


# Insere ou remove a check mark do botão da categoria do teclado conforme sua validação
def update_check_mark(keyboard, category, validation):
    for i, items in enumerate(keyboard):
        for j, item in enumerate(items):
            if category in item:
                if validation and '✅' not in item:
                    keyboard[i][j] = item + '✅'
                    return
                elif not validation and '✅' in item:
                    keyboard[i][j] = item[:-1]
                    return


# Atualiza as informações que ainda faltam ser inseridas
def update_required_data(received_data, required_data):
    for key in received_data:
        if key in required_data:
            required_data.remove(key)


# Função que adiciona done ao terminar de adicionar todas as informações
def form_filled(keyboard):
    if not ['Done'] in keyboard:
        keyboard.append(['Done'])


# Caso a pessoa tenha adicionado todas as informações e depois adicionou uma inválida novamente, ele retira o botão de done
def undone_keyboard(keyboard):
    keyboard.remove(['Done'])


# Atualiza as informações que estão faltando
def unreceived_info(received_data, required_data, all_items):
    for item in all_items:
        if not item in received_data:
            required_data.add(item)


def received_information_reply(update, context, feedback):
    markup = ReplyKeyboardMarkup(context.user_data['Keyboard'], one_time_keyboard=True, resize_keyboard=True)

    # Envia o feedback ao user
    update.message.reply_text(feedback, reply_markup=markup)
>>>>>>> 8ea4057d4a83d18386243b696c2c61014d236b25
