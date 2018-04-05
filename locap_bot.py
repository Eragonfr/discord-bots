#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import discord
from discord.ext.commands import Bot

client = Bot('!')

@client.command(pass_context = True)
async def locap(ctx):
    em = discord.Embed(title='Salut Locap!', description='Locap est connecté!', colour=0x005D0A)
    em.set_image(url='https://cdn.discordapp.com/attachments/392004299791532032/431115531701977088/WUMPUS.gif')
    em.set_author(name='Locap', icon_url=client.user.avatar_url)
    await client.send_message(ctx.message.channel, embed=em)

# infos au démmarage
@client.event
async def on_ready():
    print('Connecté en tant que:')
    print(client.user.name)
    print(client.user.id)
    print('En cours d\'exécution.')

client.run('Token')
