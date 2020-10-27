from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

ENTRY_REGEX = '^(O que é|Prevenção|Sintomas|Transmissão|Suspeita|Fake news|Telefones|Locais|Fontes)$'
CHOOSING = 0
reply_keyboard = [['O que é', 'Prevenção'],
                    ['Sintomas', 'Transmissão'],
                    ['Suspeita', 'Fake news'],
                    ['Telefones', 'Locais'],
					['Fontes', 'Voltar']]

def start(update, context):
    defaultReply(update, context)
    return CHOOSING


def defaultReply(update, context):
	markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
	update.message.reply_text(
        "Escolha uma das opções abaixo e veja as informações que reuni para você!",
        reply_markup=markup
    )


def regular_choice(update, context):
	text = update.message.text

	if 'O que é' in text:
		about(update, context)
	elif 'Prevenção' in text:
		prevention(update, context)
	elif 'Sintomas' in text:
		symptoms(update, context)
	elif 'Fake news' in text:
		fake_news(update, context)
	elif 'Telefones' in text:
		phone_numbers(update, context)
	elif 'Transmissão' in text:
		transmission(update, context)
	elif 'Suspeita' in text:
		suspected(update, context)
	elif 'Locais' in text:
		locations(update, context)
	elif 'Fontes' in text:
		sources(update, context)

	defaultReply(update, context)


def about(update, context):
    text = ('Os coronavírus são uma família de vírus comuns em várias espécies de animais. Esses vírus que infectam animais podem raramente infectar pessoas, como é o caso do <b>SARS-CoV</b>. '
            'Em dezembro de 2019 foi identificado em <b>Wuhan, na China</b>, a transmissão de um novo coronavírus (<b>SARS-CoV-2</b>), causador da <b>COVID-19</b>. Em seguida a doença foi transmitida de pessoa para pessoa.\n\n'
            'A <b>COVID-19</b> pode variar de infecções assintomáticas a quadros graves. Segundo a <b>Organização Mundial de Saúde</b>, cerca de 80% dos pacientes com a doença podem ser assintomáticos ou apresentar poucos sintomas, '
            'e cerca de 20% requer atendimento hospitalar por dificuldade respiratória. Desses, 5% podem precisar de suporte ventilatório.')
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
		parse_mode=ParseMode.HTML
    )


def symptoms(update, context):
    text = ('Os sintomas vão desde um resfriado ou uma síndrome gripal até uma pneumonia severa.\n\n<b>Os sintomas mais comuns são:</b>\n'
            '- Tosse\n- Febre\n- Coriza\n- Dor de garganta\n- Dificuldade para respirar\n- Perda de olfato\n- Alteração do paladar\n- Distúrbios gastrintestinais\n'
            '- Cansaço\n- Diminuição de apetite\n- Falta de ar')
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
		parse_mode=ParseMode.HTML
    )


def prevention(update, context):
	text = ('Aqui você encontra informações sobre prevenção de agravos, diagnósticos, tratamentos, reabilitação e a manutenção da saúde. O Ministério da Saúde aconselha a população a tomar medidas preventivas de eficácia comprovada:\n\n'
			'<b>Higiene pessoal:</b>\n\n'
			'- Higienizar as mãos com água e sabão, ou com álcool gel, principalmente depois de tossir ou espirrar; de usar o banheiro; antes de comer, antes e depois de tocar os olhos, a boca e o nariz\n'
			'- Evitar tocar os olhos, nariz ou boca após contato com superfícies potencialmente contaminadas, como corrimãos, bancos e maçanetas\n'
			'- Evitar proteger a tosse e o espirro com as mãos, utilizando, preferencialmente, lenço de papel descartável\n'
			'- Evitar contato com pessoas apresentem a síndrome gripa\n'
			'- Assegurar que sua família esteja com a carteira de vacinação atualizada\n\n'
			'<b>Higiene do alimentos:</b>\n\n'
			'- Lavar bem frutas e verduras com água limpa e deixar de molho por alguns minutos em vinagre (1 colher por litro de água) ou hipoclorito de sódio (3 gotas por litro de água)\n'
			'- Cobrir os alimentos para evitar que insetos entrem em contato\n'
			'- Evitar compartilhar qualquer objeto que seja levado à boca\n\n'
			'<b>Higiene ambiental:</b>\n\n'
			'- Manter o quintal sempre limpo, roçando a grama/capim e podando as árvores\n'
			'- Não jogar lixo no quintal. Acondicionar o lixo doméstico e colocar na frente da casa próximo aos horários de coleta, para evitar a presença de animais, como insetos e ratos\n'
			'- Não queimar lixo\n'
			'- Limpar e desinfetar superfícies regularmente\n'
			'- Não fumar dentro de casa\n'
			'- Eliminar possíveis criadouros de vetores de doenças\n'
			'- Se não houver rede de esgoto na região, os banheiros devem ser construídos longe de poços d\'água, de nascentes ou da beira do rio')
	context.bot.send_message(
		chat_id=update.effective_chat.id,
		text = text,
		parse_mode=ParseMode.HTML
	)

