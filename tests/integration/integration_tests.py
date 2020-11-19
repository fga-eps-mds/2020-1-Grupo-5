import asyncio, pathlib, string, random
from pyrogram import Client
from tgintegration import BotController, Response

def generate_random_str(size):
    characters = string.ascii_lowercase
    random_str = ''.join(random.choice(characters) for _ in range (size))
    return random_str

user_name = generate_random_str(10)
user_email = user_name + '@email.com'

def create_client():
    client = Client('my_account')
    return client

async def run_tests(client: Client):
    current_path = pathlib.Path(__file__).parent.absolute()
    bot_name = open(str(current_path) + '/bot_name.txt', 'r').read()
    controller = BotController(
        peer=bot_name,
        client=client,
    )
    await controller.clear_chat() # limpa o histórico
    await help_test(controller, client) # Testa ajuda
    await signup_test(controller, client) # Testa o cadastro
    await logout_test(controller, client) # Testa o logout
    await login_test(controller, client)  # Testa o login
    await help_test(controller, client)   # Testa ajuda após login
    await info_edit_test(controller, client) # Testa a edição de informações pessoais
    await tips_test(controller, client)   # Testa as dicas
    await logout_test(controller, client) # Logout novamente (Inicio fresco)
    

async def help_test(controller: BotController, client: Client):
    response = await start_conv_test(controller, client)

    async with controller.collect(count=3) as response:
        await client.send_message(controller.peer_id, 'Ajuda')
    assert response.num_messages == 3
    assert 'possui as seguintes funcionalidades' in response.messages[0].text
    assert 'Informações gerais' in response.messages[1].text
    assert 'Para informações mais detalhadas' in response.messages[2].text
    print('Ajuda testada\n')

async def start_conv_test(controller: BotController, client: Client):
    async with controller.collect(count=2) as response:
        await controller.send_command('start') # envia /start
    assert response.num_messages == 2 # 2 mensagens recebidas
    assert 'Bem vindo' in response.messages[0].text # primeira mensagem recebida corretamente
    assert response.messages[1].photo # segunda mensagem é uma foto
    print('Conversa iniciada')
    return response

async def email_test(controller: BotController, client: Client, response: Response):
    response = await response.reply_keyboard.click('Email')
    assert response.num_messages == 1
    print('Inserindo email')

    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, user_email)
    assert response.num_messages == 1
    assert user_email in response.full_text
    print('Email inserido')
    return response

async def password_test(controller: BotController, client: Client, response: Response):
    response = await response.reply_keyboard.click('Senha')
    assert response.num_messages == 1
    print('Inserindo senha')

    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'Senha12345')
    assert response.num_messages == 1
    assert 'Senha12345' in response.full_text
    print('Senha inserida')
    return response

async def signup_test(controller: BotController, client: Client):
    response = await start_conv_test(controller, client)

    response = await response.reply_keyboard.click('Registrar') # clica em Registrar
    assert response.num_messages == 1
    print('Registro iniciado')

    response = await response.reply_keyboard.click('Username')
    assert response.num_messages == 1
    print('Inserindo username')

    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, user_name) # envia uma mensagem contendo o nome de usuário
    assert response.num_messages == 1
    assert user_name in response.full_text
    print('Username inserido')

    response = await email_test(controller, client, response)

    response = await password_test(controller, client, response)

    response = await response.reply_keyboard.click('Raça')
    assert response.num_messages == 1
    print('Escolhendo raça')

    response = await response.reply_keyboard.click('Branco')
    assert response.num_messages == 1
    assert 'Branco' in response.full_text
    print('Raça escolhida')

    response = await response.reply_keyboard.click('Trabalho')
    assert response.num_messages == 1
    print('Escolhendo trabalho')

    response = await response.reply_keyboard.click('Sim')
    assert response.num_messages == 1
    assert 'Sim' in response.full_text
    print('Trabalho escolhido')

    response = await response.reply_keyboard.click('Genero sexual')
    assert response.num_messages == 1
    print('Escolhendo gênero')

    response = await response.reply_keyboard.click('Homem Cis')
    assert response.num_messages == 1
    assert 'Homem Cis' in response.full_text
    print('Gênero escolhido')

    response = await response.reply_keyboard.click('Localização')
    assert response.num_messages == 1
    print('Enviando localização')

    async with controller.collect(count=1) as response:
        await client.send_location(controller.peer_id, 51.500729, -0.124583) # envia uma localização
    assert response.num_messages == 1
    assert 'England' in response.full_text
    assert 'City of Westminster' in response.full_text
    assert 'United Kingdom' in response.full_text
    print('Localização enviada')

    async with controller.collect(count=2) as resp:
        await response.reply_keyboard.click('Done')
    assert resp.num_messages == 2
    print('Done clicado')

    print('Selecionando data de nascimento')
    async with controller.collect(count=9) as response:
        inline_keyboard = resp.inline_keyboards[0]
        inline_keyboard = (await inline_keyboard.click('<<')).inline_keyboards[0]
        inline_keyboard = (await inline_keyboard.click('<<')).inline_keyboards[0]
        inline_keyboard = (await inline_keyboard.click('1998')).inline_keyboards[0]
        inline_keyboard = (await inline_keyboard.click('Abril')).inline_keyboards[0]
        await inline_keyboard.click('10')

    assert response.num_messages == 9
    assert '1998-04-10' in response.messages[4].text
    assert 'você foi cadastrado com sucesso' in response.messages[5].text
    print('Data de nascimento selecionada')
    print('Registro concluído\n')

