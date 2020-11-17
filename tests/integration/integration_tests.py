import asyncio, pathlib
from pyrogram import Client
from tgintegration import BotController, Response

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
    await signup_test(controller, client) # Testa o cadastro
    await logout_test(controller, client) # Testa o logout (Inicio fresco para outros testes)
    await login_test(controller, client)  # Testa o login
    await tips_test(controller, client)   # Testa as dicas

async def signup_test(controller: BotController, client: Client):
    async with controller.collect(count=2) as response:
        await controller.send_command('start') # envia /start
    assert response.num_messages == 2 # 2 mensagens recebidas
    assert response.messages[1].photo # segunda mensagem é uma foto
    print('Conversa iniciada')

    response = await response.reply_keyboard.click('Registrar') # clica em Registrar
    assert response.num_messages == 1
    print('Registro iniciado')

    response = await response.reply_keyboard.click('Username')
    assert response.num_messages == 1
    print('Inserindo username')

    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'Usuario Teste') # envia uma mensagem contendo o nome de usuário
    assert response.num_messages == 1
    print('Username inserido')

    response = await response.reply_keyboard.click('Email')
    assert response.num_messages == 1
    print('Inserindo email')

    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'emailteste@teste.com')
    assert response.num_messages == 1
    print('Email inserido')

    response = await response.reply_keyboard.click('Senha')
    assert response.num_messages == 1
    print('Inserindo senha')

    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'Senha12345')
    assert response.num_messages == 1
    print('Senha inserida')

    response = await response.reply_keyboard.click('Raça')
    assert response.num_messages == 1
    print('Escolhendo raça')

    response = await response.reply_keyboard.click('Branco')
    assert response.num_messages == 1
    print('Raça escolhida')

    response = await response.reply_keyboard.click('Trabalho')
    assert response.num_messages == 1
    print('Escolhendo trabalho')

    response = await response.reply_keyboard.click('Sim')
    assert response.num_messages == 1
    print('Trabalho escolhido')

    response = await response.reply_keyboard.click('Genero sexual')
    assert response.num_messages == 1
    print('Escolhendo gênero')

    response = await response.reply_keyboard.click('Homem Cis')
    assert response.num_messages == 1
    print('Gênero escolhido')

    response = await response.reply_keyboard.click('Localização')
    assert response.num_messages == 1
    print('Enviando localização')

    async with controller.collect(count=1) as response:
        await client.send_location(controller.peer_id, 51.500729, -0.124583) # envia uma localização
    assert response.num_messages == 1
    print('Localização enviada')

    async with controller.collect(count=2) as resp:
        await response.reply_keyboard.click('Done')
    assert resp.num_messages == 2
    print('Done clicado')

    async with controller.collect(count=9) as response:
        inline_keyboard = resp.inline_keyboards[0]
        inline_keyboard = (await inline_keyboard.click('<<')).inline_keyboards[0]
        inline_keyboard = (await inline_keyboard.click('<<')).inline_keyboards[0]
        inline_keyboard = (await inline_keyboard.click('1998')).inline_keyboards[0]
        inline_keyboard = (await inline_keyboard.click('Abril')).inline_keyboards[0]
        await inline_keyboard.click('10')
    print('Data de nascimento selecionada')

    assert response.num_messages == 9
    assert 'você foi cadastrado com sucesso' in response.messages[5].text
    print('Cadastro concluído')

async def logout_test(controller: BotController, client: Client):
    async with controller.collect(count=2) as response:
        await controller.send_command('start') # envia /start
    assert response.num_messages == 2 # 2 mensagens recebidas
    assert response.messages[1].photo # segunda mensagem é uma foto
    print('Logout iniciado')

    async with controller.collect(count = 2) as resp:
        await response.reply_keyboard.click('Logout')
    assert 'Até a próxima' in resp.messages[0].text
    print('Logout concluído')

async def login_test(controller: BotController, client: Client):
    async with controller.collect(count=2) as response:
        await controller.send_command('start') # envia /start
    assert response.num_messages == 2 # 2 mensagens recebidas
    assert response.messages[1].photo

    response = await response.reply_keyboard.click('Login')
    assert response.num_messages == 1
    print('Iniciando login')

    response = await response.reply_keyboard.click('Email')
    assert response.num_messages == 1
    print('Inserindo email')

    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'emailteste@teste.com')
    assert response.num_messages == 1
    print('Email inserido')

    response = await response.reply_keyboard.click('Senha')
    assert response.num_messages == 1
    print('Inserindo senha')

    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'Senha12345')
    assert response.num_messages == 1
    print('Senha inserida')

    async with controller.collect(count=3) as resp:
        await response.reply_keyboard.click('Done')
    assert resp.num_messages == 3
    assert 'seja bem vindo' in resp.messages[0].text
    assert resp.messages[1].photo
    print('Login concluído')
    
async def tips_test(controller: BotController, client: Client):
    async with controller.collect(count=2) as menu:
        await controller.send_command('start') # envia /start
    assert menu.num_messages == 2

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

    print('Dicas testado com sucesso')

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(run_tests(create_client()))
