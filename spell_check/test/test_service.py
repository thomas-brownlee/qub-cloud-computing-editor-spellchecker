import unittest
import requests
import os 

# gets the enc variable from the gitlab ci
test_url = os.getenv("JOB_VAR_TEST_URL", "http://127.0.0.1:80")

class TestSpellChecker(unittest.TestCase):
    """Testing class for the unit tests"""

    def test_average_length_endpoint_no_param(self):
        url = f"{test_url}/api/average-word-length"
        response = requests.get(url)

        self.assertEqual(response.status_code, 200)

        json_data = response.json()
        
        self.assertEqual(json_data["error"], True)
        self.assertEqual(json_data["string"], "Endpoint requires parameter .../?text=")
        self.assertEqual(json_data["answer"], 0)


    def test_average_length_endpoint_no_string_content(self):
        url = f"{test_url}/api/average-word-length/?text="
        response = requests.get(url)

        self.assertEqual(response.status_code, 200)

        json_data = response.json()
        
        self.assertEqual(json_data["error"], True)
        self.assertEqual(json_data["string"], "Parameter is empty, please add a parameters")
        self.assertEqual(json_data["answer"], 0)

    def test_average_length_endpoint_contains_ascii(self):
        url = f"{test_url}/api/average-word-length/?text=®"
        response = requests.get(url)

        self.assertEqual(response.status_code, 200)

        json_data = response.json()
        
        self.assertEqual(json_data["error"], True)
        self.assertEqual(json_data["string"], "Parameter is not ASCII")
        self.assertEqual(json_data["answer"], 0)

    def test_average_length_endpoint_contains_valid_string(self):
        url = f"{test_url}/api/average-word-length/?text=develop romeo bob"
        response = requests.get(url)

        self.assertEqual(response.status_code, 200)

        json_data = response.json()
        
        self.assertEqual(json_data["error"], False)
        self.assertEqual(json_data["string"], "Text's average word length is 5.")
        self.assertEqual(json_data["answer"], 5)

    def test_average_length_endpoint_bad_endpoint(self):
        url = f"{test_url}/test/?text=develop romeo bob"
        response = requests.get(url)

        self.assertEqual(response.status_code, 200)

        json_data = response.json()
        
        self.assertEqual(json_data["error"], True)
        self.assertEqual(json_data["string"], "Bad endpoint please use a correct endpoint")
        self.assertEqual(json_data["answer"], 0)

if __name__ == "__main__":
    unittest.main()
