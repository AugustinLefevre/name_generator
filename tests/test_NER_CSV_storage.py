from named_entity_reconizer.NER_CSV_storage import NER_CSV_storage
import unittest
import csv
import os

class test_NER_CVS_storage(unittest.TestCase):
    
    def teststorage(self):
        outputFile = "target/testStorageFile.csv"
        storage = NER_CSV_storage(outputFile)
        if os.path.exists(outputFile):
            os.remove(outputFile)
        with open(outputFile, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["firstname", "lastname", "location"])

        column_firstname = []
        column_lastname = []
        column_location = []

        with open(outputFile, mode="r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile) 
            for row in reader:
                if(row["firstname"] != ""):
                    column_firstname.append(row["firstname"])
                if(row["lastname"] != ""):
                    column_lastname.append(row["lastname"])
                if(row["location"] != ""):
                    column_location.append(row["location"])
        
        
        self.assertEqual(0, len(column_firstname))
        self.assertEqual(0, len(column_lastname))
        self.assertEqual(0, len(column_location))

        givenFirstname = ["titi", "toto", "tutu"]
        givenLastname = ["patati", "patata"]
        givenLocation = ["Paris"]

        storage.storeEntities(givenFirstname, givenLastname, givenLocation)

        with open(outputFile, mode="r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile) 
            for row in reader:
                if(row["firstname"] != ""):
                    column_firstname.append(row["firstname"])
                if(row["lastname"] != ""):
                    column_lastname.append(row["lastname"])
                if(row["location"] != ""):
                    column_location.append(row["location"])

        self.assertEqual(3, len(column_firstname))
        self.assertEqual(2, len(column_lastname))
        self.assertEqual(1, len(column_location))

        self.assertEqual(givenFirstname, column_firstname)
        self.assertEqual(givenLastname, column_lastname)
        self.assertEqual(givenLocation, column_location)

        column_firstname = []
        column_lastname = []
        column_location = []

        givenFirstname = ["tonton", "toto"]
        givenLastname = ["test1", "test5"]
        givenLocation = ["Paris", "Moscou"]

        storage.storeEntities(givenFirstname, givenLastname, givenLocation)

        with open(outputFile, mode="r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile) 
            for row in reader:
                if(row["firstname"] != ""):
                    column_firstname.append(row["firstname"])
                if(row["lastname"] != ""):
                    column_lastname.append(row["lastname"])
                if(row["location"] != ""):
                    column_location.append(row["location"])

        self.assertEqual(4, len(column_firstname))
        self.assertEqual(4, len(column_lastname))
        self.assertEqual(2, len(column_location))

        self.assertEqual(['titi', 'toto', 'tutu', 'tonton'], column_firstname)
        self.assertEqual(['patati', 'patata', 'test1', 'test5'], column_lastname)
        self.assertEqual(['Paris', 'Moscou'], column_location)

    def testoccurencestorage(self):
        occurence_output_file = "target/testFirstnameOccurrence.csv"
        storage = NER_CSV_storage(occurence_output_file)
        if os.path.exists(occurence_output_file):
            os.remove(occurence_output_file)
        with open(occurence_output_file, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["firstname", "occurrence"])

        firstnames_occurrences = {}

        with open(occurence_output_file, mode="r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile) 
            for row in reader:
                    firstnames_occurrences[row["firstname"]] = row["occurrence"]
        
        
        self.assertEqual(0, len(firstnames_occurrences))

        givenFirstname = ["titi", "toto", "tutu", "toto"]
        dict_names = {"titi" : "",
                      "toto" : "",
                      "tutu" : ""}

        storage.storeFirstnameOcurence(givenFirstname, dict_names)

        with open(occurence_output_file, mode="r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile) 
            for row in reader:
                firstnames_occurrences[row["firstname"]] = row["occurrence"]

        self.assertEqual(3, len(firstnames_occurrences))

        self.assertEqual(firstnames_occurrences["titi"], '1')
        self.assertEqual(firstnames_occurrences["toto"],'2')
        self.assertEqual(firstnames_occurrences["tutu"],'1')

        givenFirstname = ["tonton", "toto"]
        dict_names["tonton"] = ""

        storage.storeFirstnameOcurence(givenFirstname, dict_names)

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