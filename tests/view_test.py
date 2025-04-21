import pytest
from httpx import AsyncClient

from svc_example.views import app

@pytest.mark.asyncio
async def test_app():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_hello():
    assert True