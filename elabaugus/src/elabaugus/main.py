import json
import argparse

from elabaugus.tools import lire_json
from elabaugus.client import Client



def main() :

    # conteneur pour les specifications d'arguments, possede des options 
    # parser de la commande principale elabaugus
    parser = argparse.ArgumentParser(
                    prog='elabaugus',
                    description='What the program does',
                    epilog='Text at the bottom of help')
    

    parser.add_argument('--config', required=True)

    subparsers = parser.add_subparsers(dest='commande', help='subcommand help')

    # parser de la sous-commande experience
    parser_expe =  subparsers.add_parser('experience')
    parser_expe.add_argument('action', choices=['liste', 'total'])
    
    #version
    parser_version = subparsers.add_parser('elabaugus_info')
    parser_version.add_argument('action', choices=['version'] )

    #json info
    parser_json = subparsers.add_parser('user')
    parser_json.add_argument('action', choices=['info'] )


    # definir les arguments
    ###parser.add_argument('chemin_fichier_config')

    # lance l'analyseur et stocke les résultats dans un objet 
    args = parser.parse_args()

    # client_config prend un fichier json, ca charge la config
    #with open(args.config) as f:
        #client_config = json.load(f)



    ###client_config = lire_json(args.chemin_fichier_config)
    client_config = lire_json(args.config)

    #creer le client
    elab_client = Client(client_config)

    if args.commande == 'user':
        if args.action == 'info':
            #affiche le contenue du json
            print(elab_client.client_config)


    if args.commande == 'elabaugus_info' :
        if args.action == 'version' :
            #affiche version elab   
            print(elab_client.elabftw_version())





    # affiche liste expe 
    if args.commande == 'experience':
        if args.action == 'liste' : 
            experiments = elab_client.liste_expe()


    if args.commande == 'experience':
        if args.action == 'total' : 
            total = elab_client.nb_expe()
            print(f"total: {total}")





if __name__ == "__main__":
    main()
