import os
import discord
from discord.ext import commands
from scrapper import get_request, find_name_link

app = commands.Bot(command_prefix='#38')

@app.event
async def on_ready():
    print('Logging in: '+app.user.name)
    print('Connection was succesful')
    await app.change_presence(status=discord.Status.online, activity=discord.Game(name='떡상기원'))

@app.command(name = "찾기")
async def posts(ctx, name):
    encoded = get_request(name)
    stock = find_name_link(encoded)
    embed = discord.Embed(title = '결과', color=discord.Color.dark_blue())
    for stocks in stock:
        embed.add_field(name = stocks['name'], value = "[%s](%s)"%('링크', stocks['link']), inline=False)
    await ctx.send(embed=embed)

app.run("")