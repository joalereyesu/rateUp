from app import app

with app.test_client() as c:
    rv = c.post('/signUp', json={
        'name': 'esteban', 'email': 'data', 'password': 'papalina'
    })
    print(rv.status_code)
    assert rv.status_code == 200


with app.test_client() as c:
    rv = c.post('/signIn', json={
        'username': 'estebansamayoa', 'password': 'papalina'
    })
    print(rv.status_code)
    assert rv.status_code == 200


with app.test_client() as c:
    rv = c.get('/homepage/estebansamayoa')
    print(rv.status_code)
    assert rv.status_code == 200



with app.test_client() as c:
    rv = c.get('/profile/estebansamayoa')
    print(rv.status_code)
    assert rv.status_code == 200

    