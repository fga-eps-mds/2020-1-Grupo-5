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
        await client.send_message(controller.peer_id, 'Dicas')
    assert response.num_messages == 1
    assert 'as informações que reuni' in response.full_text
    print('Dicas iniciado')

    print('(O que é) apertado')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, 'O que é')  # clica em O que é
    assert response.num_messages == 2
    assert 'Em dezembro de 2019 foi' in response.full_text

    print('Prevenção apertado')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, 'Prevenção')  # clica em Prevenção
    assert response.num_messages == 2
    assert 'Higiene ambiental:' in response.full_text

    print('Sintomas apertado')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, 'Sintomas')  # clica em Sintomas
    assert response.num_messages == 2
    assert 'Distúrbios gastrintestinais' in response.full_text

    print('Transmissão apertado')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, 'Transmissão')  # clica em Transmissão
    assert response.num_messages == 2
    assert 'A transmissão pode ocorrer de uma' in response.full_text

    print('Suspeita apertado')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, 'Suspeita')  # clica em Suspeita
    assert response.num_messages == 2
    assert 'postos de triagem nas Unidades Básicas' in response.full_text

    print('(Fake news) apertado')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, 'Fake news')  # clica em Fake news
    assert response.num_messages == 2
    assert 'Science Translational Medicine' in response.full_text
    
    print('Telefones apertado')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, 'Telefones')  # clica em Telefones
    assert response.num_messages == 2
    assert 'Defesa Civil' in response.full_text

    print('Locais apertado')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, 'Locais')  # clica em Fontes
    assert response.num_messages == 2
    assert 'Google Maps' in response.full_text
    assert response.inline_keyboards

    print('Fontes apertado')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, 'Fontes')  # clica em Fontes
    assert response.num_messages == 2
    assert '- BBC News' in response.full_text

    print('Voltando ao menu inicial')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, 'Voltar')  # clica em Voltar
    assert response.num_messages == 2
    assert 'Retornando' in response.full_text

    print('Dicas testado com sucesso\n')

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(run_tests(create_client()))
