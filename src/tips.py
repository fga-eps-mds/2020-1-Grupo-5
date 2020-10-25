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
            "Escolha uma das opções abaixo e veja as informações que eu reuni para você!",
            reply_markup=markup
    )
    return CHOOSING


def regular_choice(update, context):
    text = update.message.text

    if 'O que é' in text:
        about(update, context)
    elif 'Sintomas' in text:
        symptoms(update, context)

    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(
            "Escolha uma das opções abaixo e veja as dicas que eu reuni para você!\n\n",
            reply_markup=markup
    )


def about(update, context):
    text = ('Os coronavírus são uma família de vírus comuns em várias espécies de animais. Esses vírus que infectam animais podem raramente infectar pessoas, como é o caso do SARS-CoV. '
            'Em dezembro de 2019 foi identificado em Wuhan, na China, a transmissão de um novo coronavírus (SARS-CoV-2), causador da COVID-19. Em seguida a doença foi transmitida de pessoa para pessoa.\n\n'
            'A COVID-19  pode variar de infecções assintomáticas a quadros graves. Segundo a Organização Mundial de Saúde (OMS), cerca de 80% dos pacientes com a doença podem ser assintomáticos ou apresentar poucos sintomas, '
            'e cerca de 20% requer atendimento hospitalar por dificuldade respiratória. Desses, 5% podem precisar de suporte ventilatório.')
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
    )


def symptoms(update, context):
    text = ('Os sintomas vão desde um resfriado ou uma síndrome gripal até uma pneumonia severa.\n\nOs sintomas mais comuns são:\n'
            '- Tosse\n- Febre\n- Coriza\n- Dor de garganta\n- Dificuldade para respirar\n- Perda de olfato\n- Alteração do paladar\n- Distúrbios gastrintestinais\n'
            '- Cansaço\n- Diminuição de apetite\n- Falta de ar')
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
    )
