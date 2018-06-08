#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands


class Commands(object):
    """docstring for FunyCommands."""

    def __init__(self, arg):
        self.arg = arg

    def commands(config, client):
        @client.command(pass_context=True)
        async def cat(ctx):
            """[Misc command] A simple cat command."""
            em = discord.Embed(title='Here\'s a cat.', colour=0x005D0A)
            em.set_image(url='https://thecatapi.com/api/images/get')
            em.set_author(name=client.user.name, icon_url=client.user.
                          avatar_url)
            await client.send_message(ctx.message.channel, embed=em)

        @client.command(pass_context=True)
        async def dog(ctx):
            """[Misc command] A simple dogs command."""
            em = discord.Embed(title='Here\'s a dog.', colour=0x005D0A)
            em.set_image(url='https://random.dog/')
            em.set_author(name=client.user.name, icon_url=client.user.
                          avatar_url)
            await client.send_message(ctx.message.channel, embed=em)

        @client.command(pass_context=True)
        async def test(ctx):
            """[Misc command] A simple test command."""
            em = discord.Embed(title='', description='Counting the messages...',
                               colour=0x005D0A)
            em.set_author(name=client.user.name, icon_url=client.user.
                          avatar_url)
            counter = 0
            tmp = await client.send_message(ctx.message.channel,
                                            embed=em)
            async for log in client.logs_from(ctx.message.channel, limit=100):
                if log.author == ctx.message.author:
                    counter += 1

            em = discord.Embed(title='', description='You wrote {} messages.'
                               .format(counter), colour=0x005D0A)
            await client.edit_message(tmp, embed=em)

        @client.command(pass_context=True)
        async def hug(ctx):
            """[Misc command] A simple hugging command."""
            auteur = ctx.message.author.mention
            name = ctx.message.content[len('!hug'):].strip()
            em = discord.Embed(title='', description=':hugging: {} receive a \
hug from {} :heart:'.format(name, auteur), colour=0x005D0A)
            em.set_author(name=client.user.name, icon_url=client.user.
                          avatar_url)
            await client.send_message(ctx.message.channel, embed=em)

        @client.command(pass_context=True)
        async def kiss(ctx):
            """[Misc command] A simple kissing command."""
            auteur = ctx.message.author.mention
            name = ctx.message.content[len('!kiss'):].strip()
            em = discord.Embed(title='', description=':heart: {} receive a \
kiss from {} :heart:'.format(name, auteur), colour=0x005D0A)
            em.set_author(name=client.user.name, icon_url=client.user.
                          avatar_url)
            await client.send_message(ctx.message.channel, embed=em)

        @client.command(pass_context=True)
        async def tbh(ctx):
            """[Misc command] A simple cpf command."""
            await client.send_message(ctx.message.channel, 'To be honest')

        @client.command(pass_context=True)
        @commands.has_role(config['staff_role'])
        async def say(ctx):
            """[Misc command] A simple say command."""
            await client.delete_message(ctx.message)
            content = ctx.message.content.replace("!say ", "")
            await client.send_message(ctx.message.channel,
                                      '{}'.format(content))
