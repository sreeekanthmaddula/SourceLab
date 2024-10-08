import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2"

@pytest.fixture(scope="module")
def create_pet():
    pet_id = 12345
    url = f"{BASE_URL}/pet"
    payload = {
        "id": pet_id,
        "category": {
            "id": 1,
            "name": "Dog"
        },
        "name": "Fluffy",
        "photoUrls": [
            "https://example.com/photo1.jpg"
        ],
        "tags": [
            {
                "id": 1,
                "name": "Tag1"
            }
        ],
        "status": "available"
    }

    response = requests.post(url, json=payload)
    assert response.status_code in [200, 201], f"Failed to create pet. Status Code: {response.status_code}"
    yield pet_id
    print("Pet created successfully")

@pytest.mark.sanity
@pytest.mark.regression
def test_invalid_json():
    url = f"{BASE_URL}/pet"
    invalid_payload = '{"id": 12345, "name": "Fluffy", "status": "available"'  # Missing closing brace

    response = requests.post(url, data=invalid_payload, headers={"Content-Type": "application/json"})
    assert response.status_code == 400, f"Expected 400 Bad Request, got {response.status_code}"

@pytest.mark.sanity
@pytest.mark.regression
def test_unauthorized_access():
    url = f"{BASE_URL}/pet"
    payload = {
        "id": 12346,
        "category": {
            "id": 1,
            "name": "Dog"
        },
        "name": "Buddy",
        "photoUrls": [
            "https://example.com/photo2.jpg"
        ],
        "tags": [
            {
                "id": 1,
                "name": "Tag2"
            }
        ],
        "status": "available"
    }

    response = requests.post(url, json=payload)
    assert response.status_code == 401, f"Expected 401 Unauthorized, got {response.status_code}"

@pytest.mark.regression
def test_sql_injection():
    url = f"{BASE_URL}/pet"
    payload = {
        "id": "1 OR 1=1",
        "category": {
            "id": 1,
            "name": "Dog"
        },
        "name": "Hacker",
        "photoUrls": [
            "https://example.com/photo3.jpg"
        ],
        "tags": [
            {
                "id": 1,
                "name": "Tag3"
            }
        ],
        "status": "available"
    }

    response = requests.post(url, json=payload)
    assert response.status_code == 400, f"Expected 400 Bad Request, got {response.status_code}"
@pytest.mark.sanity
@pytest.mark.regression
def test_missing_fields():
    url = f"{BASE_URL}/pet"
    payload = {
        "id": 12347,
        "category": {
            "id": 1,
            "name": "Dog"
        },
        "photoUrls": [
            "https://example.com/photo4.jpg"
        ],
        "tags": [
            {
                "id": 1,
                "name": "Tag4"
            }
        ],
        "status": "available"
    }

    response = requests.post(url, json=payload)
    assert response.status_code == 400, f"Expected 400 Bad Request, got {response.status_code}"
@pytest.mark.regression
def test_slow_response_time():
    url = f"{BASE_URL}/pet"
    payload = {
        "id": 12348,
        "category": {
            "id": 1,
            "name": "Dog"
        },
        "name": "Slowpoke",
        "photoUrls": [
            "https://example.com/photo5.jpg"
        ],
        "tags": [
            {
                "id": 1,
                "name": "Tag5"
            }
        ],
        "status": "available"
    }

    response = requests.post(url, json=payload)
    assert response.elapsed.total_seconds() < 5, f"Response time exceeded 5 seconds: {response.elapsed.total_seconds()} seconds"

# Add more tests for other bugs as needed

if __name__ == "__main__":
    pytest.main()
