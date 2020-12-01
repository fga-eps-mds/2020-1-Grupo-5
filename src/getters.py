from src.CustomCalendar import CustomCalendar
from datetime import date
from telegram import ReplyKeyboardMarkup, KeyboardButton

CHOOSING, TYPING_REPLY = range(2)

race_options = [    ['Branco', 'Negro', 'Pardo'],
                    ['Indigena', 'Amarelo', 'Outro']    ]

gender_options = [  ['Homem Cis', 'Mulher Cis'],
                    ['Homem Homossexual', 'Mulher Homossexual'],
                    ['Outro']   ]

yes_no = [['Sim', 'Não']]

location_markup = ReplyKeyboardMarkup(
                    [[KeyboardButton('Enviar localização', request_location=True)]], 
                    resize_keyboard=True, 
                    one_time_keyboard=True
                )

race_markup = ReplyKeyboardMarkup(race_options, one_time_keyboard=True, resize_keyboard=True)

gender_markup = ReplyKeyboardMarkup(gender_options, one_time_keyboard=True, resize_keyboard=True)

yes_no_markup = ReplyKeyboardMarkup(yes_no, one_time_keyboard=True, resize_keyboard=True)

#Funcao que recebe o usuario
def get_User(update, context):
    text = update.message.text
    context.user_data['choice'] = text
    update.message.reply_text('Digite um nome válido, com mais de 8 caracteres!')

    return TYPING_REPLY

#Funcao que recebe a senha do user
def get_Pass(update, context):
    text = update.message.text
    context.user_data['choice'] = text
    update.message.reply_text('Digite uma senha valida, com pelo menos 8 caracteres!')

    return TYPING_REPLY

#Funcao que recebe a senha do user
def get_Email(update, context):
    text = update.message.text
    context.user_data['choice'] = text
    update.message.reply_text('Digite um email valido!')

    return TYPING_REPLY

#Funcao que recebe a Raça do usuario
def get_Race(update, context):
    text = update.message.text
    context.user_data['choice'] = text
    update.message.reply_text(
        'Selecione sua raça.',
        reply_markup=race_markup
    )

    return CHOOSING

#Funcao que recebe o genero do usuario
def get_Gender(update, context):
    text = update.message.text
    context.user_data['choice'] = text
    update.message.reply_text(
        'Selecione seu genero.',
        reply_markup=gender_markup
    )

    return CHOOSING  
    
#Funcao que recebe o dia de nascimento
def get_birthday(update, context):
    update.message.reply_text('Está quase tudo pronto, basta apenas selecionar sua data de nascimento!')

    calendar, step = CustomCalendar(locale='br', max_date=date.today()).build()
    update.message.reply_text(
        f"Selecione o {CustomCalendar.LSTEP[step]}",
        reply_markup=calendar
    )

    return CHOOSING

#Funcao que recebe o dia de nascimento
def get_birthday_edit(update, context):

    update.message.reply_text('Preencha com a data de nascimento correta.')
    calendar, step = CustomCalendar(locale='br', max_date=date.today()).build()
    update.message.reply_text(
        f"Selecione o {CustomCalendar.LSTEP[step]}",
        reply_markup=calendar
    )

    return CHOOSING

#Funcao que recebe se o usario trabalha ou não
def get_professional(update, context):
    text = update.message.text
    context.user_data['choice'] = text
    update.message.reply_text(
        'Você trabalha?',
        reply_markup=yes_no_markup
    )

    return CHOOSING

def get_location(update, context):
    text = update.message.text
    context.user_data['choice'] = text

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Clique no botão para enviar sua localização', 
        reply_markup=location_markup
    )
    return CHOOSING
    
#Funcao que recebe se o usuario eh do grupo de risco ou n
def get_Risco(update, context):
    text = update.message.text
    context.user_data['choice'] = text
    update.message.reply_text(
        'Você é do Grupo de Risco?',
        reply_markup=yes_no_markup
    )

    return CHOOSING
