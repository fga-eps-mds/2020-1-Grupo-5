from pyrogram import Client
from tgintegration import BotController
import simple_messages

async def tips_test(controller: BotController, client: Client):
    response = await simple_messages.start_conv_test(controller, client)

    response = await response.reply_keyboard.click('Dicas')  # clica em Dicas 
    assert response.num_messages == 1
    assert 'as informações que reuni' in response.messages[0].text
    print('Dicas iniciado')
   
    print('(O que é) apertado')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, 'O que é')  # clica em O que é
    assert response.num_messages == 2
    assert 'Em dezembro de 2019 foi' in response.messages[0].text

    print('Prevenção apertado')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, 'Prevenção')  # clica em Prevenção
    assert response.num_messages == 2
    assert 'Higiene ambiental:' in response.messages[0].text

    print('Sintomas apertado')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, 'Sintomas')  # clica em Sintomas
    assert response.num_messages == 2
    assert 'Distúrbios gastrintestinais' in response.messages[0].text

    print('Transmissão apertado')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, 'Transmissão')  # clica em Transmissão
    assert response.num_messages == 2
    assert 'A transmissão pode ocorrer de uma' in response.messages[0].text

    print('Suspeita apertado')
    async with controller.collect(count=2) as response:
       await client.send_message(controller.peer_id, 'Suspeita')  # clica em Suspeita
    assert response.num_messages == 2
    assert 'postos de triagem nas Unidades Básicas' in response.messages[0].text

    print('(Fake news) apertado')
    async with controller.collect(count=2) as response:
       await client.send_message(controller.peer_id, 'Fake news')  # clica em Fake news
    assert response.num_messages == 2
    assert 'Science Translational Medicine' in response.messages[0].text
    
    print('Telefones apertado')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, 'Telefones')  # clica em Telefones
    assert response.num_messages == 2
    assert 'Defesa Civil' in response.messages[0].text

    print('Fontes apertado')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, 'Fontes')  # clica em Fontes
    assert response.num_messages == 2
    assert '- BBC News' in response.messages[0].text

    print('Voltando ao menu inicial')
    async with controller.collect(count=2) as response:
        await client.send_message(controller.peer_id, 'Voltar')  # clica em Voltar
    assert response.num_messages == 2
    assert 'Retornando' in response.messages[0].text

    print('Dicas testado com sucesso\n')

