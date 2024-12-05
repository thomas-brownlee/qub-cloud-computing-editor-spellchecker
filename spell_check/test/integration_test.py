import pytest
from spell_check.src.app import app


@pytest.fixture
def client():
    """
    A test client for the Flask app.
    """
    with app.test_client() as client:
        yield client


def test_ping_endpoint(client):
    """
    Test the /api/spell-check/service/ping endpoint.
    """
    response = client.get('/api/spell-check/service/ping')

    # Assert the status code is 200
    assert response.status_code == 200

    # Assert the response headers return json and CORS is allowed
    assert response.headers["Content-Type"] == "application/json"
    assert response.headers["Access-Control-Allow-Origin"] == "*"

    # Assert the response JSON
    expected_data = {"status": "active"}
    assert response.json == expected_data

