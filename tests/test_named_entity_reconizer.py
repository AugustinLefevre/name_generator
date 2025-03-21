
from named_entity_reconizer.named_entity_reconizer import named_entity_reconizer
import unittest

class test_named_entity_reconizer(unittest.TestCase):

    ner = named_entity_reconizer()

    def testSimple(self):
        given = "Emmanuel Macron est le président de la France mange des banane."

        self.ner.parseText(given)
        actualFirstnames = self.ner.getFirstnames()

        self.assertEqual("Emmanuel", actualFirstnames[0])


    def testMultipleNames(self):
        given = "Jean-Claude Van Damme et Catherine Deneuve sont célèbres."
        self.ner.parseText(given)
        actualFirstnames = self.ner.getFirstnames()

        self.assertEqual("Jean", actualFirstnames[0])
        self.assertEqual("Claude", actualFirstnames[1])
        self.assertEqual("Catherine", actualFirstnames[2])


    def testEntityWithMultipleWords(self):
        given = "Le président des États-Unis, Joe Biden, a donné un discours."
        self.ner.parseText(given)
        actualFirstnames = self.ner.getFirstnames()

        self.assertEqual("Joe", actualFirstnames[0])

    def testWithProblematicWord(self):
        given = "Bonjour Madame"
        self.ner.parseText(given)
        actualFirstnames = self.ner.getFirstnames()

        self.assertEqual(0, len(actualFirstnames))

        given = "Bonjour Monsieur"
        self.ner.parseText(given)
        actualFirstnames = self.ner.getFirstnames()

        self.assertEqual(0, len(actualFirstnames))

    def testisAName(self):
        self.assertTrue(self.ner.is_a_name("Teo", ""))
        self.assertFalse(self.ner.is_a_name("T-o", ""))
        self.assertFalse(self.ner.is_a_name("The", ""))
        self.assertTrue(self.ner.is_a_name("Tim", ""))

    def testWithProblematicWord2(self):
        given = "Le Petit Chose a d’abord été un simple bulletin de l’association "
        self.ner.parseText(given)
        actualFirstnames = self.ner.getFirstnames()

        self.assertEqual(0, len(actualFirstnames))

    def testWithProblematicWord3(self):
        given = "le décès d’une fille du Comte d’Artois3"

        self.ner.parseText(given)
        actualFirstnames = self.ner.getFirstnames()

        self.assertEqual(0, len(actualFirstnames))

    def testWithProblematicWord4(self):
        given = "Offrez à votre enfant une aventure magique"

        self.ner.parseText(given)
        actualFirstnames = self.ner.getFirstnames()

        self.assertEqual(0, len(actualFirstnames))

    def testWithProblematicWord4(self):
        given = "Allez, Lucas, chante pour nous !"
        self.ner.parseText(given)
        actualFirstnames = self.ner.getFirstnames()

        self.assertEqual(1, len(actualFirstnames))
        self.assertEqual("Lucas", actualFirstnames[0])


if __name__ == '__main__':
    unittest.main()
