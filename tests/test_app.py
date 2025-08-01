from http import HTTPStatus


def test_root_deve_retornar_ola_mundo(client):
    response = client.get('/')

    assert (
        response.text
        == """
    <html>
        <head>
            <title>Olá mundo</title>
        </head>
        <body>
            <h1>Olá mundo</h1>
        </body>
    </html>
    """
    )
    assert response.status_code == HTTPStatus.OK


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'Alice',
            'password': '123456',
            'email': 'alice@example.com',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'Alice',
        'email': 'alice@example.com',
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [{'id': 1, 'username': 'Alice', 'email': 'alice@example.com'}]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'password': 'secret',
            'email': 'bob@example.com',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'bob',
        'email': 'bob@example.com',
    }


def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'email': 'bob@example.com',
        'username': 'bob',
        'id': 1,
    }
