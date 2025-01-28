
from main.named_entity_reconizer import named_entity_reconizer
import unittest

class test_named_entity_reconizer(unittest.TestCase):

    ner = named_entity_reconizer()

    def testSimple(self):
        given = "Emmanuel Macron est le président de la France mange des banane."

        self.ner.parseText(given)
        actualFirstnames = self.ner.getFirstNnmes()
        actualLastnames = self.ner.getLastnames()
        actualLocations = self.ner.getLocations()

        self.assertEqual("Emmanuel", actualFirstnames[0])
        self.assertEqual("Macron", actualLastnames[0])
        self.assertEqual("la France", actualLocations[0])


    def testMultipleNames(self):
        given = "Jean-Claude Van Damme et Catherine Deneuve sont célèbres."
        self.ner.parseText(given)
        actualFirstnames = self.ner.getFirstnames()
        actualLastnames = self.ner.getLastnames()
        actualLocations = self.ner.getLocations()

        self.assertEqual("Jean-Claude", actualFirstnames[0])
        self.assertEqual("Van Damme", actualLastnames[0])
        self.assertEqual("Catherine", actualFirstnames[1])
        self.assertEqual("Deneuve", actualLastnames[1])
        self.assertEqual([], actualLocations)


    def testEntityWithMultipleWords(self):
        given = "Le président des États-Unis, Joe Biden, a donné un discours."
        self.ner.parseText(given)
        actualFirstnames = self.ner.getFirstnames()
        actualLastnames = self.ner.getLastnames()
        actualLocations = self.ner.getLocations()

        self.assertEqual("Joe", actualFirstnames[0])
        self.assertEqual("Biden", actualLastnames[0])
        self.assertEqual("États-Unis", actualLocations[0]) 

if __name__ == '__main__':
    unittest.main()
