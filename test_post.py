from app import app

with app.test_client() as c:
    rv = c.post('/signUp', json={
        'name': 'esteban', 'email': 'data', 'password': 'papalina'
    })
    assert rv.status_code == 200
