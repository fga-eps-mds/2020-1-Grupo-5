import asyncio, string, random, pathlib
from pyrogram import Client
from tgintegration import BotController, Response

async def run_test(client: Client):
    current_path = pathlib.Path(__file__).parent.absolute()
    bot_name = open(str(current_path) + '/bot_name.txt', 'r').read()
    controller = BotController(
        peer=bot_name,
        client=client,
    )

    async with controller.collect(count=1) as resp:
        await client.send_message(controller.peer_id, 'Relatório de Saúde')
    assert resp.num_messages == 1
    assert 'Lembre-se sempre de cuidar' in resp.full_text
    assert 'bem 1' in resp.full_text
    assert 'mal 1' in resp.full_text
    print('Relatório de saúde enviado\n')

async def run_empty(client: Client):
    current_path = pathlib.Path(__file__).parent.absolute()
    bot_name = open(str(current_path) + '/bot_name.txt', 'r').read()
    controller = BotController(
        peer=bot_name,
        client=client,
    )

    async with controller.collect(count=1) as resp:
        await client.send_message(controller.peer_id, 'Relatório de Saúde')
    assert resp.num_messages == 1
    assert 'Parece que você ainda não reportou' in resp.full_text
    print('Inexistência de reports testada\n')
