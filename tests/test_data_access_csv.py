from data_access.data_access_csv import data_access_csv
import unittest
import os
import shutil

class test_data_access_csv(unittest.TestCase):
    data_access = data_access_csv()
    script_dir = os.path.dirname(__file__)

    def test_get_rows(self):
        actuals = self.data_access.get_rows("tests/ressources/data_access_test.csv")

        expecteds = [{'firstname': 'Titi', 'lastname': 'Toto'}, {'firstname': 'Tata', 'lastname': 'Tutu'}]

        self.assertEqual(expecteds, actuals)

    def test_get_headers(self):
        actuals = self.data_access.get_headers("tests/ressources/data_access_test.csv")

        expecteds = ['firstname', 'lastname']

        self.assertEqual(expecteds, actuals)

    def test_overwrite(self):
        source = "tests/ressources/data_access_test.csv"
        destination = "tests/ressources/tmp_data_access_test.csv"

        with open(source, "rb") as f_source, open(destination, "wb") as f_dest:
            contenu = f_source.read()
            f_dest.write(contenu)
        given = [{'firstname': 'Titi', 'lastname': 'Tata'}]

        self.data_access.overwrite(destination, given)

        actuals = self.data_access.get_rows(destination)
        self.assertEqual(given, actuals)

        os.remove(destination)

    def test_get_column(self):
        column_firstname = self.data_access.get_column("tests/ressources/data_access_test.csv", "firstname")
        self.assertEqual(["Titi", "Tata"], column_firstname)
        column_lastname = self.data_access.get_column("tests/ressources/data_access_test.csv", "lastname")
        self.assertEqual(["Toto", "Tutu"], column_lastname)

    def test_get_map(self):
        actual = self.data_access.get_map("tests/ressources/data_access_test.csv", "firstname", "lastname")
        expected = {
            "Titi" : "Toto",
            "Tata" : "Tutu"
        }
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()