import requests

def test_get_post_check_status():
    # Validamos que la API responda con un 200 (OK)
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200

def test_get_post_content():
    # Validamos que el ID del post sea el correcto
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    data = response.json()
    assert data['id'] == 1