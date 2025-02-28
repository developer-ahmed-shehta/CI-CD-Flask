import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from main import app


# Pytest fixture to set up the Flask test client
@pytest.fixture
def client():
    # Configure Flask to run in testing mode
    app.config['TESTING'] = True

    # Create a test client for the Flask app
    with app.test_client() as client:
        yield client


# Test function for the root route
def test_hello_world(client):
    # Send a GET request to the root URL
    rv = client.get('/')

    # Check that the status code is 200 (OK)
    assert rv.status_code == 200

    # Verify that the response data contains the expected text
    assert b'Hello, CI/CD World!' in rv.data


# Test function for the /goodbye route
def test_goodbye_world(client):
    # Send a GET request to the /goodbye URL
    rv = client.get('/goodbye')

    # Check that the status code is 200 (OK)
    assert rv.status_code == 200

    # Verify that the response data contains the expected text
    assert b'Hi, Ali' in rv.data
