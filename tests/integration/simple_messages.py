from pyrogram import Client
from tgintegration import BotController

async def run_tests(controller: BotController, client: Client):
    await unknown_test(controller, client)
    await about_test(controller)
    await finish_test(controller)
    await help_test(controller)

async def start_conv_test(controller: BotController):
    async with controller.collect(count=2) as response:
        await controller.send_command('start') # envia /start
    assert response.num_messages == 2 # 2 mensagens recebidas
    assert 'Bem vindo' in response.messages[0].text # primeira mensagem recebida corretamente
    assert response.messages[1].photo # segunda mensagem é uma foto
    print('Conversa iniciada')

    return response

async def unknown_test(controller: BotController, client: Client):
    response = await start_conv_test(controller)

    async with controller.collect(count=1) as response:
        await client.send_message(controller.peer_id, 'Mensagem inválida')
    assert response.num_messages == 1
    assert 'Não entendi' in response.full_text
    print('Mensagem não reconhecida testada\n')

async def help_test(controller: BotController):
    response = await start_conv_test(controller)

    async with controller.collect(count=3) as resp:
        await response.reply_keyboard.click('Ajuda')
    assert resp.num_messages == 3
    assert 'possui as seguintes funcionalidades' in resp.messages[0].text
    assert 'Informações gerais' in resp.messages[1].text
    assert 'Para informações mais detalhadas' in resp.messages[2].text
    print('Ajuda testada\n')

async def about_test(controller: BotController):
    response = await start_conv_test(controller)

    resp = await response.reply_keyboard.click('Sobre')
    assert 'O DoctorS é um Telegram Bot' in resp.full_text
    print('Sobre testado\n')

async def finish_test(controller: BotController):
    response = await start_conv_test(controller)

    resp = await response.reply_keyboard.click('Finalizar')
    assert 'Já vai?' in resp.full_text
    print('Finalizar testado\n')
