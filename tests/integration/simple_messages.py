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

    async with controller.collect(count=2) as response:
        await controller.send_command('start') # envia /start
    assert response.num_messages == 2 # 2 mensagens recebidas
    assert 'Bem vindo' in response.messages[0].text # primeira mensagem recebida corretamente
    assert response.messages[1].photo # segunda mensagem é uma foto
    print('Conversa iniciada')

    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, 'Mensagem inválida')
    assert response.num_messages == 2
    assert 'Não entendi' in response.messages[0].text
    print('Mensagem não reconhecida testada')

    async with controller.collect(count=3) as response:
        await client.send_message(controller.peer_id, 'Ajuda')
    assert response.num_messages == 3
    assert 'possui as seguintes funcionalidades' in response.messages[0].text
    assert 'Informações gerais' in response.messages[1].text
    assert 'Para informações mais detalhadas' in response.messages[2].text
    print('Ajuda testada')

    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'Sobre')
    assert 'O DoctorS é um Telegram Bot' in response.full_text
    print('Sobre testado')

    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'Finalizar')
    assert 'Já vai?' in response.full_text
    print('Finalizar testado')

    async with controller.collect(count=1) as response:
        await controller.send_command('noticia')
    assert response.num_messages == 1
    assert 'espero que esteja se sentindo bem' in response.full_text
    print('Notícia testada\n')

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(run_tests(create_client()))
