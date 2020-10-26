from telegram import Bot,Update
from telegram.ext import CommandHandler, CallbackContext, Dispatcher, Filters, CallbackQueryHandler,MessageHandler, Updater, ConversationHandler
from src import handlers, signup
import pathlib


SIGNUP_ENTRY_REGEX = '^(Username|Username✅|Email|Email✅|Senha|Senha✅|Genero sexual|Genero sexual✅|Raça|Raça✅|Trabalho|Trabalho✅)$'
LOGIN_ENTRY_REGEX = '^(Email|Email✅|Senha|Senha✅)$'
PERFIL_ENTRY_REGER = '^(Username|Raça|Genero sexual|Nascimento|País|Estado|Cidade|Grupo de Risco|Instituição de Ensino|Universidade|Matricula|Faculdade|Trabalha|Mostrar informações|Voltar)$'

class Bot:


    def __init__(self):

        try:
            # Le o token no arquivo 'token.txt' e passa para a variavel
            current_path = pathlib.Path(__file__).parent.absolute()
            f = open(str(current_path) + "/../config/token.txt", "r")
            TELEGRAM_TOKEN = f.read()

            # Estrutura responsavel por verificar todas novas mensagens
            self.updater = Updater(token=TELEGRAM_TOKEN, use_context=True)

            # Estrutura responsavel por interpretar mensagens recebidas e respondelas
            # de acordo com a interpretacao de cada uma
            dispatcher = self.updater.dispatcher

            # Mensagens reconhecidas
            dispatcher.add_handler(CommandHandler("start", handlers.start)) # Menu inicial
            dispatcher.add_handler(CommandHandler("menu", handlers.start)) # Menu inicial

            dispatcher.add_handler(MessageHandler(Filters.text("Sobre"), handlers.sobre)) # Sobre o bot
            dispatcher.add_handler(MessageHandler(Filters.text("Finalizar"), handlers.finalizar )) # Finalizar conversa

            # Handler para mostrar informações do usuário
            dispatcher.add_handler(MessageHandler(Filters.text("Minhas informações"), handlers.get_user_info)) 

            # Handler para mostrar informações do usuário
            # dispatcher.add_handler(MessageHandler(Filters.text("Editar informações"), handlers.edit_user_info)) 
            
            # Estrutura para registros
            dispatcher.add_handler(handlers.signup_handler())
            
            # Estrutura para login
            dispatcher.add_handler(handlers.login_handler())
            
            # Estrutura para mostrar o perfil/editar perfil
            dispatcher.add_handler(handlers.perfil_handler())

            # Função de logout
            dispatcher.add_handler(MessageHandler(Filters.text("Logout"), handlers.logout))
            
            # Callback query do calendário
            dispatcher.add_handler(CallbackQueryHandler(handlers.birthDayCallBack))

            # Mensagens não reconhecidas, serão respondidas aqui por uma mensagem generica
            dispatcher.add_handler(MessageHandler(Filters.all , handlers.unknown)) 

        except Exception as e:
            print(e)
            print("Token não encontrado, alguns motivos:\n"
                  "1 - Executou na pasta raiz?\n"
                  "2 - Realmente tem um arquivo token.txt na pasta config?")


    def run(self):
        #Mantem o bot rodando localmente enquanto o programa estiver sendo executado
        self.updater.start_polling()
        self.updater.idle()
