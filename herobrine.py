#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import main
import asyncio
import discord
import json
from discord.ext.commands import Bot

# Définnition des variables
BOT_TOKEN = ""

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
    await client.send_message(ctx.message.channel, ':hugging: {} reçois un câlin de {} :heart:'.format(name, auteur))

@client.command(pass_context = True)
async def kiss(ctx):
    auteur = ctx.message.author.mention
    name = ctx.message.content[len('!kiss'):].strip()
    await client.send_message(ctx.message.channel, ':heart: {} reçois un bisou de {} :heart:'.format(name, auteur))

@client.command(pass_context = True)
async def f(ctx):
    await client.send_message(ctx.message.channel, '**FAUX!**')

@client.command(pass_context = True)
async def v(ctx):
    await client.send_message(ctx.message.channel, '**Vrai!**')

@client.command(pass_context = True)
async def cpf(ctx):
    await client.send_message(ctx.message.channel, 'C\'est pas faux!')

@client.command(pass_context = True)
async def love(ctx):
    await client.send_message(ctx.message.channel, 'Je suis amoureux d\'Ahoki, mais *chuut* faut pas le dire.')

@client.command(pass_context = True)
async def castor(ctx):
    await client.send_message(ctx.message.channel, 'GallaR quand il voit des castors , il porte des lunettes pour bien les voir')

@client.command(pass_context = True)
async def kick(ctx, userName: discord.User):
    auteur = ctx.message.author.mention
    name = ctx.message.content[len('!kick'):].strip()
    await client.kick(userName)
    await client.send_message(ctx.message.channel, '{} à été expulsé par {}'.format(name, auteur))

@client.command(pass_context = True)
async def ban(ctx, userName: discord.User):
    auteur = ctx.message.author.mention
    name = ctx.message.content[len('!ban'):].strip()
    file = "/home/samuel/Images/Gif/banhammer.gif"
    await client.ban(userName)
    await client.send_file(ctx.message.channel, file, filename=None, content='{} à été banni par {}'.format(name, auteur), tts=False)

@client.command(pass_context = True)
async def torture(ctx, userName: discord.User):
    auteur = ctx.message.author.mention
    name = ctx.message.content[len('!torture'):].strip()
    await client.change_nickname(userName, 'Torturé, meurtri')
    tmp = await client.send_message(ctx.message.channel, '{} à été torturé par {}'.format(name, auteur))
    await asyncio.sleep(5)
    await client.change_nickname(userName, '')
    await client.edit_message(tmp, '{} s\'est remit de ses blessures.'.format(name, auteur))

@client.command(pass_context = True)
async def embed(ctx):
    em = discord.Embed(title='My Embed Title', description='My Embed Content.', colour=0xDEADBF)
    em.set_author(name='Someone', icon_url=client.user.default_avatar_url)
    await client.send_message(ctx.message.channel, embed=em)

@client.command(pass_context = True)
async def ageducapitaine(ctx):
    em = discord.Embed(title='Quel est l\'âge du capitaine?', description='\
Un navire est en mer, il est parti de Boston chargé de coton, il jauge 200 \
tonneaux, il fait voile vers Le Havre, le grand mât est cassé, il y a un \
mousse sur le gaillard avant, les passagers sont au nombre de douze, \
le vent souffle N.-E.-E., l\'horloge marque trois heures un quart de l\'\
après-midi, on est au mois de mai….\r**Quel est l\'âge du capitaine ?**',
    colour=0xFF2800)
    em.set_author(name='Herobrine', icon_url=client.user.avatar_url)
    await client.send_message(ctx.message.channel, embed=em)

@client.command(pass_context = True)
async def anniversaire(ctx, userName: discord.User):
    em = discord.Embed(title='Bon anniversaire!', description='Joyeux anniversaire {}!'.format(userName.mention),
    colour=0x005D0A)
    em.set_image(url='https://orig00.deviantart.net/2336/f/2018/087/a/6/a6ee731989e9972328f62f7663f54b33-dc78dpp.png')
    em.set_author(name='Herobrine', icon_url=client.user.avatar_url)
    await client.send_message(ctx.message.channel, embed=em)

# infos au démmarage
@client.event
async def on_ready():
    print('Connecté en tant que:')
    print(client.user.name)
    print(client.user.id)
    print('En cours d\'exécution.')

client.run(BOT_TOKEN)
