from app import app
with app.test_client() as c:
    response = c.get('/')
    assert response.status_code == 200

with app.test_client() as c:
    rv = c.post('/signUp', json={
        'name': 'esteban', 'email': 'data', 'password': 'papalina'
    })
    assert response.status_code == 200