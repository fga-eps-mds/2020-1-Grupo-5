from telegram import ReplyKeyboardMarkup

ENTRY_REGEX = '^(O que é|Prevenção|Sintomas|Transmissão|Suspeita|Fake news|Telefones)$'
CHOOSING = 0
reply_keyboard = [['O que é', 'Prevenção'],
                    ['Sintomas', 'Transmissão'],
                    ['Suspeita', 'Fake news'],
                    ['Telefones', 'Voltar']]

def start(update, context):
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(
            "Escolha uma das opções abaixo e veja as dicas que eu reuni para você!",
            reply_markup=markup
    )
    return CHOOSING

def regular_choice(update, context):
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(
            "Escolha uma das opções abaixo e veja as dicas que eu reuni para você!\n\n",
            reply_markup=markup
    )
