import asyncio
from pyrogram import Client
from tgintegration import BotController
import authentication, simple_messages, configs, tips, informations

async def perform_full_run(controller: BotController, client: Client):
    await controller.clear_chat() # limpa o histórico
    await simple_messages.run_tests(controller, client) # Testa mensagem desconhecida, sobre, finalizar e ajuda
    await authentication.run_tests(controller, client) # Testa, respectivamente, cadastro, logout e login
    await informations.info_edit_test(controller, client) # Testa a edição de informações pessoais
    await tips.tips_test(controller, client)   # Testa as dicas
    await authentication.logout_test(controller) # Logout novamente (Inicio fresco)

if __name__ == "__main__":
    client = configs.create_client()
    controller = configs.create_controller(client)
    asyncio.get_event_loop().run_until_complete(perform_full_run(controller, client))
