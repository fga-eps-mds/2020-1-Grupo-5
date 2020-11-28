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

    print('Mostrando Informações')
    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'Minhas informações')
    assert response.num_messages == 1
    assert response.messages[0].photo

    print('Editando Perfil')
    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'Editar perfil')
    assert response.num_messages == 1
    
    # Username
    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'Username')
    print('Inserindo Username válido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "OutroUserName")
    assert response.num_messages == 2
    assert 'sucesso' in response.full_text
    print('Username aceito')

    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'Username')
    print('Inserindo Username inválido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Mini")
    assert response.num_messages == 2
    assert 'Entrada inválida' in response.full_text
    print('Username recusado')

    # Raça
    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'Raça')
    print('Inserindo Raça válida')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Branco")
    assert response.num_messages == 2
    assert 'sucesso' in response.full_text
    print('Raça aceita')

    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'Raça')
    print('Inserindo Raça inválida')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Branquo")
    assert response.num_messages == 2
    assert 'Entrada inválida' in response.full_text
    print('Raça recusada')

    # Genero sexual
    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'Genero sexual')
    print('Inserindo Genero sexual válido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Homem Cis")
    assert response.num_messages == 2
    assert 'sucesso' in response.full_text
    print('Genero sexual aceito')

    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'Genero sexual')
    print('Inserindo Genero sexual inválido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Inval")
    assert response.num_messages == 2
    assert 'Entrada inválida' in response.full_text
    print('Genero sexual recusado')

    # Trabalho
    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'Trabalho')
    print('Inserindo Trabalho válido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Não")
    assert response.num_messages == 2
    assert 'sucesso' in response.full_text
    print('Trabalho aceito')

    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'Trabalho')
    print('Inserindo Trabalho inválido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Siim")
    assert response.num_messages == 2
    assert 'Entrada inválida' in response.full_text
    print('Trabalho recusado')

    # Grupo de Risco
    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'Grupo de Risco')
    print('Inserindo Grupo de Risco válido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Não")
    assert response.num_messages == 2
    assert 'sucesso' in response.full_text
    print('Grupo de Risco aceito')

    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'Grupo de Risco')
    print('Inserindo Grupo de Risco inválido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Siim")
    assert response.num_messages == 2
    assert 'Entrada inválida' in response.full_text
    print('Grupo de Risco recusado')

    # Data de Nascimento
    async with controller.collect(count=2) as resp:
        await client.send_message(controller.peer_id, 'Nascimento')
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

    async with controller.collect(count=2) as resp:
        await client.send_message(controller.peer_id, "Nascimento")
    assert resp.num_messages == 2
    print('Data de nascimento inválida')
    async with controller.collect(count=2) as info:
        await client.send_message(controller.peer_id, "Siim")
    assert info.num_messages == 2
    assert 'inválida' in info.full_text
    print('Data de nascimento recusada')

    # Informações
    print('Mostrando Informações')
    async with controller.collect(count=1) as info:
        await client.send_message(controller.peer_id, 'Mostrar informações')
    assert info.num_messages == 1
    assert info.messages[0].photo

    # Voltando
    print('Voltando ao menu inicial')
    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'Voltar')
    assert 'Selecione' in response.full_text
    print('Editar Perfil testado com sucesso\n')

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(run_tests(create_client()))
