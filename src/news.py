from src import utils
from googlesearch import search
import re
import time

def run(update, context):
    
    hora = time.ctime().split()

    regex_time = r"[1][9]:[4][1]:[1][0]"

    while utils.is_logged(context.user_data):
        
        hora = time.ctime().split()

        if re.search(regex_time, str(hora)):

            # utils.sendNews(update, context)
            sendNews(update, context)
            print("Hora: :", hora[3])

    print("End Thread!")


def sendNews(update, context):
    regex = r"[Ff]acebook|[Tt]witer|[Ii]nstagram|[Ll]inked[Ii]n|[Aa]rticle"

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
    
    # sendNew = "Olá, espero que esteja se sentindo bem! Hoje é dia " + str(data[2]) + " de " + str(month(data[1])) + ", a noticia do dia é: \n" + str(resultadoPrint)


    sendNew = "Olá, espero que esteja se sentindo bem! Hoje é " + str(stringDate()) + ".\n\n" + "A noticia do dia é: \n" + str(resultadoPrint) + "\n"

    context.bot.send_message(   chat_id=update.effective_chat.id,
                                text= str(sendNew))


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