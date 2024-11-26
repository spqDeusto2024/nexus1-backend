

def test_root(test_client):
    response = test_client.get("/app/endpoints/role/healthz")
    assert response.status_code == 200
    assert response.json() == {"message": "The API is LIVE!!"}