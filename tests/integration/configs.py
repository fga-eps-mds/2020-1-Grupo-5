import pathlib
from pyrogram import Client
from tgintegration import BotController

def create_client():
    client = Client('my_account')
    return client

def create_controller(client: Client):
    current_path = pathlib.Path(__file__).parent.absolute()
    bot_name = open(str(current_path) + '/bot_name.txt', 'r').read()
    controller = BotController(
        peer=bot_name,
        client=client,
    )
    return controller
