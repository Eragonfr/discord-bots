#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands


class FunyCommands(object):
    """docstring for FunyCommands."""

    def __init__(self, arg):
        self.arg = arg

    def misccommands(config, client):
        @client.command(pass_context=True)
        async def cats(ctx):
            """[Misc command] A simple cat command."""
            em = discord.Embed(title='Voilà un chat.', colour=0x005D0A)
            em.set_image(url='https://thecatapi.com/api/images/get')
            em.set_author(name=client.user.name, icon_url=client.user.
                          avatar_url)
            await client.send_message(ctx.message.channel, embed=em)

        @client.command(pass_context=True)
        async def dogs(ctx):
            """[Misc command] A simple dogs command."""
            em = discord.Embed(title='Voilà un chien.', colour=0x005D0A)
            em.set_image(url='https://random.dog/')
            em.set_author(name=client.user.name, icon_url=client.user.
                          avatar_url)
            await client.send_message(ctx.message.channel, embed=em)

        @client.command(pass_context=True)
        async def test(ctx):
            """[Misc command] A simple test command."""
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
            """[Misc command] A simple hugging command."""
            auteur = ctx.message.author.mention
            name = ctx.message.content[len('!hug'):].strip()
            em = discord.Embed(title='', description=':hugging: {} reçois un \
câlin de {} :heart:'.format(name, auteur), colour=0x005D0A)
            em.set_author(name=client.user.name, icon_url=client.user.
                          avatar_url)
            await client.send_message(ctx.message.channel, embed=em)

        @client.command(pass_context=True)
        async def kiss(ctx):
            """[Misc command] A simple kissing command."""
            auteur = ctx.message.author.mention
            name = ctx.message.content[len('!kiss'):].strip()
            em = discord.Embed(title='', description=':heart: {} reçois \
un bisou de {} :heart:'.format(name, auteur), colour=0x005D0A)
            em.set_author(name=client.user.name, icon_url=client.user.
                          avatar_url)
            await client.send_message(ctx.message.channel, embed=em)

        @client.command(pass_context=True)
        async def cpf(ctx):
            """[Misc command] A simple cpf command."""
            await client.send_message(ctx.message.channel, 'C\'est pas faux!')

        @client.command(pass_context=True)
        async def ageducapitaine(ctx):
            """[Misc command] A simple MDR command."""
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
        @commands.has_role(config['staff_role'])
        async def say(ctx):
            """[Misc command] A simple say command."""
            await client.delete_message(ctx.message)
            content = ctx.message.content.replace("!say ", "")
            await client.send_message(ctx.message.channel,
                                      '{}'.format(content))
