from email import message
from http import client
from lib2to3.pgen2 import token
from pydoc import cli
import discord

token = "OTY1OTM3MTY4OTE0NzE4NzYw.Yl6dFw.ccht5SQyb9LndjH5-S6vTykW5yw"

client = discord.Client()


block_names = [""]

    

channel_id = client.get_channel( 655756189895884816 )

@client.event
async def on_ready():
    print(f"bot log as{client.user}")

@client.event
async def on_message(msg):
    channel = discord.utils.get(msg.guild.channels, name='основной')
    str_roles = str(msg.author.roles)
    if  any([
        'алекс ди' in str_roles,
        'Moderator' in str_roles,
        ]):
            await msg.delete() # Deletes the message
            return




client.run(token)