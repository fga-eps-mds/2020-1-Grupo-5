import asyncio, pathlib
from pyrogram import Client
from tgintegration import BotController

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

    async with controller.collect(count=1) as response:
        await controller.send_command('report')
    assert response.num_messages == 1
    assert 'Sentiu sintomas' in response.full_text
    print('Report solicitado\n')

    print('Enviando sim')
    async with controller.collect(count=2) as resp:
        inline_keyboard = response.inline_keyboards[0]
        await inline_keyboard.click('Sim')
    
    assert 'Selecione os sintomas' in resp.full_text

    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'Febre')
    assert response.num_messages == 1
    assert 'Febre' in response.full_text
    print('Febre selecionado')

    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'Tosse')
    assert response.num_messages == 1
    assert 'Tosse' in response.full_text
    print('Tosse selecionado')

    async with controller.collect(count=2) as response:
        await client.send_location(controller.peer_id, 51.500729, -0.124583)
    assert resp.num_messages == 2
    assert 'Obrigado por nos informar' in response.full_text
    print('Bad report testado')

    async with controller.collect(count=1) as response:
        await controller.send_command('report')
    assert response.num_messages == 1
    assert 'Sentiu sintomas' in response.full_text
    print('Report solicitado\n')

    print('Enviando não')
    async with controller.collect(count=1) as resp:
        inline_keyboard = response.inline_keyboards[0]
        await inline_keyboard.click('Não')
    assert response.num_messages == 1
    assert 'Obrigado por nos informar' in resp.full_text
    print('Good report testado')

    async with controller.collect(count=1) as response:
        await controller.send_command('report')
    assert response.num_messages == 1
    assert 'Sentiu sintomas' in response.full_text
    print('Report solicitado\n')

    async with controller.collect(count=1) as resp:
        inline_keyboard = response.inline_keyboards[0]
        await inline_keyboard.click('Não')
    assert response.num_messages == 1
    assert 'Algo deu errado' in resp.full_text
    print('Report recusado')

    print('Report de saúde testado')


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(run_tests(create_client()))