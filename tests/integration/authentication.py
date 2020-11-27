import asyncio, string, random, pathlib
from pyrogram import Client
from tgintegration import BotController, Response

def generate_random_str(size):
    characters = string.ascii_lowercase
    random_str = ''.join(random.choice(characters) for _ in range (size))
    return random_str

user_name = generate_random_str(10)
user_email = user_name + '@email.com'

async def run_tests(client: Client):
    current_path = pathlib.Path(__file__).parent.absolute()
    bot_name = open(str(current_path) + '/bot_name.txt', 'r').read()
    controller = BotController(
        peer=bot_name,
        client=client,
    )

    await signup_test(controller, client)
    await logout_test(controller)
    await login_test(controller, client)

async def test_username(controller: BotController, client: Client, response: Response):
    resp = await response.reply_keyboard.click('Username')
    assert resp.num_messages == 1
    print('Inserindo username')

    async with controller.collect(count=1) as resp:
        await client.send_message(controller.peer_id, user_name)
    assert resp.num_messages == 1
    assert user_name in resp.full_text
    print('Username validado')

    return resp

async def test_invalid_username(controller: BotController, client: Client, response: Response):
    resp = await response.reply_keyboard.click('Username')
    assert resp.num_messages == 1
    print('Inserindo username inválido')

    async with controller.collect(count=1) as resp:
        await client.send_message(controller.peer_id, 'wrong')
    assert resp.num_messages == 1
    assert 'wrong' not in resp.full_text
    print('Username invalidado')

    return resp

async def test_email(controller: BotController, client: Client, response: Response):
    resp = await response.reply_keyboard.click('Email')
    assert resp.num_messages == 1
    print('Inserindo email')

    async with controller.collect(count=1) as resp:
        await client.send_message(controller.peer_id, user_email)
    assert resp.num_messages == 1
    assert user_email in resp.full_text
    print('Email validado')

    return resp

async def test_invalid_email(controller: BotController, client: Client, response: Response):
    resp = await response.reply_keyboard.click('Email')
    assert resp.num_messages == 1
    print('Inserindo email inválido')

    async with controller.collect(count=1) as resp:
        await client.send_message(controller.peer_id, 'emailinvalido')
    assert resp.num_messages == 1
    assert 'emailinvalido' not in resp.full_text
    print('Email invalidado')

    return resp

async def test_password(controller: BotController, client: Client, response: Response):
    resp = await response.reply_keyboard.click('Senha')
    assert resp.num_messages == 1
    print('Inserindo senha')

    async with controller.collect(count=1) as resp:
        await client.send_message(controller.peer_id, 'Senha12345')
    assert resp.num_messages == 1
    assert 'Senha12345' in resp.full_text
    print('Senha validada')

    return resp

async def test_invalid_password(controller: BotController, client: Client, response: Response):
    resp = await response.reply_keyboard.click('Senha')
    assert resp.num_messages == 1
    print('Inserindo senha inválida')

    async with controller.collect(count=1) as resp:
        await client.send_message(controller.peer_id, 'pass12')
    assert resp.num_messages == 1
    assert 'pass12' not in resp.full_text
    print('Senha invalidada')

    return resp

async def test_race(response: Response):
    resp = await response.reply_keyboard.click('Raça')
    assert resp.num_messages == 1
    print('Escolhendo raça')

    resp_1 = await resp.reply_keyboard.click('Branco')
    assert resp_1.num_messages == 1
    assert 'Branco' in resp_1.full_text
    print('Raça validada')

    return resp_1

async def test_invalid_race(controller: BotController, client: Client, response: Response):
    resp = await response.reply_keyboard.click('Raça')
    assert resp.num_messages == 1
    print('Escolhendo raça inválida')

    async with controller.collect(count=1) as resp:
        await client.send_message(controller.peer_id, 'invalid')
    assert resp.num_messages == 1
    assert 'invalid' not in resp.full_text
    print('Raça invalidada')

    return resp

async def test_job(response: Response):
    resp = await response.reply_keyboard.click('Trabalho')
    assert resp.num_messages == 1
    print('Escolhendo trabalho')

    resp_1 = await resp.reply_keyboard.click('Sim')
    assert resp_1.num_messages == 1
    assert 'Sim' in resp_1.full_text
    print('Trabalho validado')

    return resp_1

