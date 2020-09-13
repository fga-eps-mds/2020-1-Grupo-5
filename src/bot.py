import json
from telegram import Bot, Update
from telegram.ext import CommandHandler, Dispatcher, Filters, MessageHandler, Updater
from handlers import start, sobre, unknown


class Bot:
    def __init__(self):

        #Le o token no arquivo 'token.txt' e passa para a variavel
        f = open("token.txt", "r")
        TELEGRAM_TOKEN = f.read()

        #Estrutura responsavel por verificar todas novas mensagens
        self.updater = Updater(token=TELEGRAM_TOKEN, use_context=True)

        # Estrutura responsavel por interpretar mensagens recebidas e respondelas
        # de acordo com a interpretacao de cada uma
        dispatcher = self.updater.dispatcher
        
        # Mensagens reconhecidas
        dispatcher.add_handler(CommandHandler("start", start)) # Menu inicial
        dispatcher.add_handler(CommandHandler("menu", start))


        dispatcher.add_handler(CommandHandler("sobre", sobre)) # Sobre o bot
        
        #Mensagens não reconhecidas, serão respondidas aqui por uma mensagem generica
        dispatcher.add_handler(MessageHandler(Filters.all , unknown)) 


    def run(self):
        #Mantem o bot rodando localmente enquanto o programa estiver sendo executado
        self.updater.start_polling()

