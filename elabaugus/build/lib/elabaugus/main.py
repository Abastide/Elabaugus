import json
import argparse

from tools import lire_json
from client import Client




def main() :

    # conteneur pour les specifications d'arguments, possede des options 
    parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')
    
    # definir les arguments
    parser.add_argument('chemin_fichier_config')

    # lance l'analyseur et stocke les résultats dans un objet 
    args = parser.parse_args()

    # client_config prend un fichier json, ca charge la config 
    #with open(args.config) as f:
        #client_config = json.load(f)
    client_config = lire_json(args.chemin_fichier_config)
    
    #creer le client
    elab_client = Client(client_config)


    #affiche le contenue du json
    print(elab_client.client_config)

    #affiche version elab
    print(elab_client.elabftw_version())

    #elab_client.creaexpe("info", "journée de la presentation", "astro, presentation", "extraa", "number", "mw", 3, 50, "tomson", "extraa", "number", "mw", 3, 60)



    # affiche liste expe 
    experiments = elab_client.liste_expe()







if __name__ == "__main__":
    main()






