import requests
from bs4 import BeautifulSoup

def process_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        products = soup.find_all('div', class_='product-wrapper')

        for product in products:
            module = product.find('h3', class_='wd-entities-title')
            price = product.find('span', class_='price')
            stock = product.find('span', class_='out-of-stock product-label')

            if module and price:  # Verifica tanto el módulo como el precio
                print("Módulo:", module.text.strip())
                print("Precio:", price.text.strip())

                if stock:
                    print("Stock:", stock.text.strip())
                else:
                    print("Stock: Disponible")
                
                print()

    else:
        print("No se pudo acceder al sitio:", response.status_code)

base_url = 'https://www.evophone.com.ar/categoria-producto/modulos/page/'
page_numbers = range(1, 15)

urls = [base_url + str(page) + '/' for page in page_numbers]

for url in urls:
    process_page(url)
