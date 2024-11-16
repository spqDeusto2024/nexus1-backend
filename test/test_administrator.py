import pytest
from httpx import AsyncClient
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))
import main as app # Esto debería importar app.main correctamente


@pytest.mark.asyncio
async def test_create_user():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/users/", json={"username": "testuser", "email": "testuser@example.com"})
        assert response.status_code == 201
        assert response.json()["username"] == "testuser"

@pytest.mark.asyncio
async def test_get_user():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/users/1")
        assert response.status_code == 200
        assert response.json()["id"] == 1

@pytest.mark.asyncio
async def test_update_user():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.put("/users/1", json={"username": "updateduser"})
        assert response.status_code == 200
        assert response.json()["username"] == "updateduser"

@pytest.mark.asyncio
async def test_delete_user():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.delete("/users/1")
        assert response.status_code == 204
