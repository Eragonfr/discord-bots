#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import json
from discord.ext.commands import Bot

from bots.admin import AdminCommands
from bots.fun import FunyCommands
from bots.herobrine import HeroCommands


class LoadFunctions(object):
    """"""

    def __init__(self, arg):
        self.arg = arg

    def help_bot(args):
        print("""
Utilisation : \n  main.py [dev|prod] [options]\n\n
Les arguments 'dev' et 'prod' sont obligatoires, certaines commandes n'en
ont pas besoin.\n
 -h, --help   \t\tafficher cette aide\n
 -V, --version\t\tafficher la version(pas implémenté)\n
 Signalez toute anomalie à sam.vzh@netc.fr
""")

    def load_config(bot):
        try:
            ofi = open('config.json', 'r')
            all_config_json = ofi.read()
            ofi.close()
            all_config = json.loads(all_config_json)
            bot_config = all_config[bot]
        except KeyError:
            print('Erreur la configuration n\'a pas pu être trouvée assurez \
                   vous d\'avoir bien un fichier config.json, \n et de l\'\
                   avoir correctement rempli')
        return bot_config

    def logs(bot):
        """Chargement et écriture des logs."""
        print('Chargement des logs')
        logger = logging.getLogger('discord')
        if bot == 'dev':
            logger.setLevel(logging.DEBUG)
            file = 'discord.dev.log'
        else:
            logger.setLevel(logging.DEBUG)
            file = 'discord.log'
        handler = logging.FileHandler(filename=file,
                                      encoding='utf-8', mode='w')
        handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:\
                                                %(name)s: %(message)s'))
        logger.addHandler(handler)

    def run(config):
        botclient = Bot(config['BOT_PREFIX'])

        @botclient.event
        async def on_ready():
            print('Connecté en tant qu\'{}'.format(botclient.user.name))
            print('ID:{}'.format(botclient.user.id))
            print('En cours d\'éxecution.')
        print(config['BOT_VERSION'])
        AdminCommands.commands(config, botclient)
        FunyCommands.commands(config, botclient)
        HeroCommands.commands(config, botclient)
        LoadFunctions.logs(config['BOT_VERSION'])
        print('Connexion à Discord en cours...')
        botclient.run(config['BOT_TOKEN'])