async def logout_test(controller: BotController, client: Client):
    response = await start_conv_test(controller, client)

    async with controller.collect(count = 2) as resp:
        await response.reply_keyboard.click('Logout')
    assert 'Até a próxima' in resp.messages[0].text
    print('Logout concluído\n')

async def login_test(controller: BotController, client: Client):
    response = await start_conv_test(controller, client)

    response = await response.reply_keyboard.click('Login')
    assert response.num_messages == 1
    print('Iniciando login')

    response = await email_test(controller, client, response)

    response = await password_test(controller, client, response)

    async with controller.collect(count=3) as resp:
        await response.reply_keyboard.click('Done')
    assert resp.num_messages == 3
    assert 'seja bem vindo' in resp.messages[0].text
    assert resp.messages[1].photo
    print('Login concluído\n')
    
async def tips_test(controller: BotController, client: Client):
    menu = await start_conv_test(controller, client)

    menu = await menu.reply_keyboard.click('Dicas')  # clica em Dicas 
    assert menu.num_messages == 1
    assert 'as informações que reuni' in menu.messages[0].text
    print('Dicas iniciado')
   
    print('(O que é) apertado')
    async with controller.collect(count=2) as response:
        await menu.reply_keyboard.click('O que é')  # clica em O que é
    assert response.num_messages == 2
    assert 'Em dezembro de 2019 foi' in response.messages[0].text

    print('Prevenção apertado')
    async with controller.collect(count=2) as response:
        await menu.reply_keyboard.click('Prevenção')  # clica em Prevenção
    assert response.num_messages == 2
    assert 'Higiene ambiental:' in response.messages[0].text

    print('Sintomas apertado')
    async with controller.collect(count=2) as response:
        await menu.reply_keyboard.click('Sintomas')  # clica em Sintomas
    assert response.num_messages == 2
    assert 'Distúrbios gastrintestinais' in response.messages[0].text

    print('Transmissão apertado')
    async with controller.collect(count=2) as response:
        await menu.reply_keyboard.click('Transmissão')  # clica em Transmissão
    assert response.num_messages == 2
    assert 'A transmissão pode ocorrer de uma' in response.messages[0].text

    print('Suspeita apertado')
    async with controller.collect(count=2) as response:
        await menu.reply_keyboard.click('Suspeita')  # clica em Suspeita
    assert response.num_messages == 2
    assert 'postos de triagem nas Unidades Básicas' in response.messages[0].text

    print('(Fake news) apertado')
    async with controller.collect(count=2) as response:
        await menu.reply_keyboard.click('Fake news')  # clica em Fake news
    assert response.num_messages == 2
    assert 'Science Translational Medicine' in response.messages[0].text
    
    print('Telefones apertado')
    async with controller.collect(count=2) as response:
        await menu.reply_keyboard.click('Telefones')  # clica em Telefones
    assert response.num_messages == 2
    assert 'Defesa Civil' in response.messages[0].text

    print('Fontes apertado')
    async with controller.collect(count=2) as response:
        await menu.reply_keyboard.click('Fontes')  # clica em Fontes
    assert response.num_messages == 2
    assert '- BBC News' in response.messages[0].text

    print('Voltando ao menu inicial')
    async with controller.collect(count=2) as response:
        await menu.reply_keyboard.click('Voltar')  # clica em Voltar
    assert response.num_messages == 2
    assert 'Cancelando' in response.messages[0].text

    print('Dicas testado com sucesso\n')

