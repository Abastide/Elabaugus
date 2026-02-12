import elabapi_python

import main
from client import Client
from tools import lire_json
import tools
#from setuptools import setup

#setup(client_config = lire_json("connexion_client.json"),
#     client = Client(client_config),
#      )



import unittest


client_config = lire_json("connexion_client.json")
client = Client(client_config)


class Test_Elabftw(unittest.TestCase):

    def test_elabftw_version (self):

       
        version = client.elabftw_version()

        
        self.assertTrue(tools.check_version(version))



    def test_nb_exp(self) : 

        

        nb_expe = client.nb_expe()
        

        self.assertIsInstance(nb_expe, int)
        self.assertGreaterEqual(nb_expe, 0)



    def test_liste_exp(self) :

        
        liste_expe = client.liste_expe()

        self.assertIsInstance(liste_expe, list)
        self.assertIsNotNone(liste_expe)
        
        


if __name__ == "__main__":
    unittest.main()
