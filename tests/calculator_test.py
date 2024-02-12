from app import app
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_main_page(client):
    response = client.get("/")
    assert b"Calculator App" in response.data

def test_addition(client):
    response = client.post("/calculate", data={"number_one": "5", "number_two": "4", "operation": "add"})
    assert b"9.0" in response.data

def test_subtraction(client):
    response = client.post("/calculate", data={"number_one": "10", "number_two": "7", "operation": "subtract"})
    assert b"3.0" in response.data

def test_multiplication(client):
    response = client.post("/calculate", data={"number_one": "4", "number_two": "5", "operation": "multiply"})
    assert b"20.0" in response.data

def test_division(client):
    response = client.post("/calculate", data={"number_one": "12", "number_two": "3", "operation": "divide"})
    assert b"4.0" in response.data

def test_invalid_operation(client):
    response = client.post("/calculate", data={"number_one": "5", "number_two": "3", "operation": "invalid"})
    assert b"Error: Invalid operation" in response.data

def test_divide_by_zero(client):
    response = client.post("/calculate", data={"number_one": "10", "number_two": "0", "operation": "divide"})
    assert b"Error: Cannot divide by zero" in response.data
