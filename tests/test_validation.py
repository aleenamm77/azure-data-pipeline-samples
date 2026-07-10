import unittest
import pandas as pd

class TestValidation(unittest.TestCase):

    def test_no_missing_values(self):
        df = pd.read_csv("data/output.csv")
        self.assertEqual(df.isnull().sum().sum(), 0)

    def test_row_count(self):
        df = pd.read_csv("data/output.csv")
        self.assertGreater(len(df), 0)

if __name__ == "__main__":
    unittest.main()
