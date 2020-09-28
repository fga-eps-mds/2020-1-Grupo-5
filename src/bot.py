from telegram import Bot,Update
from telegram.ext import CommandHandler, Dispatcher, Filters, CallbackQueryHandler,MessageHandler, Updater, ConversationHandler
import src.handlers as handlers
import src.signup as signup
import pathlib


class Bot:
    def __init__(self):

        try:
            #Le o token no arquivo 'token.txt' e passa para a variavel
            current_path = pathlib.Path(__file__).parent.absolute()
            f = open(str(current_path) + "/../config/token.txt", "r")
            TELEGRAM_TOKEN = f.read()

            #Estrutura responsavel por verificar todas novas mensagens
            self.updater = Updater(token=TELEGRAM_TOKEN, use_context=True)

            # Estrutura responsavel por interpretar mensagens recebidas e respondelas
            # de acordo com a interpretacao de cada uma
            dispatcher = self.updater.dispatcher
            
            # Mensagens reconhecidas
            dispatcher.add_handler(CommandHandler("start", handlers.start)) # Menu inicial
            dispatcher.add_handler(CommandHandler("menu", handlers.start)) # Menu inicial

            dispatcher.add_handler(MessageHandler(Filters.text("Sobre"), handlers.sobre)) # Sobre o bot
            dispatcher.add_handler(MessageHandler(Filters.text("Finalizar"), handlers.finalizar )) #Finalizar conversa

            # Estrutura para registros
            dispatcher.add_handler(handlers.signup_handler())
            
            
            #Callback query do calendário
            dispatcher.add_handler(CallbackQueryHandler(signup.birthDayCallBack))

            #Mensagens não reconhecidas, serão respondidas aqui por uma mensagem generica
            dispatcher.add_handler(MessageHandler(Filters.all , handlers.unknown)) 


        except Exception as e:
            print(e)
            print("Token não encontrado, alguns motivos:\n"
                  "1 - Executou na pasta raiz?\n"
                  "2 - Realmente tem um arquivo token.txt na pasta config?")

    def run(self):
        #Mantem o bot rodando localmente enquanto o programa estiver sendo executado
        self.updater.start_polling()
