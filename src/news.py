from threading import Thread
from src import login, utils, handlers, getters
from googlesearch import search
import re
import time

def run(update, context):
    
    regex_time = r"[1][7]:[1][5]:[1][0]"

    while utils.is_logged(context.user_data):
        
        hora = time.ctime().split()

        if re.search(regex_time, str(hora)):

            # utils.sendNews(update, context)
            sendNews(update, context)
            print("Hora: :", hora[3])

    print("End Thread!")


def sendNews(update, context):
    regex = r"[Ff]acebook|[Tt]witer|[Ii]nstagram|[Ll]inked[Ii]n|[Aa]rticle"
    data = time.ctime().split()

    res = []
    # for resultado in search('"noticias saúde" news', stop=10):
    for resultado in search("saude plantão news", stop=10):
        res.append(resultado)
        # print(resultado)

        # print(res)
    resultadoPrint = ""

    for resultado in res:
        if not re.search(regex, resultado):
            # print("\n", resultado)
            if len(resultado) > len(resultadoPrint):
                resultadoPrint = resultado

    print("Resul print: ", resultadoPrint)
    


    sendNew = "Olá, espero que esteja se sentindo bem! Hoje é dia " + str(data[2]) + " de " + str(month(data[1])) + ", a noticia do dia é: \n" + str(resultadoPrint)

    context.bot.send_message(   chat_id=update.effective_chat.id,
                                text= str(sendNew))


def month(mes):
    if mes == 'Oct':
        return 'outubro'