async def test_invalid_job(controller: BotController, client: Client, response: Response):
    resp = await response.reply_keyboard.click('Trabalho')
    assert resp.num_messages == 1
    print('Escolhendo trabalho inválido')

    async with controller.collect(count=1) as resp:
        await client.send_message(controller.peer_id, 'invalid')
    assert resp.num_messages == 1
    assert 'invalid' not in resp.full_text
    print('Trabalho invalidado')

    return resp

async def test_gender(response: Response):
    resp = await response.reply_keyboard.click('Genero sexual')
    assert resp.num_messages == 1
    print('Escolhendo gênero')

    resp_1 = await resp.reply_keyboard.click('Homem Cis')
    assert resp_1.num_messages == 1
    assert 'Homem Cis' in resp_1.full_text
    print('Gênero validado')

    return resp_1

async def test_invalid_gender(controller: BotController, client: Client, response: Response):
    resp = await response.reply_keyboard.click('Genero sexual')
    assert resp.num_messages == 1
    print('Escolhendo gênero inválido')

    async with controller.collect(count=1) as resp:
        await client.send_message(controller.peer_id, 'invalid')
    assert resp.num_messages == 1
    assert 'invalid' not in resp.full_text
    print('Gênero invalidado')

    return resp

async def test_location(controller: BotController, client: Client, response: Response):
    resp = await response.reply_keyboard.click('Localização')
    assert resp.num_messages == 1
    print('Enviando localização')

    async with controller.collect(count=1) as resp:
        await client.send_location(controller.peer_id, 51.500729, -0.124583)
    assert resp.num_messages == 1
    assert 'England' in resp.full_text
    assert 'City of Westminster' in resp.full_text
    assert 'United Kingdom' in resp.full_text
    print('Localização enviada')

    return resp

async def click_signup_done(controller: BotController, client: Client, response: Response):
    async with controller.collect(count=2) as resp:
        await response.reply_keyboard.click('Done')
    assert resp.num_messages == 2
    print('Done clicado')

    return resp

async def select_birthdate(controller: BotController, client: Client, resp: Response):
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

    return response

async def click_signup(response: Response):
    resp = await response.reply_keyboard.click('Registrar')
    assert resp.num_messages == 1
    print('Registro iniciado')

    return resp

async def signup_test(controller: BotController, client: Client):
    async with controller.collect(count=1) as response:
        await controller.send_command('menu')
    resp = await click_signup(response)
    response = await test_invalid_username(controller, client, resp)
    resp = await test_username(controller, client, response)
    response = await test_invalid_email(controller, client, resp)
    resp = await test_email(controller, client, response)
    response = await test_invalid_password(controller, client, resp)
    resp = await test_password(controller, client, response)
    response = await test_invalid_race(controller, client, resp)
    resp = await test_race(response)
    response = await test_invalid_job(controller, client, resp)
    resp = await test_job(response)
    response = await test_location(controller, client, resp)
    resp = await test_gender(response)
    response = await test_invalid_gender(controller, client, resp)
    resp = await test_gender(response)
    response = await click_signup_done(controller, client, resp)
    await select_birthdate(controller, client, response)
    print('Registro concluído\n')

async def click_login(response: Response):
    resp = await response.reply_keyboard.click('Login')
    assert resp.num_messages == 1
    print('Iniciando login')

    return resp

async def click_login_done(controller: BotController, response: Response):
    async with controller.collect(count=3) as resp:
        await response.reply_keyboard.click('Done')
    assert resp.num_messages == 3
    assert 'seja bem vindo' in resp.messages[0].text
    assert resp.messages[1].photo

    return resp

async def login_test(controller: BotController, client: Client):
    async with controller.collect(count=1) as response:
        await controller.send_command('menu')
    resp = await click_login(response)
    response = await test_invalid_email(controller, client, resp)
    resp = await test_email(controller, client, response)
    response = await test_password(controller, client, resp)
    resp = await test_invalid_password(controller, client, response)
    response = await test_password(controller, client, resp)
    resp = await click_login_done(controller, response)
    print('Login concluído\n')

async def click_logout(controller: BotController, response: Response):
    async with controller.collect(count=2) as resp:
        await response.reply_keyboard.click('Logout')
    assert 'Até a próxima' in resp.messages[0].text
    print('Logout clicado')

async def logout_test(controller: BotController):
    async with controller.collect(count=1) as response:
        await controller.send_command('menu')
    await click_logout(controller, response)
    print('Logout concluído\n')

if __name__ == '__main__':
    client = Client('my_account')
    asyncio.get_event_loop().run_until_complete(run_tests(client))
