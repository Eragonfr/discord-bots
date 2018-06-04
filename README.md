## Repository du bot discord Herobrine.
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e243badfedd94abfaecb3c34eb5d1c10)](https://www.codacy.com/app/Eragonfr/discord-bots)
[![GitHub release](https://img.shields.io/github/release/Eragonfr/discord-bots.svg)](https://github.com/Eragonfr/discord-bots)
[![Download Badge](https://img.shields.io/github/downloads/Eragonfr/discord-bots/total.svg)](https://github.com/Eragonfr/discord-bots/releases)
[![Requirements Status](https://requires.io/github/Eragonfr/discord-bots/requirements.svg?branch=master)](https://requires.io/github/Eragonfr/discord-bots/requirements/?branch=master)

Le bot est disponible
[ici](https://discordapp.com/oauth2/authorize?&client_id=428998328387371018&scope=bot&permissions=0)
en version de développement et
[ici](https://discordapp.com/oauth2/authorize?&client_id=428998234808254464&scope=bot&permissions=0)
en version bêta.

### Configuration et démarrage

La configuration du Bot est contenue dans un fichier `config.json` qui doit contenir au minimum:

```json
"beta":{
    "BOT_VERSION": "beta",
    "BOT_NAME": "Le nom du bot",
    "BOT_TOKEN": "LeTokenDeVotreBot",
    "BOT_PREFIX": "!",
    "BOT_COMMANDS": {"config": "True", "fun": "True"}
}
```
vous pouvez changer:
- Le préfixe du bot en changeant la valeur de `BOT_PREFIX`.
- Le nom du bot en changeant la valeur de `BOT_NAME`.
- Les fichiers de commandes à charger en changeant les valeurs de `BOT_COMMANDS`

Pour lancer le bot vous devez utiliser `python3 main.py dev` ou `./main.py dev`

### TODO:
- Chargement dynamique des fichiers de commandes.
- Créer un wiki.
