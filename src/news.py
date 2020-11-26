from threading import Thread
from src import login, utils, handlers, getters, diario
from googlesearch import search
import re
import time

def run(update, context):
    
    hora = time.ctime().split()

    # Recebe a hora que será realizada o diario e enviado a noticia
    regex_time = utils.hour_routine()

    while utils.is_logged(context.user_data):
        
        hora = time.ctime().split()

        if re.search(regex_time, str(hora)):

            sendNews(update, context)

def sendNews(update, context):
    regex = r"[Ff]acebook|[Tt]witer|[Ii]nstagram|[Ll]inked[Ii]n|[Aa]rticle"
    data = time.ctime().split()

    res = []

    for resultado in search("saude plantão news", stop=10):
        res.append(resultado)

    resultadoPrint = ""

    for resultado in res:
        if not re.search(regex, resultado):

            if len(resultado) > len(resultadoPrint):
                resultadoPrint = resultado

    sendNew = "Olá, espero que esteja se sentindo bem! Hoje é " + str(stringDate()) + ".\n\n" + "A noticia do dia é: \n" + str(resultadoPrint) + "\n"

    context.bot.send_message(   chat_id=update.effective_chat.id,
                                text= str(sendNew))

    context.bot.send_message(   chat_id=update.effective_chat.id,
                                text= "Não se esqueça de reportar seu estado de saúde!")

    context.user_data['Global'] = True

def stringDate():

    dateTotal = (time.strftime("%A, %d %B %Y", time.gmtime()))
    dateTotal = dateTotal.replace('January', 'de janeiro de ')
    dateTotal = dateTotal.replace('February', 'de fevereiro de ')
    dateTotal = dateTotal.replace('March', 'de março de ')
    dateTotal = dateTotal.replace('April', 'de abril de ')
    dateTotal = dateTotal.replace('May', 'de maio de ')
    dateTotal = dateTotal.replace('June', 'de junho de ')
    dateTotal = dateTotal.replace('July', 'de julho de ')
    dateTotal = dateTotal.replace('August', 'agosto de ')
    dateTotal = dateTotal.replace('September', 'de setembro de ')
    dateTotal = dateTotal.replace('July', 'de julho de ')
    dateTotal = dateTotal.replace('October', 'de outubro de ')
    dateTotal = dateTotal.replace('November', 'de novembro de ')
    dateTotal = dateTotal.replace('December', 'de dezembro de ')
    dateTotal = dateTotal.replace('Sunday', 'domingo')
    dateTotal = dateTotal.replace('Monday', 'segunda-Feira')
    dateTotal = dateTotal.replace('Tuesday', 'terça-Feira')
    dateTotal = dateTotal.replace('Wednesday', 'quarta-Feira')
    dateTotal = dateTotal.replace('Thursday', 'quinta-Feira')
    dateTotal = dateTotal.replace('Friday', 'sexta-Feira')
    dateTotal = dateTotal.replace('Saturday', 'sábado')
    return dateTotal