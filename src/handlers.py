
import requests


#Envia o menu para o usuario
def start(update, context):
    resposta = ("Bem vindo ao DoctorS Bot, digite a opção que desejar:\n\n"
                "/Sobre - Para mais informações\n")
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=resposta
    )

#Envia informaçoes sobre o bot
def sobre(update, context):
    resposta = 'O DoctorS é um Telegram Bot criado para ajudar a população no combate ao novo Corona Vírus(SARS-CoV-2).'
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=resposta
    )


#Mensagens não reconhecidas
def unknown(update, context):
    resposta = "Não entendi. Tem certeza de que digitou corretamente?"
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=resposta,
    )