async def info_edit_test(controller: BotController, client: Client):
    response = await start_conv_test(controller, client)

    print('Mostrando Informações')
    async with controller.collect(count=1) as info:
        await client.send_message(controller.peer_id, 'Minhas informações')
    assert info.num_messages == 1
    assert info.messages[0].photo

    print('Editando Perfil')
    response = await response.reply_keyboard.click('Editar perfil')
    assert response.num_messages == 1
    
    # Username
    response = await response.reply_keyboard.click('Username')
    print('Inserindo Username válido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "OutroUserName")
    assert response.num_messages == 2
    assert 'sucesso' in response.messages[0].text
    print('Username aceito')
    response = await response.reply_keyboard.click('Username')
    print('Inserindo Username inválido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Mini")
    assert response.num_messages == 2
    assert 'Entrada inválida' in response.messages[0].text
    print('Username recusado')

    # Raça
    response = await response.reply_keyboard.click('Raça')
    print('Inserindo Raça válida')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Branco")
    assert response.num_messages == 2
    assert 'sucesso' in response.messages[0].text
    print('Raça aceita')
    response = await response.reply_keyboard.click('Raça')
    print('Inserindo Raça inválida')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Branquo")
    assert response.num_messages == 2
    assert 'Entrada inválida' in response.messages[0].text
    print('Raça recusada')

    # Genero sexual
    response = await response.reply_keyboard.click('Genero sexual')
    print('Inserindo Genero sexual válido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Homem Cis")
    assert response.num_messages == 2
    assert 'sucesso' in response.messages[0].text
    print('Genero sexual aceito')
    response = await response.reply_keyboard.click('Genero sexual')
    print('Inserindo Genero sexual inválido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Inval")
    assert response.num_messages == 2
    assert 'Entrada inválida' in response.messages[0].text
    print('Genero sexual recusado')

    # Trabalho
    response = await response.reply_keyboard.click('Trabalho')
    print('Inserindo Trabalho válido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Não")
    assert response.num_messages == 2
    assert 'sucesso' in response.messages[0].text
    print('Trabalho aceito')
    response = await response.reply_keyboard.click('Trabalho')
    print('Inserindo Trabalho inválido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Siim")
    assert response.num_messages == 2
    assert 'Entrada inválida' in response.messages[0].text
    print('Trabalho recusado')

    # Grupo de Risco
    response = await response.reply_keyboard.click('Grupo de Risco')
    print('Inserindo Grupo de Risco válido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Não")
    assert response.num_messages == 2
    assert 'sucesso' in response.messages[0].text
    print('Grupo de Risco aceito')
    response = await response.reply_keyboard.click('Grupo de Risco')
    print('Inserindo Grupo de Risco inválido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Siim")
    assert response.num_messages == 2
    assert 'Entrada inválida' in response.messages[0].text
    print('Grupo de Risco recusado')

    # Data de Nascimento
    async with controller.collect(count=2) as resp:
        await response.reply_keyboard.click('Nascimento')
    assert resp.num_messages == 2
    print('Data de nascimento válida')
    async with controller.collect(count=6) as info:
        inline_keyboard = resp.inline_keyboards[0]
        inline_keyboard = (await inline_keyboard.click('<<')).inline_keyboards[0]
        inline_keyboard = (await inline_keyboard.click('<<')).inline_keyboards[0]
        inline_keyboard = (await inline_keyboard.click('1998')).inline_keyboards[0]
        inline_keyboard = (await inline_keyboard.click('Abril')).inline_keyboards[0]
        await inline_keyboard.click('10')
    assert info.num_messages == 6
    assert 'sucesso' in info.messages[5].text
    print('Data de nascimento aceita')
    async with controller.collect(count=2) as info:
        await response.reply_keyboard.click('Nascimento')
    assert info.num_messages == 2
    print('Data de nascimento inválida')
    async with controller.collect(count=2) as info:
        await client.send_message(controller.peer_id, "Siim")
    assert info.num_messages == 2
    assert 'inválida' in info.messages[0].text
    print('Data de nascimento recusada')

    # Informações
    print('Mostrando Informações')
    async with controller.collect(count=1) as info:
        await client.send_message(controller.peer_id, 'Mostrar informações')
    assert info.num_messages == 1
    assert info.messages[0].photo

    # Voltando
    print('Voltando ao menu inicial')
    response = await response.reply_keyboard.click('Voltar')
    print('Editar Perfil testado com sucesso\n')


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(run_tests(create_client()))
