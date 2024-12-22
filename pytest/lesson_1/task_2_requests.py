import requests

class TestPetStore:

    def test_get_petstore_page(self):
        response = requests.get("https://petstore.swagger.io/#/pet/getPetById")
        assert response.status_code == 200, "Некорректный ответ от сервера"

    def test_add_new_pet(self):
        response = requests.post(
            url="https://petstore.swagger.io/v2/pet",
            json={
                "id": 123,
                "category": {
                    "id": 1,
                    "name": "test"
                },
                "name": "PugTestDog",
                "photoUrls": [
                    "https://i.pinimg.com/originals/09/48/d7/0948d75925d495545e4e3dd754a46847.jpg"
                ],
                "tags": [
                    {
                        "id": 1,
                        "name": "test"
                    }
                ],
                "status": "available"
            }
        )
        assert response.status_code == 200, "Не удалось добавить нового питомца"

    def test_find_pet_by_id(self):
        response = requests.get("https://petstore.swagger.io/v2/pet/123")
        data = response.json()
        expected_name = "PugTestDog"
        actual_name = data.get("name")
        assert expected_name == actual_name, f"Имена не совпадают {actual_name}"

    def test_delete_nonexistent_user_negative(self):
        response = requests.get("https://petstore.swagger.io/v2/user/0")
        assert response.status_code == 404, f"Ожидался код 404, а получен {response.status_code}"
