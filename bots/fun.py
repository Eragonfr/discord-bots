#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import discord


class FunyCommands(object):
    """docstring for FunyCommands."""

    def __init__(self, arg):
        self.arg = arg

    def commands(config, client):
        @client.command(pass_context=True)
        async def cats(ctx):
            em = discord.Embed(title='Voilà un chat.', colour=0x005D0A)
            em.set_image(url='https://thecatapi.com/api/images/get')
            em.set_author(name=client.user.name, icon_url=client.user.
                          avatar_url)
            await client.send_message(ctx.message.channel, embed=em)

        @client.command(pass_context=True)
        async def dogs(ctx):
            em = discord.Embed(title='Voilà un chien.', colour=0x005D0A)
            em.set_image(url='https://random.dog/')
            em.set_author(name=client.user.name, icon_url=client.user.
                          avatar_url)
            await client.send_message(ctx.message.channel, embed=em)

        @client.command(pass_context=True)
        async def test(ctx):
            em = discord.Embed(title='', description='Calcul des messages...',
                               colour=0x005D0A)
            em.set_author(name=client.user.name, icon_url=client.user.
                          avatar_url)
            counter = 0
            tmp = await client.send_message(ctx.message.channel,
                                            embed=em)
            async for log in client.logs_from(ctx.message.channel, limit=100):
                if log.author == ctx.message.author:
                    counter += 1

            em = discord.Embed(title='', description='Vous avez écrit {} \
messages.'.format(counter), colour=0x005D0A)
            await client.edit_message(tmp, embed=em)

        @client.command(pass_context=True)
        async def hug(ctx):
            auteur = ctx.message.author.mention
            name = ctx.message.content[len('!hug'):].strip()
            em = discord.Embed(title='', description=':hugging: {} reçois un \
câlin de {} :heart:'.format(name, auteur), colour=0x005D0A)
            em.set_author(name=client.user.name, icon_url=client.user.
                          avatar_url)
            await client.send_message(ctx.message.channel, embed=em)

        @client.command(pass_context=True)
        async def kiss(ctx):
            auteur = ctx.message.author.mention
            name = ctx.message.content[len('!kiss'):].strip()
            em = discord.Embed(title='', description=':heart: {} reçois \
un bisou de {} :heart:'.format(name, auteur), colour=0x005D0A)
            em.set_author(name=client.user.name, icon_url=client.user.
                          avatar_url)
            await client.send_message(ctx.message.channel, embed=em)

        @client.command(pass_context=True)
        async def cpf(ctx):
            await client.send_message(ctx.message.channel, 'C\'est pas faux!')

        @client.command(pass_context=True)
        async def torture(ctx, userName: discord.User):
            auteur = ctx.message.author.mention
            name = ctx.message.content[len('!torture'):].strip()
            await client.change_nickname(userName, 'Torturé, meurtri')
            em = discord.Embed(title='Torture', description='{} à été \
torturé par {}'.format(name, auteur), colour=0x005D0A)
            em.set_author(name=client.user.name, icon_url=client.user.
                          avatar_url)
            tmp = await client.send_message(ctx.message.channel, embed=em)
            await asyncio.sleep(5)
            await client.change_nickname(userName, '')
            em = discord.Embed(title='Fin de la torture.', description='{} s\'\
est remit de ses blessures.'.format(name), colour=0x005D0A)
            em.set_author(name=client.user.name, icon_url=client.user.
                          avatar_url)
            await client.edit_message(tmp, embed=em)

        @client.command(pass_context=True)
        async def ageducapitaine(ctx):
            em = discord.Embed(title='Quel est l\'âge du capitaine?',
                               description='Un navire est en mer, il est \
parti de Boston chargé de coton, il jauge 200 tonneaux, il fait voile vers Le \
Havre, le grand mât est cassé, il y a un mousse sur le gaillard avant, les \
passagers sont au nombre de douze, le vent souffle N.-E.-E., l\'horloge \
marque trois heures un quart de l\'après-midi, on est au mois de mai….\
\r**Quel est l\'âge du capitaine ?**', colour=0xFF2800)
            em.set_author(name=client.user.name,
                          icon_url=client.user.avatar_url)
            await client.send_message(ctx.message.channel, embed=em)

        @client.command(pass_context=True)
        async def anniversaire(ctx, userName: discord.User):
            em = discord.Embed(title='Bon anniversaire!', description='Joyeux \
anniversaire {}!'.format(userName.mention), colour=0x005D0A)
            em.set_image(url='https://orig00.deviantart.net/2336/f/2018/087/a/\
6/a6ee731989e9972328f62f7663f54b33-dc78dpp.png')
            em.set_author(name=client.user.name,
                          icon_url=client.user.avatar_url)
            await client.send_message(ctx.message.channel, embed=em)

        @client.command(pass_context=True)
        async def say(ctx):
            for i in ctx.message.author.roles:
                if i.name == config['staff_role']:
                    await client.delete_message(ctx.message)
                    content = ctx.message.content.replace("!say ", "")
                    await client.send_message(ctx.message.channel,
                                              '{}'.format(content))
                else:
                    print('{} à essayé de faire un say'.format(ctx.message.
                                                               author.name))
