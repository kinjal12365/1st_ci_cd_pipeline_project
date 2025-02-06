from src.main import app

def app_check():
    response = app.test_client().get('/')

    assert response.status_code == 200