# ShopFlow QualityGuard - Automation Framework

This project is a hybrid test automation project with a **Page Object Model (POM)** ​​architecture, developed to validate the business processes of an e-commerce platform (SauceDemo).

## Project Features

* **UI Automation:** Playwright & Python
* **Architecture:** Page Object Model (POM)

* **Data-Driven Testing:** Different user profiles (Standard, Locked, Problem user) are tested in a single scenario.
* **API Testing:** An API test layer has been added for backend service controls.
* **Reporting:** Visual test reports with Pytest-HTML.
* **CI/CD:** Automatic test execution with GitHub Actions on every push.
* **Error Handling:** Automatic screenshot taking (Screenshot on Failure) when a test fails.

## Installation and Operation

1. **Clone the repository:**
```bash
git clone [https://github.com/kerememree/shopflow-test.git](https://github.com/kerememree/shopflow-test.git)
cd shopflow-test
```

2. **Install the requirements:**
```bash
pip install pytest-playwright pytest-html
playwright install
```

3. **Run the tests:**
```bash
python -m pytest --headed --html=report.html
```

## Test Scenarios

| ID | Test Name | Description |
| :--- | :--- | :--- |
| **TC01** | `test_login_scenarios` | Validates valid, invalid, and locked user logins. |
| **TC02** | `test_price_sorting` | Mathematically validates the "Low to High" sorting algorithm for products. |
| **TC03** | `test_add_to_cart` | Checks the add-to-cart function and cart counter. |
| **TC04** | `test_backend_service` | Validates API response codes and data integrity (JSON Schema). |

---------------------------------------------------------------------------------------------

# ShopFlow QualityGuard - Automation Framework

Bu proje, bir e-ticaret platformunun (SauceDemo) iş süreçlerini doğrulamak için geliştirilmiş, **Page Object Model (POM)** mimarisine sahip hibrit bir test otomasyon projesidir.

## Proje Özellikleri

* **UI Otomasyonu:** Playwright & Python
* **Mimari:** Page Object Model (POM) 
* **Data-Driven Testing:** Farklı kullanıcı profilleri (Standard, Locked, Problem user) tek senaryoda test edilmiştir.
* **API Testing:** Backend servis kontrolleri için API test katmanı eklenmiştir.
* **Raporlama:** Pytest-HTML ile görsel test raporları.
* **CI/CD:** GitHub Actions ile her push işleminde otomatik test koşumu.
* **Hata Yakalama:** Test başarısız olduğunda otomatik ekran görüntüsü (Screenshot on Failure) alma.

## Kurulum ve Çalıştırma

1.  **Repoyu klonlayın:**
    ```bash
    git clone [https://github.com/kerememree/shopflow-test.git](https://github.com/kerememree/shopflow-test.git)
    cd shopflow-test
    ```

2.  **Gereksinimleri yükleyin:**
    ```bash
    pip install pytest-playwright pytest-html
    playwright install
    ```

3.  **Testleri Çalıştırın:**
    ```bash
    python -m pytest --headed --html=report.html
    ```

## Test Senaryoları

| ID | Test Adı | Açıklama |
| :--- | :--- | :--- |
| **TC01** | `test_login_scenarios` | Geçerli, geçersiz ve kilitli kullanıcı girişlerini doğrular. |
| **TC02** | `test_price_sorting` | Ürünlerin "Low to High" sıralama algoritmasını matematiksel olarak doğrular. |
| **TC03** | `test_add_to_cart` | Sepete ekleme fonksiyonunu ve sepet sayacını kontrol eder. |
| **TC04** | `test_backend_service` | API yanıt kodlarını ve veri bütünlüğünü (JSON Schema) doğrular. |


