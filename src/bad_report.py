from telegram import ReplyKeyboardMarkup

CHOOSING = 0

sintomas = ['Febre', 'Falta de ar', 'Dor de cabeça', 'Alteração de Paladar e Olfato', 'Bolhas na Pele',
'Calafrios', 'Cansaço', 'Coceira', 'Congestão Nasal','Dor de Garganta', 'Dor nos Músculos','Dor nos olhos',
'Tosse', 'Mal-estar', 'Náuse ou Vômito']

markup = ReplyKeyboardMarkup([['Febre', 'Falta de Ar', 'Dor de Cabeça'],
                              ['Alteração de Paladar e Olfato', 'Bolhas na Pele'],
                               ['Calafrios', 'Cansaço', 'Coceira'],
                               ['Congestão Nasal','Dor de Garganta'],
                               ['Dor nos Músculos','Dor nos olhos'],
                               ['Tosse', 'Mal-estar', 'Náuse ou Vômito'],
                               ['Done']],
        resize_keyboard=True,
        one_time_keyboard=True)

def start(update, context):

    update.callback_query.edit_message_text(
        "Obrigado por nos informar!"
        )

    context.bot.send_message(
        text='Selecione os sintomas que sentiu nas últimas 24 horas!',
        chat_id=update.effective_chat.id,
        reply_markup=markup
    )

    return CHOOSING


def regular_choice(update, context):
    actual_symptoms = list()

    if context.user_data.get('Symptoms'):
        print(context.user_data.get('Symptoms'))
        actual_symptoms = list(context.user_data['Symptoms'])
    
    if(update.message.text in sintomas):
        if actual_symptoms:
            actual_symptoms.append(update.message.text)
            context.user_data['Symptoms'] = actual_symptoms

        else:
            context.user_data['Symptoms'] = update.message.text  

    
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{context.user_data['Symptoms']}, selecione mais sintomas abaixo.",
        reply_markup=markup
    )

    return CHOOSING

def done(update, context):
    print("Done")   

    return -1 # END

def cancel(update, context):
    print("Voltar")

    return -1 # END

def bad_entry(update, context):
    print('Bad_entry')
    
    return -1 # END