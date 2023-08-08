import requests
from bs4 import BeautifulSoup

urls = [
    'https://www.evophone.com.ar/categoria-producto/modulos/page/1/',
    'https://www.evophone.com.ar/categoria-producto/modulos/page/2/',
    'https://www.evophone.com.ar/categoria-producto/modulos/page/3/',
    'https://www.evophone.com.ar/categoria-producto/modulos/page/4/ '] 

print("Módulos disponibles:")
#Primer Proceso
for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        # Objetivo 1: Obtener los nombres de los módulos en la página
        modules = soup.find_all('h3', class_='wd-entities-title')
        
        for module in modules:
            print(module.text.strip())

 
        

    else:
                print("No se pudo acceder al sitio:", response.status_code)

#Segundo Proceso
for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

     
        # Objetivo 2: Obtener los precios de los módulos en la página
        prices = soup.find_all('span', class_='woocommerce-Price-amount amount')
        print("\nPrecios:")
        for price in prices:
            print(price.text)
        

    else:
                print("No se pudo acceder al sitio:", response.status_code)