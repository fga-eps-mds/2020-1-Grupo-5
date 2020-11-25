import asyncio
from pyrogram import Client
from tgintegration import BotController
import authentication, simple_messages, configs

async def perform_full_run(controller: BotController, client: Client):
    await controller.clear_chat() # limpa o histórico
    await simple_messages.help_test(controller, client) # Testa ajuda
    await simple_messages.finish_test(controller, client) # Testa Finalizar
    await simple_messages.unknown_test(controller, client) # Testa mensagem desconhecida
    await simple_messages.about_test(controller, client) # Testa Sobre
    await authentication.run_tests(controller, client) # Testa, respectivamente, cadastro, logout e login
    await info_edit_test(controller, client) # Testa a edição de informações pessoais
    await tips_test(controller, client)   # Testa as dicas
    await authentication.logout_test(controller, client) # Logout novamente (Inicio fresco)
    
async def tips_test(controller: BotController, client: Client):
    menu = await simple_messages.start_conv_test(controller, client)

    menu = await menu.reply_keyboard.click('Dicas')  # clica em Dicas 
    assert menu.num_messages == 1
    assert 'as informações que reuni' in menu.messages[0].text
    print('Dicas iniciado')
   
    print('(O que é) apertado')
    async with controller.collect(count=2) as response:
        await menu.reply_keyboard.click('O que é')  # clica em O que é
    assert response.num_messages == 2
    assert 'Em dezembro de 2019 foi' in response.messages[0].text

    print('Prevenção apertado')
    async with controller.collect(count=2) as response:
        await menu.reply_keyboard.click('Prevenção')  # clica em Prevenção
    assert response.num_messages == 2
    assert 'Higiene ambiental:' in response.messages[0].text

    print('Sintomas apertado')
    async with controller.collect(count=2) as response:
        await menu.reply_keyboard.click('Sintomas')  # clica em Sintomas
    assert response.num_messages == 2
    assert 'Distúrbios gastrintestinais' in response.messages[0].text

    print('Transmissão apertado')
    async with controller.collect(count=2) as response:
        await menu.reply_keyboard.click('Transmissão')  # clica em Transmissão
    assert response.num_messages == 2
    assert 'A transmissão pode ocorrer de uma' in response.messages[0].text

    print('Suspeita apertado')
    async with controller.collect(count=2) as response:
        await menu.reply_keyboard.click('Suspeita')  # clica em Suspeita
    assert response.num_messages == 2
    assert 'postos de triagem nas Unidades Básicas' in response.messages[0].text

    print('(Fake news) apertado')
    async with controller.collect(count=2) as response:
        await menu.reply_keyboard.click('Fake news')  # clica em Fake news
    assert response.num_messages == 2
    assert 'Science Translational Medicine' in response.messages[0].text
    
    print('Telefones apertado')
    async with controller.collect(count=2) as response:
        await menu.reply_keyboard.click('Telefones')  # clica em Telefones
    assert response.num_messages == 2
    assert 'Defesa Civil' in response.messages[0].text

    print('Fontes apertado')
    async with controller.collect(count=2) as response:
        await menu.reply_keyboard.click('Fontes')  # clica em Fontes
    assert response.num_messages == 2
    assert '- BBC News' in response.messages[0].text

    print('Voltando ao menu inicial')
    async with controller.collect(count=2) as response:
        await menu.reply_keyboard.click('Voltar')  # clica em Voltar
    assert response.num_messages == 2
    assert 'Cancelando' in response.messages[0].text

    print('Dicas testado com sucesso\n')

async def info_edit_test(controller: BotController, client: Client):
    response = await simple_messages.start_conv_test(controller, client)

    print('Mostrando Informações')
    async with controller.collect(count=1) as info:
        await client.send_message(controller.peer_id, 'Minhas informações')
    assert info.num_messages == 1
    assert info.messages[0].photo

    print('Editando Perfil')
    response = await response.reply_keyboard.click('Editar perfil')
    assert response.num_messages == 1
    
    # Username
    response = await response.reply_keyboard.click('Username')
    print('Inserindo Username válido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "OutroUserName")
    assert response.num_messages == 2
    assert 'sucesso' in response.messages[0].text
    print('Username aceito')
    response = await response.reply_keyboard.click('Username')
    print('Inserindo Username inválido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Mini")
    assert response.num_messages == 2
    assert 'Entrada inválida' in response.messages[0].text
    print('Username recusado')

    # Raça
    response = await response.reply_keyboard.click('Raça')
    print('Inserindo Raça válida')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Branco")
    assert response.num_messages == 2
    assert 'sucesso' in response.messages[0].text
    print('Raça aceita')
    response = await response.reply_keyboard.click('Raça')
    print('Inserindo Raça inválida')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Branquo")
    assert response.num_messages == 2
    assert 'Entrada inválida' in response.messages[0].text
    print('Raça recusada')

    # Genero sexual
    response = await response.reply_keyboard.click('Genero sexual')
    print('Inserindo Genero sexual válido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Homem Cis")
    assert response.num_messages == 2
    assert 'sucesso' in response.messages[0].text
    print('Genero sexual aceito')
    response = await response.reply_keyboard.click('Genero sexual')
    print('Inserindo Genero sexual inválido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Inval")
    assert response.num_messages == 2
    assert 'Entrada inválida' in response.messages[0].text
    print('Genero sexual recusado')

    # Trabalho
    response = await response.reply_keyboard.click('Trabalho')
    print('Inserindo Trabalho válido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Não")
    assert response.num_messages == 2
    assert 'sucesso' in response.messages[0].text
    print('Trabalho aceito')
    response = await response.reply_keyboard.click('Trabalho')
    print('Inserindo Trabalho inválido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Siim")
    assert response.num_messages == 2
    assert 'Entrada inválida' in response.messages[0].text
    print('Trabalho recusado')

    # Grupo de Risco
    response = await response.reply_keyboard.click('Grupo de Risco')
    print('Inserindo Grupo de Risco válido')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, "Não")
    assert response.num_messages == 2
    assert 'sucesso' in response.messages[0].text
    print('Grupo de Risco aceito')
    response = await response.reply_keyboard.click('Grupo de Risco')
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
    async with controller.collect(count=2) as info:
        await response.reply_keyboard.click('Nascimento')
    assert info.num_messages == 2
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
    response = await response.reply_keyboard.click('Voltar')
    print('Editar Perfil testado com sucesso\n')


if __name__ == "__main__":
    client = configs.create_client()
    controller = configs.create_controller(client)
    asyncio.get_event_loop().run_until_complete(perform_full_run(controller, client))
