import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    callbacks = {
        "janet": "Slut!",
        "brad": "Asshole!",
        "dr scott": "Suck my cock!",
        "dr. scott": "Suck my cock!",
        "doctor scott": "Suck my cock!",
        "rocky": "Bullwinkle!",
        'frank n furter': 'ilise is gay lol'
    }

    lower = message.content.lower()
    for key in callbacks:
        if key in lower:
            await message.channel.send(callbacks[key])

client.run(TOKEN)