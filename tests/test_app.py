from app import app

client = app.test_client()

def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_add_member():
    response = client.post(
        "/members",
        json={"name": "Sam", "program": "Weight Loss"}
    )
    assert response.status_code == 201


def test_get_members():
    response = client.get("/members")
    assert response.status_code == 200