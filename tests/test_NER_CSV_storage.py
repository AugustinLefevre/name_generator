from named_entity_reconizer.NER_CSV_storage import NER_CSV_storage
import unittest
import csv
import os

class test_NER_CVS_storage(unittest.TestCase):

    def testoccurencestorage(self):
        occurence_output_file = "target/testFirstnameOccurrence.csv"
        storage = NER_CSV_storage(occurence_output_file)
        if os.path.exists(occurence_output_file):
            os.remove(occurence_output_file)
        with open(occurence_output_file, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["firstname", "occurrence","source"])

        firstnames_occurrences = {}

        with open(occurence_output_file, mode="r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile) 
            for row in reader:
                    firstnames_occurrences[row["firstname"]] = row["occurrence"]
        
        
        self.assertEqual(0, len(firstnames_occurrences))

        givenFirstname = ["titi", "toto", "tutu", "toto"]
        name_source = {"titi" : "titi va a la plage",
                      "toto" : "toto fait du sky",
                      "tutu" : "tutu va bien"}

        storage.storeFirstnameOcurence(givenFirstname, name_source)

        with open(occurence_output_file, mode="r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile) 
            for row in reader:
                firstnames_occurrences[row["firstname"]] = row["occurrence"]

        self.assertEqual(3, len(firstnames_occurrences))

        self.assertEqual(firstnames_occurrences["titi"], '1')
        self.assertEqual(firstnames_occurrences["toto"],'2')
        self.assertEqual(firstnames_occurrences["tutu"],'1')

        givenFirstname = ["tonton", "toto"]
        name_source["tonton"] = "tonton est la"

        storage.storeFirstnameOcurence(givenFirstname, name_source)

        with open(occurence_output_file, mode="r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile) 
            for row in reader:
                firstnames_occurrences[row["firstname"]] = row["occurrence"]

        self.assertEqual(4, len(firstnames_occurrences))

        self.assertEqual(firstnames_occurrences["titi"], '1')
        self.assertEqual(firstnames_occurrences["toto"], '3')
        self.assertEqual(firstnames_occurrences["tutu"], '1')
        self.assertEqual(firstnames_occurrences["tonton"], '1')
        

if __name__ == '__main__':
    unittest.main()