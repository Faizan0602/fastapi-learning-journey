from fastapi.testclient import TestClient
from Pytest import app

client = TestClient(app)

#Test Home API
def test_home():
    response=client.get("/")
    #STATUS CODE CHECK 
    assert response.status_code==200
    #RESPONSE DATA CHECK
    assert response.json()=={"message":"Hello Faizan"}
    
#TEST ADD API 
def test_add():
    response=client.get("/add?a=10&b=20")
    
    assert response.status_code==200
    assert response.json()=={"result":30}

