#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import discord
import logging
import importlib
import sys
import json
from discord.ext.commands import Bot
from bots.admin import AdminCommands
from bots.fun import FunyCommands


class LoadFunctions(object):
    """"""
    def __init__(self, arg):
        self.arg = arg

    def help_bot():
        print("Utilisation: \n  main.py [dev|prod] [options]\n")
        print("Options:\n\t\t+TODO+")
        print("--------------------------------------------\n")
        print(" -h, --help   \t\tafficher cette aide")
        print(" -V, --version\t\tafficher la version\n")

    def load_config(bot):
        ofi = open('config.json', 'r')
        all_config_json = ofi.read()
        ofi.close()
        all_config = json.loads(all_config_json)
        try:
            bot_config = all_config[bot]
        except KeyError:
            print('Erreur la configuration n\'a pas pu être trouvée assurez \
                   vous d\'avoir bien un fichier config.json, \n et de l\'\
                   avoir correctement rempli')
        except:
            print('Oups! Une erreur inconnue est survenue lors du chargement \
                   de la configuration.')
        return bot_config

    def logs(bot):
        """Chargement et écriture des logs."""
        print('Chargement des logs')
        logger = logging.getLogger('discord')
        if bot == 'dev':
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.INFO)
        handler = logging.FileHandler(filename='discord.dev.log',
                                      encoding='utf-8', mode='w')
        handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:\
                                                %(name)s: %(message)s'))
        logger.addHandler(handler)

    def run(param1, config):
        botclient = Bot(config['BOT_PREFIX'])

        @botclient.event
        async def on_ready():
            print('Connecté en tant qu\'{}'.format(botclient.user.name))
            print('ID:{}'.format(botclient.user.id))
            print('En cours d\'éxecution.')
        print(config['BOT_VERSION'])
        AdminCommands.commands(config, botclient)
        FunyCommands.commands(config, botclient)
        LoadFunctions.logs(param1)
        print('Connexion à Discord en cours...')
        botclient.run(config['BOT_TOKEN'])
