#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
import asyncio
from discord.ext import commands


class AdminCommands(object):
    def __init__(self, arg):
        self.arg = arg

    def commands(config, client):
        @client.command(pass_context=True)
        async def clear(ctx, number):
            """
            Clear all of the selected messages. Ex: !clear 10 clear the last
            10 messages
            """
            mgs = []
            number = int(number)
            msg_del = 0
            async for x in client.logs_from(ctx.message.channel, limit=number):
                mgs.append(x)
                msg_del += 1
            await client.delete_messages(mgs)
            em = discord.Embed(title='', description='{} messages  ont été \
supprimées.'.format(msg_del), colour=0x005D0A)
            em.set_author(name=client.user.name, icon_url=client.user.
                          avatar_url)
            await client.send_message(ctx.message.channel, embed=em)

        @client.command(pass_context=True)
        @commands.has_role(config['staff_role'])
        async def kick(ctx, userName: discord.User):
            """[Admin command] A simple kick command."""
            await client.kick(userName)
            await client.send_message(ctx.message.channel, '{} à été expulsé \
par {}'.format(userName.mention, ctx.message.author.mention))

        @client.command(pass_context=True)
        @commands.has_role(config['staff_role'])
        async def ban(ctx, userName: discord.User):
            """[Admin command] A simple banhammer command."""
            await client.ban(userName)
            await client.send_message(ctx.message.channel, '{} à été banni\
par {}'.format(userName.mention, ctx.message.author.mention))

        @client.command(pass_context=True)
        @commands.has_role(config['staff_role'])
        async def unban(ctx, userName: discord.User):
            """[Admin command] A simple unban command."""
            await client.unban(userName)
            await client.send_message(ctx.message.channel, '{} à été débanni\
par {}'.format(userName.mention, ctx.message.author.mention))

        @client.command(pass_context=True)
        async def torture(ctx, userName: discord.User):
            """[Misc command] A simple destroy command."""
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
