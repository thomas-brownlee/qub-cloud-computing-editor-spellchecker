"""Runs the end-to-end tests for the docker image"""

import unittest
from os import getenv

import requests

# gets the enc variable from the gitlab ci
test_url = getenv("JOB_VAR_TEST_URL", "http://127.0.0.1:80")


class TestSpellChecker(unittest.TestCase):
    """Testing class for the unit tests"""

    def test_ping_service(self):
        """Runs a test for the service ping"""
        url = f"{test_url}/api/spell-check/service/ping"
        response = requests.get(url, timeout=10)

        self.assertEqual(response.status_code, 200)

        json_data = response.json()

        self.assertEqual(json_data["status"], "active")

    def test_spell_check_endpoint_no_string_content(self):
        """Runs a test for the spell-check endpoint without a string text"""

        url = f"{test_url}/api/spell-check?test="
        response = requests.get(url, timeout=10)

        self.assertEqual(response.status_code, 200)

        json_data = response.json()

        self.assertEqual(True, json_data["error"])
        self.assertEqual("Missing parameters - must have an text", json_data["string"])
        self.assertEqual(json_data["answer"], 0)

    def test_spell_check_endpoint_normal_string(self):
        """Runs a test for the spell-check endpoint with a string text"""
        url = f"{test_url}/api/spell-check?text=hello hello"
        response = requests.get(url, timeout=10)

        self.assertEqual(response.status_code, 200)

        json_data = response.json()

        self.assertEqual(False, json_data["error"])
        self.assertEqual(
            "There are no misspelled words in this text.", json_data["string"]
        )
        self.assertEqual(json_data["answer"], 0)

    def test_spell_check_endpoint_normal_with_spelling_mistake(self):
        """Runs a test for the spell-check endpoint with a spelling mistake"""
        url = f"{test_url}/api/spell-check?text=hello helo"
        response = requests.get(url, timeout=10)

        self.assertEqual(response.status_code, 200)

        json_data = response.json()

        expected_string = "spelling mistake helo on line 0 did you mean help"
        self.assertEqual(False, json_data["error"])
        self.assertEqual(expected_string, json_data["string"])
        self.assertEqual(json_data["answer"], 1)


if __name__ == "__main__":
    unittest.main()
