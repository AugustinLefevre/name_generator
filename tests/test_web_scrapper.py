import re
from web_scrapper.web_scrapper import web_scrapper
from unittest.mock import MagicMock
import unittest
import os

class test_web_scrapper(unittest.TestCase):
    ws = web_scrapper("https://www.test.com")
    script_dir = os.path.dirname(__file__)

    def test_getTexts(self):
        given_file_path = os.path.join(self.script_dir, "ressources", "html_exemple.html")
        given_file = open(given_file_path, "r")
        content = given_file.read()
        self.ws.web_client.get_content = MagicMock(return_value=content)
        actual = self.ws.get_texts("https://www.test.com")

        given_file.close()
        expected = ['\nLes Astuces\nInternet\n',
                    '\nLes Tutoriaux\nCompression\n',
                    ' Et un paragraphe avec du texte en gras\n\n        et un retour Ã\xa0 la ligne.\n        ']

        self.assertEqual(expected, actual)
        
        

    
    def test_getLinks(self):
        given_file_path = os.path.join(self.script_dir, "ressources", "html_exemple.html")
        given_file = open(given_file_path, "r")
        content = given_file.read()
        given_file.close()
        self.ws.web_client.get_content = MagicMock(return_value=content)
        actual = self.ws.get_links()

        expected = ['https://www.test.com/astu/index.php', 
                    'https://www.test.com/astu/internet/index.php', 
                    'https://www.test.com/tuto/compression/index.php',
                    'https://www.test.com#top']

        self.assertEqual(expected, actual)
        

    def test_scan_site_map(self):
        given_file_path = os.path.join(self.script_dir, "ressources", "html_exemple.html")
        given_file = open(given_file_path, "r")
        content = given_file.read()
        given_file.close()
        self.ws.web_client.get_content = MagicMock(return_value=content)

        given = ['https://www.test.com/astu/index.php#top',
                    'https://www.test.com/astu/internet/index.php',
                    'https://www.test.com/tuto/compression/index.php',]
        self.ws.get_links = MagicMock(return_value=given)

        actual = self.ws.scan_site_map("https://www.test.com")

        self.assertTrue('https://www.test.com/tuto/compression/index.php' in actual)
        self.assertTrue('https://www.test.com/astu/internet/index.php' in actual)
        self.assertTrue('https://www.test.com/astu/index.php#top' in actual)
        self.assertTrue(len(actual) == 3)
        
        
    #    self.ws.get_links.assert_any_call('https://www.test.com/tuto/compression/index.php')
    #    self.ws.get_links.assert_any_call('https://www.test.com/astu/internet/index.php')
    #    self.ws.get_links.assert_any_call('https://www.test.com/astu/index.php#top')
    #    self.assertEqual(self.ws.get_links.call_count, 4)
        



if __name__ == '__main__':
    unittest.main()