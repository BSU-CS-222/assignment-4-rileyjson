import json
import ssl
from urllib.request import urlopen
import unittest
from Assignment4 import RetrieveData

class TestURL(unittest.TestCase):
    
    def test_TestURL(self):
        #this is testing to make sure its fetching from the same URL defined below.
        url = "https://api.weather.gov/gridpoints/IND/83,90/forecast"  
        context = ssl._create_unverified_context()
        response = urlopen(url, context=context)
        test_data = json.loads(response.read())
        
        expected_weatherinfo = test_data
        actual_weatherinfo = RetrieveData()
        
        
        self.assertEqual(actual_weatherinfo, expected_weatherinfo)


            
        

if __name__ == '__main__':
    unittest.main()