def fake_news(update, context):
	text = ('Para evitar informações falsas se atente ao seguinte:\n\n'
			'- Não se baseie somente pelo título, leia sempre a notícia inteira\n'
			'- Veja sempre a autoria e as referências da notícia\n'
			'- Pesquise o título da notícia\n'
			'- Tente buscar trechos da notícia separadamente\n'
			'- Se for uma imagem, tente uma busca reversa\n'
			'- Para áudios e vídeos, busque por palavras chave e tente encontrar a fonte\n'
			'- Se uma pessoa te enviou, pergunte a ela sobre as fontes\n'
			'- Sobre a covid-19 os seguintes sites possuem informação confiável:\n\n'
			'  <b>1.</b>Ministério da Saúde\n'
			'  <b>2.</b>Conselho Nacional de Secretarias de Saúde\n'
			'  <b>3.</b>OPAS/OMS Brasil\n'	
			'  <b>4.</b>Anvisa\n'
			'  <b>5.</b>INCA\n'
			'  <b>6.</b>Fiocruz\n'
			'  <b>7.</b><i>Science Traslational Medicine</i>')
	context.bot.send_message(
		chat_id=update.effective_chat.id,
		text = text,
		parse_mode=ParseMode.HTML
	)

def phone_numbers(update, context):
	text = ('Lista de telefones úteis:\n\n'
			'- Disque Saúde do Ministério da Saúde:\n<b>(136)</b>\n'
			'- Corpo de Bombeiros:\n<b>(193)</b>\n'
			'- SAMU:\n<b>(192)</b>\n'
			'- Polícia Militar:\n<b>(190)</b>\n'			
			'- Polícia Rodoviária Federal:\n<b>(191)</b>\n'
			'- Poiícia Rodoviária Estadual:\n<b>(198)</b>\n'
			'- Defesa Civil:\n<b>(199)</b>')
	context.bot.send_message(
		chat_id=update.effective_chat.id,
		text = text,
		parse_mode=ParseMode.HTML
	)

def transmission(update, context):
	text = ('<b>A transmissão pode ocorrer de uma pessoa com a doença para outra ou por meio de contato próximo como:</b> aperto de mãos contaminadas, '
			'gotículas de saliva, espirro, tosse, catarro ou objetos e superfícies contaminadas, incluindo celulares, mesas, '
			'talheres, maçanetas, brinquedos e teclados de computador.')
	context.bot.send_message(
		chat_id=update.effective_chat.id,
		text = text,
		parse_mode=ParseMode.HTML
	)

def suspected(update, context):
	text = ('<b>Se estiver doente, com sintomas compatíveis com a COVID-19, como febre, tosse, dor de garganta e/ou coriza, com ou sem falta de ar:</b>\n\n'
			'- Evite contato físico com outras pessoas, principalmente idosos e doentes crônicos.\n'
			'- <b>Procure imediatamente os postos de triagem nas Unidades Básicas de Saúde / UPAS ou outras unidades de saúde.</b> Após encaminhamento consulte-se com o médico.\n'
			'- Uma vez diagnosticado pelo médico, receba as orientações e prescrição dos medicamentos que você deverá usar.\n'
			'- Mantenha seu médico sempre informado da evolução dos sintomas durante o tratamento e siga suas recomendações.\n'
			'- Utilize máscara o tempo todo.\n'
			'- Se precisar cozinhar utilize máscara de proteção, cobrindo boca e nariz o tempo todo.\n'
			'- Separe toalhas, talheres, copos e outros objetos apenas para seu uso.\n'
			'- O lixo produzido pela pessoa com suspeita ou já diagnosticada precisa ser separado e descartado.\n'
			'- Evite o compartilhamento de sofás e cadeiras e faça a limpeza frequentemente com água sanitária, álcool 70% ou outro produto recomendado pela Anvisa.\n'
			'- Se o paciente não mora sozinho é recomendado que os demais moradores da residência durmam em outro cômodo e mantenham a distância mínima de 1 metro da pessoa infectada.')
	context.bot.send_message(
		chat_id=update.effective_chat.id,
		text = text,
		parse_mode=ParseMode.HTML
	)

def locations(update, context):
	context.bot.send_message(
    	text='Clique em um botão abaixo e encontre locais próximos no <i>Google Maps</i>:',
    	reply_markup=InlineKeyboardMarkup([
        	[InlineKeyboardButton(text='Fármacias', url='https://www.google.com.br/maps/search/farmacias')],
	        [InlineKeyboardButton(text='Hospitais', url='https://www.google.com.br/maps/search/hospitais')],
    	]),
		chat_id=update.effective_chat.id,
		parse_mode=ParseMode.HTML
	)

def sources(update, context):
	text = ('As informações foram obtidas das seguintes fontes:\n'
			'- <a href="https://play.google.com/store/apps/details?id=com.guardioesapp&hl=pt_BR">Guardiões da Saúde</a>\n'
			'- <a href="https://coronavirus.saude.gov.br/">Ministério da Saúde</a>'
			)
	context.bot.send_message(
		chat_id=update.effective_chat.id,
		text = text,
		parse_mode=ParseMode.HTML,
		disable_web_page_preview=True
	)
