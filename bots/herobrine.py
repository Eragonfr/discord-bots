#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import discord


class HeroCommands(object):
    """Commandes personalisées pour Hérobrine."""

    def commands(config, client):
        @client.command(pass_context=True)
        async def sleep(ctx):
            em = discord.Embed(title='Bonne nuit!', description='Je vais me \
coucher pour faire passer la nuit.', colour=0x005D0A)
            em.set_author(name=client.user.name, icon_url=client.user.
                          avatar_url)
            tmp = await client.send_message(ctx.message.channel, embed=em)
            await asyncio.sleep(5)
            em = discord.Embed(title='Coucou!', description='C\'est le matin!',
                               colour=0x005D0A)
            await client.edit_message(tmp, embed=em)
            await client.delete_message(ctx.message)

        @client.command(pass_context=True)
        async def love(ctx):
            await client.send_message(ctx.message.channel, 'Je suis amoureux d\
\'Ahoki')
            await client.delete_message(ctx.message)

        @client.command(pass_context=True)
        async def castor(ctx):
            em = discord.Embed(title='GallaR.', description='GallaR quand il \
voit des castors , il porte des lunettes pour bien les voirs.',
                               colour=0x005D0A)
            em.set_author(name=client.user.name, icon_url=client.user.
                          avatar_url)
            await client.send_message(ctx.message.channel, embed=em)
            await client.delete_message(ctx.message)
