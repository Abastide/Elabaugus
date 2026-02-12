import json
import logging

logger = logging.getLogger(__name__)


def lire_json(chemin_fichier_json):

    with open(chemin_fichier_json) as f:
            return  json.load(f)
    




def check_version(version):


    #si pas chaine cara alors false
    if isinstance (version, str) is False:
        logger.debug("la version n'est pas une chaine de caractère")
        return False
    
    #on met une version.splitn dans part_split pour decouper
    part_split = version.split('.')

    # si taille de split != de 3 alors false
    if len(part_split) != 3:
        return False
    
    #si chiffres alors true 
    if part_split[0].isnumeric() and part_split[1].isnumeric() and part_split[2].isnumeric():
        return True
    
    return False


