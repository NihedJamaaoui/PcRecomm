# from bs4 import BeautifulSoup
# import requests

# class DataExtraction:
#     @staticmethod
#     def fetch_data(url):
#         target_page = requests.get(url)
#         soup = BeautifulSoup(target_page.text, "html.parser")
#         return soup

#     @staticmethod
#     def extract_products(soup):
#         products_title = soup.findAll("h2", attrs={"class": "product-title"})
#         products_reference = soup.findAll("span", attrs={"class": "product-reference"})
#         products_description = soup.findAll("div", attrs={"class": "listds"})
#         products_prices = soup.findAll("span", attrs={"class": "price"})
#         return products_title, products_reference, products_description, products_prices
from bs4 import BeautifulSoup
import requests

class DataExtraction:
    @staticmethod
    def fetch_data(url):
        target_page = requests.get(url)
        soup = BeautifulSoup(target_page.text, "html.parser")
        return soup

    @staticmethod
    def extract_products(soup):
        products_title = soup.findAll("h2", attrs={"class": "product-title"})
        products_reference = soup.findAll("span", attrs={"class": "product-reference"})
        products_description = soup.findAll("div", attrs={"class": "listds"})
        products_prices = soup.findAll("span", attrs={"class": "price"})
        products_graphics = soup.findAll("span", attrs={"class": "graphics-card"})  # Assuming graphics card info is in this class
        return products_title, products_reference, products_description, products_prices, products_graphics




