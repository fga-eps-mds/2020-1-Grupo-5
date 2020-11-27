import asyncio
from pyrogram import Client
import authentication, simple_messages, tips, informations

async def perform_full_run():
    client = Client('my_account')
    await simple_messages.run_tests(client)
    await authentication.run_tests(client)
    await informations.run_tests(client)
    await tips.run_tests(client)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(perform_full_run())
