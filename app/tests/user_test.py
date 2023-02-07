from fastapi.testclient import TestClient
from main import app
from typing import List
from app.user.entities.UserEntity import UserEntity
from datetime import datetime


client = TestClient(app)

def test_get_all_users():
    response = client.get("/users/test")
    res = [{"Name": "Ivan", "Email": "ivan@test.mx", "Password": "1234", "Estatus": "activo","AudFecha": '01/26/2023, 10:00:07', "FechaBaja": None,"FechaBloq": None}]
    print(response.json())
    assert response.json() == res