import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


URL = "https://www.saucedemo.com/"

@pytest.mark.parametrize("username, password, expected_result", [
    ("standard_user", "secret_sauce", "success"),           
    ("locked_out_user", "secret_sauce", "error_locked"),    
    ("problem_user", "secret_sauce", "success"),            
])
def test_login_scenarios(page, username, password, expected_result):
    login_p = LoginPage(page)
    login_p.navigate()
    login_p.login(username, password)

    if expected_result == "success":
        assert "inventory.html" in page.url, f"{username} kullanıcısı giriş yapamadı!"
    
    elif expected_result == "error_locked":
        error_msg = login_p.get_error_message()
        assert "locked out" in error_msg, "Kilitli kullanıcı için beklenen hata mesajı gelmedi!"


def test_price_sorting_low_to_high(page):
    login_p = LoginPage(page)
    login_p.navigate()
    login_p.login("standard_user", "secret_sauce") 
    
    inventory_p = InventoryPage(page)
    inventory_p.sort_products_by("lohi")
    prices = inventory_p.get_all_prices()
    expected_sorted_prices = sorted(prices)
    assert prices == expected_sorted_prices

def test_add_to_cart(page):
    login_p = LoginPage(page)
    login_p.navigate()
    login_p.login("standard_user", "secret_sauce")

    inventory_p = InventoryPage(page)
    inventory_p.add_first_product_to_cart()
    assert inventory_p.get_cart_count() == 1