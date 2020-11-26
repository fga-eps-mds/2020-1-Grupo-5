import asyncio, string, random
from pyrogram import Client
from tgintegration import BotController, Response
from simple_messages import start_conv_test
import configs

def generate_random_str(size):
    characters = string.ascii_lowercase
    random_str = ''.join(random.choice(characters) for _ in range (size))
    return random_str

user_name = generate_random_str(10)
user_email = user_name + '@email.com'

async def run_tests(controller: BotController, client: Client):
    await signup_test(controller, client)
    await logout_test(controller, client)
    await login_test(controller, client)

async def test_username(controller: BotController, client: Client, response: Response):
    response = await response.reply_keyboard.click('Username')
    assert response.num_messages == 1
    print('Inserindo username')

    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, user_name)
    assert response.num_messages == 1
    assert user_name in response.full_text
    print('Username validado')

    return response

async def test_invalid_username(controller: BotController, client: Client, response: Response):
    response = await response.reply_keyboard.click('Username')
    assert response.num_messages == 1
    print('Inserindo username inválido')

    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'wrong')
    assert response.num_messages == 1
    assert 'wrong' not in response.full_text
    print('Username invalidado')

    return response

async def test_email(controller: BotController, client: Client, response: Response):
    response = await response.reply_keyboard.click('Email')
    assert response.num_messages == 1
    print('Inserindo email')

    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, user_email)
    assert response.num_messages == 1
    assert user_email in response.full_text
    print('Email validado')

    return response

async def test_invalid_email(controller: BotController, client: Client, response: Response):
    response = await response.reply_keyboard.click('Email')
    assert response.num_messages == 1
    print('Inserindo email inválido')

    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'emailinvalido')
    assert response.num_messages == 1
    assert 'emailinvalido' not in response.full_text
    print('Email invalidado')

    return response

async def test_password(controller: BotController, client: Client, response: Response):
    response = await response.reply_keyboard.click('Senha')
    assert response.num_messages == 1
    print('Inserindo senha')

    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'Senha12345')
    assert response.num_messages == 1
    assert 'Senha12345' in response.full_text
    print('Senha validada')

    return response

async def test_invalid_password(controller: BotController, client: Client, response: Response):
    response = await response.reply_keyboard.click('Senha')
    assert response.num_messages == 1
    print('Inserindo senha inválida')

    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'pass12')
    assert response.num_messages == 1
    assert 'pass12' not in response.full_text
    print('Senha invalidada')

    return response

async def test_race(controller: BotController, client: Client, response: Response):
    response = await response.reply_keyboard.click('Raça')
    assert response.num_messages == 1
    print('Escolhendo raça')

    response = await response.reply_keyboard.click('Branco')
    assert response.num_messages == 1
    assert 'Branco' in response.full_text
    print('Raça validada')

    return response

async def test_invalid_race(controller: BotController, client: Client, response: Response):
    response = await response.reply_keyboard.click('Raça')
    assert response.num_messages == 1
    print('Escolhendo raça inválida')

    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'invalid')
    assert response.num_messages == 1
    assert 'invalid' not in response.full_text
    print('Raça invalidada')

    return response

async def test_job(controller: BotController, client: Client, response: Response):
    response = await response.reply_keyboard.click('Trabalho')
    assert response.num_messages == 1
    print('Escolhendo trabalho')

    response = await response.reply_keyboard.click('Sim')
    assert response.num_messages == 1
    assert 'Sim' in response.full_text
    print('Trabalho validado')

    return response

async def test_invalid_job(controller: BotController, client: Client, response: Response):
    response = await response.reply_keyboard.click('Trabalho')
    assert response.num_messages == 1
    print('Escolhendo trabalho inválido')

    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'invalid')
    assert response.num_messages == 1
    assert 'invalid' not in response.full_text
    print('Trabalho invalidado')

    return response

async def test_gender(controller: BotController, client: Client, response: Response):
    response = await response.reply_keyboard.click('Genero sexual')
    assert response.num_messages == 1
    print('Escolhendo gênero')

    response = await response.reply_keyboard.click('Homem Cis')
    assert response.num_messages == 1
    assert 'Homem Cis' in response.full_text
    print('Gênero validado')

    return response

async def test_invalid_gender(controller: BotController, client: Client, response: Response):
    response = await response.reply_keyboard.click('Genero sexual')
    assert response.num_messages == 1
    print('Escolhendo gênero inválido')

    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'invalid')
    assert response.num_messages == 1
    assert 'invalid' not in response.full_text
    print('Gênero invalidado')

    return response

async def test_location(controller: BotController, client: Client, response: Response):
    response = await response.reply_keyboard.click('Localização')
    assert response.num_messages == 1
    print('Enviando localização')

    async with controller.collect(count=1) as response:
        await client.send_location(controller.peer_id, 51.500729, -0.124583)
    assert response.num_messages == 1
    assert 'England' in response.full_text
    assert 'City of Westminster' in response.full_text
    assert 'United Kingdom' in response.full_text
    print('Localização enviada')

    return response

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

async def click_signup(controller: BotController, client: Client, response: Response):
    response = await response.reply_keyboard.click('Registrar')
    assert response.num_messages == 1
    print('Registro iniciado')

    return response

async def signup_test(controller: BotController, client: Client):
    response = await start_conv_test(controller, client)
    response = await click_signup(controller, client, response)
    response = await test_invalid_username(controller, client, response)
    response = await test_username(controller, client, response)
    response = await test_invalid_email(controller, client, response)
    response = await test_email(controller, client, response)
    response = await test_invalid_password(controller, client, response)
    response = await test_password(controller, client, response)
    response = await test_invalid_race(controller, client, response)
    response = await test_race(controller, client, response)
    response = await test_invalid_job(controller, client, response)
    response = await test_job(controller, client, response)
    response = await test_location(controller, client, response)
    response = await test_gender(controller, client, response)
    response = await test_invalid_gender(controller, client, response)
    response = await test_gender(controller, client, response)
    resp = await click_signup_done(controller, client, response)
    await select_birthdate(controller, client, resp)
    print('Registro concluído\n')

async def click_login(controller: BotController, client: Client, response: Response):
    response = await response.reply_keyboard.click('Login')
    assert response.num_messages == 1
    print('Iniciando login')

    return response

async def click_login_done(controller: BotController, client: Client, response: Response):
    async with controller.collect(count=3) as resp:
        await response.reply_keyboard.click('Done')
    assert resp.num_messages == 3
    assert 'seja bem vindo' in resp.messages[0].text
    assert resp.messages[1].photo

    return response

async def login_test(controller: BotController, client: Client):
    response = await start_conv_test(controller, client)
    response = await click_login(controller, client, response)
    response = await test_invalid_email(controller, client, response)
    response = await test_email(controller, client, response)
    response = await test_password(controller, client, response)
    response = await test_invalid_password(controller, client, response)
    response = await test_password(controller, client, response)
    response = await click_login_done(controller, client, response)
    print('Login concluído\n')

async def click_logout(controller: BotController, client: Client, response: Response):
    async with controller.collect(count=2) as resp:
        await response.reply_keyboard.click('Logout')
    assert 'Até a próxima' in resp.messages[0].text
    print('Logout clicado')

async def logout_test(controller: BotController, client: Client):
    response = await start_conv_test(controller, client)
    await click_logout(controller, client, response)
    print('Logout concluído\n')

if __name__ == '__main__':
    client = configs.create_client()
    controller = configs.create_controller(client)
    asyncio.get_event_loop().run_until_complete(run_tests(controller, client))
