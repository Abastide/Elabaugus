import logging
import unittest
import tools


class Test_Tools(unittest.TestCase):

    def test_lire_json(self):

        client_config = tools.lire_json("test_tools.json")        


        self.assertIsInstance(client_config, dict)

        self.assertEqual(list(client_config.keys()), ['API_KEY', 'API_HOST', 'PORT'])

        #self.assertIsInstance(client_config.keys(), (str, str, int))
        self.assertIsInstance(client_config['API_KEY'], str)
        self.assertIsInstance(client_config['API_HOST'], str)
        self.assertIsInstance(client_config['PORT'], int)

        self.assertEqual(client_config['API_KEY'], "1-123456789")
        self.assertEqual(client_config['PORT'], 1234)

        #self.assertCountEqual()



 


    def test_check_version(self):


        self.assertFalse(tools.check_version(None)) 
        self.assertTrue(tools.check_version("1.2.3"))
        self.assertFalse(tools.check_version("toto"))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
