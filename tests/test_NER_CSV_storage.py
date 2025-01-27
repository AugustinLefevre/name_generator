from main.NER_CSV_storage import NER_CSV_storage
import unittest
import csv
import os

class test_NER_CVS_storage(unittest.TestCase):
    
    outputFile = "target/testStorageFile.csv"
    storage = NER_CSV_storage(outputFile)


    def teststorage(self):

        if os.path.exists(self.outputFile):
            os.remove(self.outputFile)
        with open(self.outputFile, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["firstname", "lastname", "location"])

        column_firstname = []
        column_lastname = []
        column_location = []

        with open(self.outputFile, mode="r", newline="", encoding="utf-8") as csvfile:
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

        self.storage.storeEntities(givenFirstname, givenLastname, givenLocation)

        with open(self.outputFile, mode="r", newline="", encoding="utf-8") as csvfile:
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

        self.storage.storeEntities(givenFirstname, givenLastname, givenLocation)

        with open(self.outputFile, mode="r", newline="", encoding="utf-8") as csvfile:
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
        

if __name__ == '__main__':
    unittest.main()