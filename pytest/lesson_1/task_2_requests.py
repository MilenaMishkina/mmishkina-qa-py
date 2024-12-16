import requests

class TestPetStore:

    def test_get_petstore_page(self):
        response = requests.get("https://petstore.swagger.io/#/pet/getPetById")
        assert response.status_code == 200, "Некорректный ответ от сервера"

    def test_find_pet_by_id(self):
        response = requests.get("https://petstore.swagger.io/v2/pet/123")
        data = response.json()
        expected_name = "Labrador"
        actual_name = data.get('name')
        assert expected_name == actual_name, f'Имена не совпадают {actual_name}'

    def test_delete_nonexistent_user_negative(self):
        response = requests.get("https://petstore.swagger.io/v2/user/0")
        assert response.status_code == 404, "Некорректный ответ от сервера"
