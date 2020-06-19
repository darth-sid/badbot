import os,random
import discord
from dotenv import load_doten

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author ==  client.user:
        return
    if message.content == 'censor':
        censored = True
    if message.content == 'f':
        if censored:
            await message.channel.send('||fuck you||')
        else:
            await message.channel.send('fuck you')
