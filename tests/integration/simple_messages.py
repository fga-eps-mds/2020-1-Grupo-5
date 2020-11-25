from pyrogram import Client
from tgintegration import BotController

async def start_conv_test(controller: BotController, client: Client):
    async with controller.collect(count=2) as response:
        await controller.send_command('start') # envia /start
    assert response.num_messages == 2 # 2 mensagens recebidas
    assert 'Bem vindo' in response.messages[0].text # primeira mensagem recebida corretamente
    assert response.messages[1].photo # segunda mensagem é uma foto
    print('Conversa iniciada')

    return response

async def unknown_test(controller: BotController, client: Client):
    response = await start_conv_test(controller, client)

    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'Mensagem inválida')
    assert response.num_messages == 1
    assert 'Não entendi' in response.full_text
    print('Mensagem não reconhecida testada\n')

async def help_test(controller: BotController, client: Client):
    response = await start_conv_test(controller, client)

    async with controller.collect(count=3) as response:
        await client.send_message(controller.peer_id, 'Ajuda')
    assert response.num_messages == 3
    assert 'possui as seguintes funcionalidades' in response.messages[0].text
    assert 'Informações gerais' in response.messages[1].text
    assert 'Para informações mais detalhadas' in response.messages[2].text
    print('Ajuda testada\n')

async def about_test(controller: BotController, client: Client):
    response = await start_conv_test(controller, client)

    response = await response.reply_keyboard.click('Sobre')
    assert 'O DoctorS é um Telegram Bot' in response.full_text
    print('Sobre testado\n')

async def finish_test(controller: BotController, client: Client):
    response = await start_conv_test(controller, client)

    response = await response.reply_keyboard.click('Finalizar')
    assert 'Já vai?' in response.full_text
    print('Finalizar testado\n')
