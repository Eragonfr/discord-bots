#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Fichier des fonctions principales du bot, chargement dynamique des fichiers
et autres fonctions pratiques du bot.
"""

import logging
import sys
import discord
import configparser
import importlib
from discord.ext.commands import Bot


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
            all_config = configparser.ConfigParser()
            all_config.read('config.ini')
            bot_config = all_config[bot]
        except FileNotFoundError:
            print('Erreur le fichier de configuration n\'a pas pu être \
localisé. Assurez vous d\'en avoir un et d\'avoir les droits de lecture et \
d\'écriture dessus')
            sys.exit(1)
        except KeyError:
            print('Erreur la configuration demandé n\'a pas pu être trouvée \
assurez vous d\'avoir correctement rempli le fichier config.ini')
            sys.exit(1)
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
        botclient = Bot(config['prefix'])

        @botclient.event
        async def on_ready():
            print('Connecté en tant qu\'{}'.format(botclient.user.name))
            print('ID:{}'.format(botclient.user.id))
            print('En cours d\'éxecution.')
        print('Discord Bot({}) using discord.py {}'.format(
              config['version'], discord.__version__))
        for i, e in eval(config['commands']).items():
            importlib.import_module(e, i)
            eval(i).commands(config, botclient)
            # FunyCommands.commands(config, botclient)
            # HeroCommands.commands(config, botclient)
        LoadFunctions.logs(config['version'])
        print('Connexion à Discord en cours...')
        botclient.run(config['token'])
