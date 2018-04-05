import asyncio
import discord
from discord.ext.commands import Bot


client = Bot('¿')

@client.command(pass_context = True)
async def cats(ctx):
    await client.send_file(channel, 'https://thecatapi.com/api/images/get')

@client.command(pass_context = True)
async def dogs(ctx):
    await client.send_file(channel, 'https://random.dog/')


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
async def cpf(ctx):
    await client.send_message(ctx.message.channel, 'C\'est pas faux')
