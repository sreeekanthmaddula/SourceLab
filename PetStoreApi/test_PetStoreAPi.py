import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2"
pet_id = 123456  # Shared pet ID


@pytest.fixture(scope="module")
def create_pet():
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


def test_get_pet_by_id(create_pet):
    url = f"{BASE_URL}/pet/{create_pet}"

    response = requests.get(url)
    assert response.status_code == 200, f"Failed to get pet with ID {create_pet}. Status Code: {response.status_code}"

    pet_data = response.json()
    print(pet_data)
    assert pet_data["id"] == create_pet, f"Expected pet ID {create_pet}, but got {pet_data['id']}"


def test_update_pet(create_pet):
    url = f"{BASE_URL}/pet"
    payload = {
        "id": create_pet,
        "category": {
            "id": 1,
            "name": "Dog"
        },
        "name": "Fluffy Updated",
        "photoUrls": [
            "https://example.com/newphoto.jpg"
        ],
        "tags": [
            {
                "id": 1,
                "name": "Updated Tag"
            }
        ],
        "status": "sold"
    }

    response = requests.put(url, json=payload)
    assert response.status_code == 200, f"Failed to update pet. Status Code: {response.status_code}"

    pet_data = response.json()
    assert pet_data["name"] == "Fluffy Updated", f"Expected pet name 'Fluffy Updated', but got {pet_data['name']}"


def test_delete_pet(create_pet):
    url = f"{BASE_URL}/pet/{create_pet}"
    response = requests.delete(url)
    assert response.status_code == 200, f"Failed to delete pet with ID {create_pet}. Status Code: {response.status_code}"
    response_data = response.json()
    assert response_data.get("message") == str(create_pet), f"Expected message with pet ID {create_pet}, but got {response_data.get('message')}"
