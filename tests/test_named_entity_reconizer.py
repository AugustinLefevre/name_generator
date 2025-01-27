
from main.named_entity_reconizer import named_entity_reconizer
import unittest

class test_named_entity_reconizer(unittest.TestCase):

    ner = named_entity_reconizer()

    def testSimple(self):
        given = "Emmanuel Macron est le président de la France mange des banane."

        self.ner.parseText(given)
        actualFirstNames = self.ner.getFistNames()
        actualLastNames = self.ner.getLastNames()
        actualLocations = self.ner.getLocations()

        self.assertEqual("Emmanuel", actualFirstNames[0])
        self.assertEqual("Macron", actualLastNames[0])
        self.assertEqual("la France", actualLocations[0])


    def testMultipleNames(self):
        given = "Jean-Claude Van Damme et Catherine Deneuve sont célèbres."
        self.ner.parseText(given)
        actualFirstNames = self.ner.getFistNames()
        actualLastNames = self.ner.getLastNames()
        actualLocations = self.ner.getLocations()

        self.assertEqual("Jean-Claude", actualFirstNames[0])
        self.assertEqual("Van Damme", actualLastNames[0])
        self.assertEqual("Catherine", actualFirstNames[1])
        self.assertEqual("Deneuve", actualLastNames[1])
        self.assertEqual([], actualLocations)


    def testEntityWithMultipleWords(self):
        given = "Le président des États-Unis, Joe Biden, a donné un discours."
        self.ner.parseText(given)
        actualFirstNames = self.ner.getFistNames()
        actualLastNames = self.ner.getLastNames()
        actualLocations = self.ner.getLocations()

        self.assertEqual("Joe", actualFirstNames[0])
        self.assertEqual("Biden", actualLastNames[0])
        self.assertEqual("États-Unis", actualLocations[0]) 

if __name__ == '__main__':
    unittest.main()
