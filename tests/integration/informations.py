from pyrogram import Client
from tgintegration import BotController
import simple_messages

async def info_edit_test(controller: BotController, client: Client):
    response = await simple_messages.start_conv_test(controller)

    print('Mostrando Informações')
    async with controller.collect(count=1) as info:
        await client.send_message(controller.peer_id, 'Minhas informações')
    assert info.num_messages == 1
    assert info.messages[0].photo

    print('Editando Perfil')
    resp = await response.reply_keyboard.click('Editar perfil')
    assert resp.num_messages == 1
    
    # Username
    response = await resp.reply_keyboard.click('Username')
    print('Inserindo Username válido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "OutroUserName")
    assert response.num_messages == 2
    assert 'sucesso' in response.messages[0].text
    print('Username aceito')
    resp = await response.reply_keyboard.click('Username')
    print('Inserindo Username inválido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Mini")
    assert response.num_messages == 2
    assert 'Entrada inválida' in response.messages[0].text
    print('Username recusado')

    # Raça
    resp = await response.reply_keyboard.click('Raça')
    print('Inserindo Raça válida')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Branco")
    assert response.num_messages == 2
    assert 'sucesso' in response.messages[0].text
    print('Raça aceita')
    resp = await response.reply_keyboard.click('Raça')
    print('Inserindo Raça inválida')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Branquo")
    assert response.num_messages == 2
    assert 'Entrada inválida' in response.messages[0].text
    print('Raça recusada')

    # Genero sexual
    resp = await response.reply_keyboard.click('Genero sexual')
    print('Inserindo Genero sexual válido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Homem Cis")
    assert response.num_messages == 2
    assert 'sucesso' in response.messages[0].text
    print('Genero sexual aceito')
    resp = await response.reply_keyboard.click('Genero sexual')
    print('Inserindo Genero sexual inválido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Inval")
    assert response.num_messages == 2
    assert 'Entrada inválida' in response.messages[0].text
    print('Genero sexual recusado')

    # Trabalho
    resp = await response.reply_keyboard.click('Trabalho')
    print('Inserindo Trabalho válido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Não")
    assert response.num_messages == 2
    assert 'sucesso' in response.messages[0].text
    print('Trabalho aceito')
    resp = await response.reply_keyboard.click('Trabalho')
    print('Inserindo Trabalho inválido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Siim")
    assert response.num_messages == 2
    assert 'Entrada inválida' in response.messages[0].text
    print('Trabalho recusado')

    # Grupo de Risco
    resp = await response.reply_keyboard.click('Grupo de Risco')
    print('Inserindo Grupo de Risco válido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Não")
    assert response.num_messages == 2
    assert 'sucesso' in response.messages[0].text
    print('Grupo de Risco aceito')
    resp = await response.reply_keyboard.click('Grupo de Risco')
    print('Inserindo Grupo de Risco inválido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Siim")
    assert response.num_messages == 2
    assert 'Entrada inválida' in response.messages[0].text
    print('Grupo de Risco recusado')

    # Data de Nascimento
    async with controller.collect(count=2) as resp:
        await response.reply_keyboard.click('Nascimento')
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
    assert 'inválida' in info.messages[0].text
    print('Data de nascimento recusada')

    # Informações
    print('Mostrando Informações')
    async with controller.collect(count=1) as info:
        await client.send_message(controller.peer_id, 'Mostrar informações')
    assert info.num_messages == 1
    assert info.messages[0].photo

    # Voltando
    print('Voltando ao menu inicial')
    resp = await response.reply_keyboard.click('Voltar')
    print('Editar Perfil testado com sucesso\n')

