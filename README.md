# Cookie Clicker Bot ve Google Arama Otomasyonu

Bu proje, Selenium kullanarak Cookie Clicker oyununu otomatikleştiren ve Google'da arama yapıp belirli bir bağlantıya tıklayan Python betiklerini içerir.

## Gereksinimler

- Python 3.x
- Selenium
- ChromeDriver

## Kurulum

1. Gerekli Python paketlerini yükleyin:
    ```sh
    pip install selenium
    ```

2. ChromeDriver'ı indirin ve `chromedriver_path` değişkenine uygun yolu ekleyin.

## Kullanım

1. `cookie_clickers.py` dosyasını çalıştırarak Cookie Clicker oyununu otomatikleştirin:
    ```sh
    python cookie_clickers.py
    ```

2. `main.py` dosyasını çalıştırarak Google'da arama yapın ve belirli bir bağlantıya tıklayın:
    ```sh
    python main.py
    ```

## Dosya Yapısı

- `cookie_clickers.py`: Cookie Clicker oyununu otomatikleştiren betik.
- `main.py`: Google'da arama yapıp belirli bir bağlantıya tıklayan betik.
- `chromedriver`: ChromeDriver dosyası.

## cookie_clickers.py Açıklaması

Bu betik, Cookie Clicker oyununu otomatikleştirir. İşte betiğin nasıl çalıştığına dair detaylı bir açıklama:

1. **Tarayıcıyı Başlatma ve Oyunu Açma**:
    ```python
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    driver = webdriver.Chrome(executable_path='chromedriver_path')
    driver.get('https://orteil.dashnet.org/cookieclicker/')
    ```

2. **Cookie'ye Tıklama ve Cookie Sayısını Alma**:
    ```python
    cookie = driver.find_element(By.ID, 'bigCookie')
    cookies_id = 'cookies'
    product_price_prefix = 'productPrice'
    product_prefix = 'product'

    while True:
        cookie.click()
        cookies_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
        cookies_count = int(cookies_count.replace(",", ""))
        print(cookies_count)
    ```

3. **Ürün Fiyatlarını Kontrol Etme ve Satın Alma**:
    ```python
    for i in range(4):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")
        
        if not product_price.isdigit():
            continue

        product_price = int(product_price)

        if cookies_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break
    ```

Bu döngü, sürekli olarak cookie'ye tıklar ve yeterli cookie sayısına ulaşıldığında ürünleri satın alır.

## Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen bir pull request gönderin veya bir issue açın.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır.
