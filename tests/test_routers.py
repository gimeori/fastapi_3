import pytest
from httpx import AsyncClient
from main import app


@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client



async def test_get_authors(client):
    response = await client.get("/authors/")
    assert response.status_code == 200
    authors = response.json()
    assert isinstance(authors, list)



# async def test_get_author(client):
#     response = await client.get("/authors/100")
#     assert response.status_code == 404  # Предполагая, что автора с id=100 нет



async def test_create_author(client):
    data = {"name": "Test Author"}
    response = await client.post("/authors/", json=data)
    assert response.status_code == 201
    created_author = response.json()
    assert created_author["name"] == "Test Author"


async def test_get_books(client):
    response = await client.get("/books/")
    assert response.status_code == 200
    books = response.json()
    assert isinstance(books, list)



async def test_get_book(client):
    response = await client.get("/books/100")
    assert response.status_code == 404  # Предполагая, что книги с id=100 нет


async def test_create_book(client):
    data = {"title": "Test Book"}
    response = await client.post("/books/100", json=data)
    assert response.status_code == 404  # Предполагая, что автора с id=100 нет
