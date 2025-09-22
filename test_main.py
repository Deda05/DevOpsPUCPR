from fastapi.testclient import TestClient
from main import app, Estudante
import random

client = TestClient(app)

# 1. Teste para root (/)
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

# 2. Teste para a rota /teste1
def test_funcaoteste_return_true():
    response = client.get("/teste1")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["teste"] is True
    assert "NumAleatorio" in json_data
    # Garante que o número aleatório está no intervalo esperado
    assert 0 <= json_data["NumAleatorio"] <= 100000

# 3. Teste para a rota de cadastro de estudante
def test_create_estudante():
    estudante_data = {
        "name": "João",
        "curso": "Engenharia de Software",
        "ativo": True
    }
    response = client.post("/estudantes/cadastro", json=estudante_data)
    assert response.status_code == 200
    assert response.json() == estudante_data

# 4. Teste para a rota de atualização de estudante com um ID válido
def test_update_valid_estudante():
    response = client.put("/estudantes/update/123")
    assert response.status_code == 200
    assert response.json() is True

# 5. Teste para a rota de exclusão de estudante com um ID válido
def test_delete_valid_estudante():
    response = client.delete("/estudantes/delete/456")
    assert response.status_code == 200
    assert response.json() is True
