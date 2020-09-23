import json
from telegram import Bot,Update
from telegram.ext import CommandHandler, Dispatcher, Filters, MessageHandler, Updater, ConversationHandler, CallbackQueryHandler
import handlers
import signup
import pathlib


class Bot:
    def __init__(self):

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

        # Estrutura para registros
        dispatcher.add_handler(ConversationHandler(
        entry_points=[MessageHandler(Filters.text("Registrar"), signup.start)],
        states={
            signup.CHOOSING: [MessageHandler(Filters.regex('^(Username|Email|Senha|Genero sexual|Raça|Trabalho|Dia nascimento|Mes nascimento|Ano nascimento)$'),
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

        #Mensagens não reconhecidas, serão respondidas aqui por uma mensagem generica
        dispatcher.add_handler(MessageHandler(Filters.all , handlers.unknown)) 

        #Callback query do calendário
        dispatcher.add_handler(CallbackQueryHandler(signup.cal))

    def run(self):
        #Mantem o bot rodando localmente enquanto o programa estiver sendo executado
        self.updater.start_polling()


bot = Bot()
bot.run()
