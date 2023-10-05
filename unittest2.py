import unittest
from Assignment4 import RetrieveData

class TestRetrieveData(unittest.TestCase):
    def test_retrieve_data(self):
        
        weather_data = RetrieveData()
        self.assertIsNotNone(weather_data)  #Tests to make sure its actually retrieving some kind of data.

if __name__ == '__main__':
    unittest.main()