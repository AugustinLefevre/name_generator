import re
from main.web_scrapper import web_scrapper
from main.web_client import web_client
from unittest.mock import MagicMock
import unittest
import os

class test_web_scrapper(unittest.TestCase):
    ws = web_scrapper()
    script_dir = os.path.dirname(__file__)

    def test_getTexts(self):
        given_file_path = os.path.join(self.script_dir, "ressources", "html_exemple.html")
        given_file = open(given_file_path, "r")
        content = given_file.read()
        self.ws.web_client.get_content = MagicMock(return_value=content)
        url = "https://www.test.com"
        actual = self.ws.get_texts(url)

        expected_file_path = os.path.join(self.script_dir, "ressources", "texte_exemple.txt")
        expected_file = open(expected_file_path, "r")
        expected = expected_file.read()

        expected = re.sub(r'\s+', ' ', expected.strip())
        actual = re.sub(r'\s+', ' ', actual.strip())
        self.assertEqual(expected, actual)
        
        expected_file.close()
        given_file.close()

    
    def test_getLinks(self):
        given_file_path = os.path.join(self.script_dir, "ressources", "html_exemple.html")
        given_file = open(given_file_path, "r")
        content = given_file.read()
        self.ws.web_client.get_content = MagicMock(return_value=content)
        url = "https://www.test.com"
        actual = self.ws.get_links(url)

        expected = ['https://www.test.com/astu/index.php', 
                    'https://www.test.com/astu/internet/index.php', 
                    'https://www.test.com/tuto/compression/index.php',
                    'https://www.test.com#top']

        self.assertEqual(expected, actual)
        given_file.close()

    def test_scan_site_map(self):
        given_file_path = os.path.join(self.script_dir, "ressources", "html_exemple.html")
        given_file = open(given_file_path, "r")
        content = given_file.read()
        self.ws.web_client.get_content = MagicMock(return_value=content)

        given = ['https://www.test.com/astu/index.php#top',
                    'https://www.test.com/astu/internet/index.php',
                    'https://www.test.com/tuto/compression/index.php',]
        self.ws.get_links = MagicMock(return_value=given)

        url = "https://www.test.com"
        actual = self.ws.scan_site_map(url)

        self.assertTrue('https://www.test.com/tuto/compression/index.php' in actual)
        self.assertTrue('https://www.test.com/astu/internet/index.php' in actual)
        self.assertTrue('https://www.test.com/astu/index.php#top' in actual)
        self.assertTrue(len(actual) == 3)
        
        
        self.ws.get_links.assert_any_call('https://www.test.com/tuto/compression/index.php')
        self.ws.get_links.assert_any_call('https://www.test.com/astu/internet/index.php')
        self.ws.get_links.assert_any_call('https://www.test.com/astu/index.php#top')
        self.assertEqual(self.ws.get_links.call_count, 4)
        given_file.close()



if __name__ == '__main__':
    unittest.main()