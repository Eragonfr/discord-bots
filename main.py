#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import discord
import logging
import importlib
import sys
import json

# Définition de quelques variables globales
client = discord.Client()

# Définition des fonctions utilisées dans ce fichier
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
        print('Erreur la configuration n\'a pas pu être trouvée assurez vous d\'avoir bien un fichier config.json, \n et de l\'avoir correctement rempli')
    except:
        print('Oups! Une erreur inconnue est survenue lors du chargement de la configuration.')
    return bot_config

def logs(bot):
    """Chargement et écriture des logs."""
    if bot == 'dev':
        logger = logging.getLogger('discord')
        logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(filename='discord.dev.log', encoding='utf-8', mode='w')
        handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
        logger.addHandler(handler)
    else:
        logger = logging.getLogger('discord')
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
        handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
        logger.addHandler(handler)

def load_commands(self, extra_commands):
    for commands_module, config in extra_commands.items():
        self.info("Chargement du module: %s", commands_file)
        module = importlib.import_module(".commands.{}".format(commands_module),
                                         package="")
        commands_module, function = module.load()
        self.callbacks[(command_module)] = function

@client.event
async def on_ready():
    print('Connecté en tant que:')
    print(client.user.name)
    print(client.user.id)
    print('En cours d\'éxecution.')


# Code principal du bot, vérification des paramètres et chargement de la configuration
if len(sys.argv) < 2:
    help_bot()
    sys.exit(1)

param1 = sys.argv[1]
if len(sys.argv) > 3:
    param2 = sys.argv[2]

if param1 == "dev":
    config = load_config(param1)
    print(config['BOT_VERSION'])
    client.run(config['BOT_TOKEN'])
elif param1 == "prod":
    config = load_config(param1)
    print(config['BOT_VERSION'])
    client.run(config['BOT_TOKEN'])
elif param1 == "help":
    help_bot()
    sys.exit(1)
else:
    print('Erreur: la paramètre "{}" n\'est pas reconnu êtes vous sûr de l\'avoir correctement écrit et placé dans la commande?'.format(param1))
    help_bot()
    sys.exit(1)
