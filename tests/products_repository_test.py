import pytest
from src.models.sqlite.settings.connection import SqliteConnectionHandle         # teste de integração
from src.models.sqlite.repository.products_repository import ProductsRepository

conn_handle = SqliteConnectionHandle()
conn = conn_handle.connect()

@pytest.mark.skip(reason='interacao com o banco')
def test_insert_products():
    repo = ProductsRepository(conn)

    name = "nome-teste2"
    price = "4,50"
    quantity = 8

    repo.insert_product(name, price, quantity)
    
@pytest.mark.skip(reason='interacao com o banco')
def test_find_product():
    repo = ProductsRepository(conn)

    name = "nome-teste2"
    response = repo.find_product_by_name(name)
    print(response)
    print(type(response))