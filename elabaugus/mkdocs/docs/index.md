# Welcome to Augustin  

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.


##### La racine des commandes est celle-ci : pixi run elabaugus --config connexion_client.json

Puis par exemple, pour avoir le nombre d'experiences, 
il sufit de lancer les commandes: 'pixi run elabaugus --config connexion_client.json experience' 
On rentre dans experience et ensuite on veux le total, donc 
'pixi run elabaugus --config connexion_client.json experience total'.
Cela nous donne le nombre total d'experiences de l'utilisateur.

pour avoir la liste des experiences : 'pixi run elabaugus --config connexion_client.json experience liste'

-----------------------

Pour voir vos informations utilisateur : 'pixi run elabaugus --config connexion_client.json user info'

Dans 'user' puis ensuite la commande 'info'.

-----------------------

Pour avoir la version du elabftw sur lequel vous etes : 'pixi run elabaugus --config connexion_client.json elabaugus_info version'

On entre dans les informations d'elabaugus 'elabaugus_info', et ensuite on entre dans 'version' qui nous retourne sa version.


## Nombre total d'expériences

Pour avoir le nombre d'expériences, il suffit de lancer :

pixi run elabaugus --config connexion_client.json experience total

Résultat :

total: 8
