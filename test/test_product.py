from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# def test_read_product(db_session):
#   response = client.get("/api/v1/products/1")
#   assert response.status_code == 200
#   assert response.json() == {
#     "id": 39,
#     "name": "와이드 슬랙스",
#     "price": 56000.00,
#     "description": "편한 와이드 슬랙스입니다. 롱 기장으로 발등을 덮어 다리를 더 길게 보여줍니다. 여름에는 물론 가을까지 활용할 수 있는 아이템이에요!",
#     "image_url": "https://nb2at4ndwbwcrxzp.public.blob.vercel-storage.com/slacks1-yci6AUlyOlpNWrnGXwJkQNUarqMt2v.jpg",
#     "category_id": 2
#  }
  

def test_create_product_and_read_product(db_session):
    product_data = {
        "name": "와이드 슬랙스",
        "price": 56000.00,
        "description": "편한 와이드 슬랙스입니다. 롱 기장으로 발등을 덮어 다리를 더 길게 보여줍니다. 여름에는 물론 가을까지 활용할 수 있는 아이템이에요!",
        "image_url": "https://nb2at4ndwbwcrxzp.public.blob.vercel-storage.com/slacks1-yci6AUlyOlpNWrnGXwJkQNUarqMt2v.jpg",
        "category_id": 2
    }
    expected_response = {
        "id": 1,
        "name": "와이드 슬랙스",
        "price": 56000.00,
        "description": "편한 와이드 슬랙스입니다. 롱 기장으로 발등을 덮어 다리를 더 길게 보여줍니다. 여름에는 물론 가을까지 활용할 수 있는 아이템이에요!",
        "image_url": "https://nb2at4ndwbwcrxzp.public.blob.vercel-storage.com/slacks1-yci6AUlyOlpNWrnGXwJkQNUarqMt2v.jpg",
        "category_id": 2
    }
    response = client.post("/api/v1/products/", json=product_data)
    assert response.status_code == 200
    assert response.json() == expected_response

    #### read
    response = client.get("/api/v1/products/1")
    assert response.status_code == 200
    assert response.json() == expected_response

    #### update
    update_data = {
        "name": "와이드 슬랙스",
        "price": 56000.00,
        "description": "편한 와이드 슬랙스입니다. 롱 기장으로 발등을 덮어 다리를 더 길게 보여줍니다. 여름에는 물론 가을까지 활용할 수 있는 아이템이에요!",
        "image_url": "https://nb2at4ndwbwcrxzp.public.blob.vercel-storage.com/slacks1-yci6AUlyOlpNWrnGXwJkQNUarqMt2v.jpg",
        "category_id": 2
    }
    expected_response = {
      "id": 1,    
      "name": "와이드 슬랙스",
      "price": 56000.00,
      "description": "편한 와이드 슬랙스입니다. 롱 기장으로 발등을 덮어 다리를 더 길게 보여줍니다. 여름에는 물론 가을까지 활용할 수 있는 아이템이에요!",
      "image_url": "https://nb2at4ndwbwcrxzp.public.blob.vercel-storage.com/slacks1-yci6AUlyOlpNWrnGXwJkQNUarqMt2v.jpg",
      "category_id": 2
    }
    response = client.put("/api/v1/products/1", json=update_data)
    assert response.status_code == 200
    response = client.get("/api/v1/products/1")
    assert response.status_code == 200
    assert response.json() == expected_response

    #### delete
    response = client.delete(f"/api/v1/products/1")
    assert response.status_code == 200
    response = client.get(f"/api/v1/products/1")
    assert response.status_code == 404


       

    

# def test_update_product(db_session):
#   product_data = {
#     "name": "와이드 슬랙스",
#     "price": 56000.00,
#     "description": "편한 와이드 슬랙스입니다. 롱 기장으로 발등을 덮어 다리를 더 길게 보여줍니다. 여름에는 물론 가을까지 활용할 수 있는 아이템이에요!",
#     "image_url": "https://nb2at4ndwbwcrxzp.public.blob.vercel-storage.com/slacks1-yci6AUlyOlpNWrnGXwJkQNUarqMt2v.jpg",
#     "category_id": 2
#   }
#   response = client.put("/api/v1/products/1", json=product_data)
#   assert response.status_code == 200
#   assert response.json()["name"] == "Updated Product 1"
#   assert response.json()["price"] == 19.99
#   assert response.json()["description"] == "This is the updated product 1"

# def test_delete_product(db_session):
#     response = client.delete("/api/v1/products/12")
#     assert response.status_code == 200
#     assert response.json()["name"] == "Updated Product 1"
#     assert response.json()["price"] == 19.99
#     assert response.json()["description"] == "This is the updated product 1"