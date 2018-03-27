# -*- coding: utf-8 -*-

import asyncio
import discord
from discord.ext.commands import Bot

# Définnition du préfixe
client = Bot('!')


# Définnition des commandes
@client.command(pass_context = True)
async def clear(ctx, number):
    mgs = [] #Empty list to put all the ctx.messages in the log
    number = int(number) #Converting the amount of ctx.messages to delete to an integer
    msg_del = 0
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
        msg_del += 1
    await client.delete_messages(mgs)
    await client.send_message(ctx.message.channel, '{} messages  ont été supprimées.'.format(msg_del))

@client.command(pass_context = True)
async def test(ctx):
    counter = 0
    tmp = await client.send_message(ctx.message.channel, 'Calcul des messages...')
    async for log in client.logs_from(ctx.message.channel, limit=100):
        if log.author == ctx.message.author:
            counter += 1

    await client.edit_message(tmp, 'Vous avez {} messages.'.format(counter))

@client.command(pass_context = True)
async def sleep(ctx):
    tmp = await client.send_message(ctx.message.channel, 'Je vais me coucher pour faire passer la nuit.')
    await asyncio.sleep(5)
    await client.edit_message(tmp, 'C\'est le matin!')

@client.command(pass_context = True)
async def hug(ctx):
    auteur = ctx.message.author.mention
    name = ctx.message.content[len('!hug'):].strip()
    await client.send_message(ctx.message.channel, '{} reçois un câlin de {}'.format(name, auteur))

@client.command(pass_context = True)
async def kick(ctx, userName: discord.User):
    auteur = ctx.message.author.mention
    name = ctx.message.content[len('!kick'):].strip()
    await client.kick(userName)
    await client.send_message(ctx.message.channel, '{} à été expulsé par {}'.format(name, auteur))

# infos au démmarage
@client.event
async def on_ready():
    print('Connecté en tant que:')
    print(client.user.name)
    print(client.user.id)
    print('En cours d\'éxecution.')

client.run('NDI3Nzg0NjY1NjU1NDEwNjk5.DZplNg.3MYNRJ3LD0fh72sgbVdXkpXYDco')
