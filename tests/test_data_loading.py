import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
  
import unittest
from src.data_loading import load_dataset

class TestDataLoading(unittest.TestCase):
    def test_load_dataset(self):
        file_path = "data/modern_Data.csv"
        df = load_dataset(file_path)
        self.assertFalse(df.empty, "The dataset should not be empty")

if __name__ == "__main__":
    unittest.main()
