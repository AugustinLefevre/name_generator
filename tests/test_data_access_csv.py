import re
from data_access.data_access_csv import data_access_csv
import unittest
import os

class test_data_access_csv(unittest.TestCase):
    data_access = data_access_csv()
    script_dir = os.path.dirname(__file__)

    def test_get_rows(self):
        #given_file_path = os.path.join(self.script_dir, "ressources", "data_access_test.csv")
        actuals = self.data_access.get_rows("tests/ressources/data_access_test.csv")

        expecteds = [{'firstname': 'Titi', 'lastname': 'Toto'}]

        self.assertEqual(expecteds, actuals)

if __name__ == '__main__':
    unittest.main()