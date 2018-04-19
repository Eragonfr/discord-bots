#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio

class AdminCommands(object):
    """"""
    def __init__(self, arg):
        self.arg = arg

    def commands(config, client):
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

        # @client.command(pass_context = True)
        # async def kick(ctx, userName: discord.User):
        #     auteur = ctx.message.author.mention
        #     name = ctx.message.content[len('!kick'):].strip()
        #     await client.kick(userName)
        #     await client.send_message(ctx.message.channel, '{} à été expulsé par {}'.format(name, auteur))

        # @client.command(pass_context = True)
        # async def ban(ctx, userName: discord.User):
        #     auteur = ctx.message.author.mention
        #     name = ctx.message.content[len('!ban'):].strip()
        #     await client.ban(userName)
        #     await client.send_message(ctx.message.channel, '{} à été banni par {}'.format(name, auteur))
        #
        # @client.command(pass_context = True)
        # async def unban(ctx, userName: discord.User):
        #     auteur = ctx.message.author.mention
        #     name = ctx.message.content[len('!unban'):].strip()
        #     await client.unban(userName)
        #     await client.send_message(ctx.message.channel, '{} à été débanni par {}'.format(name, auteur))
