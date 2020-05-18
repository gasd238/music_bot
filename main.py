# -*- coding: utf-8 -*- 
import asyncio
import discord
import youtube_dl
import datetime
import re
import os

from Modules.help import Help
from Modules.setting import *

client = discord.Client()

# Discord Client
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----------------------')
    game = discord.Game("-설명으로 도움말")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(msg):
    channel = msg.channel
    # 봇 설명
    if msg.content == "-설명":
        createdEmbed = Help.create_help_embed()
        await channel.send(embed=createdEmbed)
    
    if msg.content.startswith == "-재생":
        await channel.send("준비중")

client.run(token)
