class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.product_sort_container = page.locator(".product_sort_container")
        self.inventory_item_prices = page.locator(".inventory_item_price")
        self.shopping_cart_badge = page.locator(".shopping_cart_badge")

    def sort_products_by(self, option_value):
        self.product_sort_container.select_option(option_value)

    def get_all_prices(self):
        self.inventory_item_prices.first.wait_for()
        
        price_texts = self.inventory_item_prices.all_inner_texts()
        prices = [float(price.replace('$', '')) for price in price_texts]
        return prices

    def add_first_product_to_cart(self):
        self.page.locator("button:has-text('Add to cart')").first.click()

    def get_cart_count(self):
        return int(self.shopping_cart_badge.inner_text())