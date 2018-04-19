#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import discord


class HeroCommands(object):
    """docstring for HeroCommands."""
    def __init__(self, arg):
        self.arg = arg

    def commands(config, client):
        @client.command(pass_context=True)
        async def sleep(ctx):
            tmp = await client.send_message(ctx.message.channel,
                                            'Je vais me coucher pour faire \
passer la nuit.')
            await asyncio.sleep(5)
            await client.edit_message(tmp, 'C\'est le matin!')

        @client.command(pass_context=True)
        async def love(ctx):
            await client.send_message(ctx.message.channel, 'Je suis amoureux \
d\'Ahoki')

        @client.command(pass_context=True)
        async def castor(ctx):
            await client.send_message(ctx.message.channel,
                                      'GallaR quand il voit des castors , il \
porte des lunettes pour bien les voirs.')
