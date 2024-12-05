"""
This is the Integration Test folder checking the behaviours of the test format

"""

import pytest

from spell_check.src.app import app


@pytest.fixture
def make_client():
    """
    A test client for the Flask app.
    """
    with app.test_client() as client:
        yield client


def test_ping_endpoint(client):
    """
    Test the /api/spell-check/service/ping endpoint.
    """
    response = client.get("/api/spell-check/service/ping")

    # Assert the status code is 200
    assert response.status_code == 200

    # Assert the response headers return json and CORS is allowed
    assert response.headers["Content-Type"] == "application/json"
    assert response.headers["Access-Control-Allow-Origin"] == "*"

    # Assert the response JSON
    expected_data = {"status": "active"}
    assert response.json == expected_data


def test_spell_check_endpoint_no_parameter_passed(client):
    """
    Test the /api/spell-check/service/ping endpoint.

    When no parameters are passed
    """
    response = client.get("/api/spell-check")

    # Assert the status code is 200
    assert response.status_code == 200

    # Assert the response headers return json and CORS is allowed
    assert response.headers["Content-Type"] == "application/json"
    assert response.headers["Access-Control-Allow-Origin"] == "*"

    # Assert the response JSON
    expected_data = {
        "error": True,
        "string": "Missing parameters - must have an text",
        "answer": 0,
    }
    assert response.json == expected_data


def test_spell_check_endpoint_string_pram_is_empty(client):
    """
    Test the /api/spell-check endpoint.

    When parameter is empty
    """
    response = client.get("/api/spell-check?text=")

    # Assert the status code is 200
    assert response.status_code == 200

    # Assert the response headers return json and CORS is allowed
    assert response.headers["Content-Type"] == "application/json"
    assert response.headers["Access-Control-Allow-Origin"] == "*"

    # Assert the response JSON
    expected_data = {
        "error": True,
        "string": "Empty parameters - Text is not a string",
        "answer": 0,
    }
    assert response.json == expected_data


def test_spell_check_endpoint_string_pram_is_valid_string_with_no_spelling_mistakes(
    client,
):
    """
    Test the /api/spell-check endpoint.

    When parameter is empty
    """
    response = client.get("/api/spell-check?text=hello world")

    # Assert the status code is 200
    assert response.status_code == 200

    # Assert the response headers return json and CORS is allowed
    assert response.headers["Content-Type"] == "application/json"
    assert response.headers["Access-Control-Allow-Origin"] == "*"

    # Assert the response JSON
    expected_data = {
        "error": False,
        "string": "There are no misspelled words in this text.",
        "answer": 0,
    }
    assert response.json == expected_data


def test_spell_check_endpoint_string_pram_is_valid_string_with_spelling_mistake(client):
    """
    Test the /api/spell-check endpoint.

    When parameter is empty
    """
    response = client.get("/api/spell-check?text=helo world")

    # Assert the status code is 200
    assert response.status_code == 200

    # Assert the response headers return json and CORS is allowed
    assert response.headers["Content-Type"] == "application/json"
    assert response.headers["Access-Control-Allow-Origin"] == "*"

    # Assert the response JSON
    expected_data = {
        "error": False,
        "string": "spelling mistake helo on line 0 did you mean help",
        "answer": 1,
    }
    assert response.json == expected_data


def test_spell_check_endpoint_string_pram_is_valid_string_with_spelling_mistakes(
    client,
):
    """
    Test the /api/spell-check endpoint.

    When parameter is empty
    """
    response = client.get("/api/spell-check?text=helo world thoms")

    # Assert the status code is 200
    assert response.status_code == 200

    # Assert the response headers return json and CORS is allowed
    assert response.headers["Content-Type"] == "application/json"
    assert response.headers["Access-Control-Allow-Origin"] == "*"

    # Assert the response JSON
    expected_data = {
        "error": False,
        "answer": 2,
    }
    assert response.json["error"] == expected_data["error"]
    assert response.json["answer"] == expected_data["answer"]
