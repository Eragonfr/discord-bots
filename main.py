#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Code principal du bot, vérification des paramètres
et chargement de la configuration
"""
# import asyncio
# import discord
import sys
from bots.functions import LoadFunctions

if len(sys.argv) < 2:
    LoadFunctions.help_bot(sys.argv)
    sys.exit(1)

param1 = sys.argv[1]
if len(sys.argv) > 3:
    param2 = sys.argv[2]
    if len(sys.argv) > 4:
        param3 = sys.argv[3]

if param1 == "dev":
    config = LoadFunctions.load_config(param1)
    LoadFunctions.run(config)
elif param1 == "beta":
    config = LoadFunctions.load_config(param1)
    LoadFunctions.run(config)
elif param1 == "help" or param1 == "-h" or param1 == "--help" or\
     param2 == "help" or param2 == "-h" or param2 == "--help":
    LoadFunctions.help_bot(sys.argv)
    sys.exit(1)
else:
    print('Erreur: la paramètre "{}" n\'est pas reconnu êtes vous sûr de l\'\
avoir correctement écrit et placé dans la commande?'.format(param1))
    LoadFunctions.help_bot(sys.argv)
    sys.exit(1)
