import os
import discord
from discord.ext import commands

app = commands.Bot(command_prefix='#38')

@app.event
async def on_ready():
    print('Logging in: ')
    print(app.user.name)
    print('connection was succesful')
    await app.change_presence(status=discord.Status.online, activity=discord.Game(name='떡상기원'))

app.run("")