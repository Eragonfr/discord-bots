#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import discord


class Commands(object):
    """Commandes personalisées pour Hérobrine."""

    def commands(config, client):
        @client.command(pass_context=True)
        async def sleep(ctx):
            em = discord.Embed(title='Good night!', description='I\'m gonna \
sleep to pass the night', colour=0x005D0A)
            em.set_author(name=client.user.name, icon_url=client.user.
                          avatar_url)
            tmp = await client.send_message(ctx.message.channel, embed=em)
            await asyncio.sleep(5)
            em = discord.Embed(title='Hello!', description='It\'s morning!',
                               colour=0x005D0A)
            await client.edit_message(tmp, embed=em)
            await client.delete_message(ctx.message)

        @client.command(pass_context=True)
        async def love(ctx):
            await client.send_message(ctx.message.channel, 'I\'m in love with \
Ahoki')
            await client.delete_message(ctx.message)

        @client.command(pass_context=True)
        async def birthday(ctx, userName: discord.User):
            em = discord.Embed(title='Happy birthday !!', description='It\'s \
your birthday {}!'.format(userName.mention), colour=0x005D0A)
            em.set_image(url='https://orig00.deviantart.net/2336/f/2018/087/a/\
6/a6ee731989e9972328f62f7663f54b33-dc78dpp.png')
            em.set_author(name=client.user.name,
                          icon_url=client.user.avatar_url)
            await client.send_message(ctx.message.channel, embed=em)
