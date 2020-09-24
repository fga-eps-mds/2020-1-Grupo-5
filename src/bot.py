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
            dispatcher.add_handler(CommandHandler("menu", handlers.start))
            dispatcher.add_handler(MessageHandler(Filters.text("Sobre"), handlers.sobre)) # Sobre o bot
            dispatcher.add_handler(MessageHandler(Filters.text("Finalizar"), handlers.finalizar )) #Finalizar conversa
            dispatcher.add_handler(MessageHandler(Filters.text("Login"), handlers.login)) # Login de usuario

            # Estrutura para registros
            dispatcher.add_handler(ConversationHandler(
            entry_points=[MessageHandler(Filters.text("Registrar"), signup.start)],
            states={
                signup.CHOOSING: [MessageHandler(Filters.regex('^(Username|Email|Senha|Genero sexual|Raça|Trabalho|Data nascimento)$'),
                                        signup.regular_choice)
                        ],
                signup.TYPING_CHOICE: [
                    MessageHandler(Filters.text & ~(Filters.command | Filters.regex('^Done$')),
                                signup.regular_choice)],
                signup.TYPING_REPLY: [
                    MessageHandler(Filters.text & ~(Filters.command | Filters.regex('^Done$')),
                                signup.received_information)],
            },
            fallbacks=[MessageHandler(Filters.regex('^Done$'), signup.done)],
            allow_reentry=True
            ))
            
            #Callback query do calendário
            dispatcher.add_handler(CallbackQueryHandler(signup.birthDayCallBack))

            #Mensagens não reconhecidas, serão respondidas aqui por uma mensagem generica
            dispatcher.add_handler(MessageHandler(Filters.all , handlers.unknown)) 


        except:
            print("Token não encontrado, alguns motivos:\n"
                  "1 - Executou na pasta raiz?\n"
                  "2 - Realmente tem um arquivo token.txt na pasta config?")

    def run(self):
        #Mantem o bot rodando localmente enquanto o programa estiver sendo executado
        self.updater.start_polling()
