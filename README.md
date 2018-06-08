## Repository du bot discord Herobrine.
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e243badfedd94abfaecb3c34eb5d1c10)](https://www.codacy.com/app/Eragonfr/discord-bots)
[![GitHub release](https://img.shields.io/github/release/Eragonfr/discord-bots.svg)](https://github.com/Eragonfr/discord-bots)
[![Requirements Status](https://requires.io/github/Eragonfr/discord-bots/requirements.svg?branch=master)](https://requires.io/github/Eragonfr/discord-bots/requirements/?branch=master)

Le bot est disponible
[ici](https://discordapp.com/oauth2/authorize?&client_id=428998328387371018&scope=bot&permissions=0)
en version de développement et
[ici](https://discordapp.com/oauth2/authorize?&client_id=428998234808254464&scope=bot&permissions=0)
en version bêta.

### Configuration et démarrage

La configuration du Bot est contenue dans un fichier `config.ini` qui doit contenir au minimum:

```ini
[beta]
version = beta
name = Herobrine
token = YourTokenHere
prefix = !
staff_role = Staff
commands = ['bots.admin', 'bots.fun', 'bots.herobrine']
```
vous pouvez changer:
- Le préfixe du bot en changeant la valeur de `prefix`.
- Le nom du role staff en changeant la valeur de `staff_role`(le rôle staff peux faire certaines commandes suplémentaires).
- Les fichiers de commandes à charger en changeant les valeurs de `comamnds`

Pour lancer le bot vous devez utiliser `python3 main.py dev` ou `./main.py dev`

### TODO:
- Utilisation d'une base de données SQLite.
- Créer un wiki.
