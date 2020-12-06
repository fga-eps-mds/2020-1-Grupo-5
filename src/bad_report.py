from telegram import ReplyKeyboardMarkup, KeyboardButton
from requests import post
from src import utils, handlers, daily_report

CHOOSING = 0

sintomas = ['Dor de cabeça', 'Bolhas na Pele', 'Mal-estar', 'Congestão Nasal', 'Náuseas', 'Diarréia', 'Dificuldade de respirar', 'Olhos vermelhos', 'Dor nas Articulações',
            'Febre', 'Tosse', 'Dor no Estômago', 'Dor nos Músculos', 'Sangramentos', 'Dor nos Olhos', 'Calafrios', 'Vômito', 'Pele e olhos avermelhados', 'Manchas vermelhas no corpo']

location_button = KeyboardButton('Done', request_location=True)

markup = ReplyKeyboardMarkup([  ['Dor de cabeça', 'Bolhas na Pele', 'Mal-estar'],
                                ['Congestão Nasal', 'Náuseas', 'Diarréia'],
                                ['Dificuldade de respirar', 'Olhos vermelhos', 'Dor nas Articulações'],
                                ['Febre', 'Tosse', 'Dor no Estômago'],
                                ['Dor nos Músculos', 'Sangramentos', 'Dor nos Olhos'],
                                ['Calafrios', 'Vômito', 'Pele e olhos avermelhados'],
                                ['Manchas vermelhas no corpo'],
                                [location_button]   ],
                                resize_keyboard=True,
                                one_time_keyboard=True
                            )

def start(update, context):
    update.callback_query.answer()
    context.user_data['Symptoms'] = list()

    update.callback_query.edit_message_text("Obrigado por nos informar!")
    context.bot.send_message(
        text='Selecione os sintomas que sentiu nas últimas 24 horas!',
        chat_id=update.effective_chat.id,
        reply_markup=markup
    )

    return CHOOSING

def regular_choice(update, context):
    message = update.message.text

    if message in sintomas and not message in context.user_data['Symptoms']:
        context.user_data['Symptoms'].append(update.message.text)

    string = utils.list_to_str(context.user_data['Symptoms'])
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{string}\nSelecione os sintomas que sentiu, lembrando que é necessário nos fornecer sua localização antes de enviar.",
        reply_markup=markup
    )

    return CHOOSING

def done(update, context):
    headers =  {'Accept' : 'application/vnd.api+json', 'Content-Type' : 'application/json', 'Authorization' : str(context.user_data['AUTH_TOKEN'])}
    json_entry = {
        "survey" : {
                "symptom": context.user_data['Symptoms'],
                "latitude": update.message.location.latitude,
                "longitude": update.message.location.longitude,
        }
    }
    url = f"http://localhost:3001/users/{context.user_data['id']}/surveys"
    r = post(headers=headers, json=json_entry, url=url)

    if r.status_code == 201:
        resposta = "Obrigado por nos informar o seu estado de saúde.\n\nEsperamos que tudo fique bem, mantenha-se sempre hidratado e isolado.\n\nImportante lembrar que caso precise de alguma ajuda, temos o botão de ajuda no menu abaixo."
    else:
        resposta = "Algo deu errado. Lembre-se que só pode reportar seu estado de saúde uma vez por dia."

    context.bot.send_message(
        chat_id= update.effective_chat.id,
        text = resposta
    )

    context.user_data.pop('Symptoms', None)

    handlers.menu(update, context)

    daily_report.reported_chat_ids.add(update.effective_chat.id)

    return -1 # END
