import pytest
from playwright.sync_api import Playwright

def test_backend_product_service(playwright: Playwright):
    api_request = playwright.request.new_context(base_url="https://jsonplaceholder.typicode.com")
    
    response = api_request.get("/posts/1")
    
    assert response.ok, f"API Hatası! Status: {response.status}"
    
    data = response.json()
    
    assert "userId" in data
    assert "id" in data
    assert "title" in data
    
    print(f"\nAPI Test Başarılı! Çekilen Veri Başlığı: {data['title']}")