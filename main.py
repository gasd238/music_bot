# -*- coding: utf-8 -*- 
import asyncio
import discord
import youtube_dl
import datetime
import re
import os

from Modules.help import Help

# Discord Client
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----------------------')
    game = discord.Game("!설명으로 도움말")
    await client.change_presence(status=discord.Status.online, activity=game)

    loop.create_task(realtime())


@client.event
async def on_message(msg):
    # 봇 설명
    if message.content == "!설명":
        createdEmbed = help.create_help_embed()
        await channel.send(embed=createdEmbed)

client.run(token)
