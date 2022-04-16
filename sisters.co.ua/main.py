import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor, as_completed
import re

BASE_URL = 'https://sisters.co.ua'


@dataclass
class Product:
    name: str
    category: str
    price: int
    brand: str
    img_link: str
    link_to_product: str

    volume: str = ''
    img_path: str = ''
    id: int = 0
    origin: str = ''
    gender: str = ''

    def download_data(self):
        pass


class ProductList:
    def __iter__(self):
        session = requests.Session()
        res = session.get(url)
        bs = BeautifulSoup(res.text, 'lxml')

    def __next__(self):
        pass


def pars_main(url: str) -> list:
    res = requests.get(url)
    bs = BeautifulSoup(res.text, 'lxml')
    cards_on_page = bs.find_all('div', class_='card')
    # links_list = []
    product_list = []
    for card in cards_on_page:
        link = BASE_URL + card.find('a').attrs['href']
        name = card.find('div', class_='card-inner').text.strip()
        category = card.find('div', class_='card-category').text.strip().strip('#')
        price = int(re.sub("[^0-9]", "", card.find('div', class_='card-price').text.strip()))
        img_link = BASE_URL + card.find('div', class_='card-image').find('a').attrs['href']
        brand = card.find('div', class_='card-brand').text.strip()
        product_list.append(Product(name, category, price, brand, img_link, link))
    print(product_list)
    print(url)
    return product_list

def pars_extra(product:Product):
    res = requests.get(product.link_to_product)
    bs = BeautifulSoup(res.text, 'lxml')
    volume= bs.find()
    img_path=
    id=
    origin=
    gender=








def pages_in_category(url: str) -> int:
    session = requests.Session()
    res = session.get(url)
    bs = BeautifulSoup(res.text, 'lxml')
    pag = bs.find_all('li', class_='next')
    return int(pag[-1].find('a').attrs['data-page']) + 1


def grabber(links: list, parser):
    with ThreadPoolExecutor(10) as executor:
        elements = []
        threads = []
        for page in links:
            threads.append(executor.submit(pars_main, url=page))
        for page in as_completed(threads):
            elements += page.result()
    print(elements)
    return elements



def collect_main_data():
    base_category_url = 'https://sisters.co.ua/kosmetyka-dlya-volossa/'
    pages_in_cat = pages_in_category(base_category_url)
    links_list = []
    for page in range(1, pages_in_cat+1):
        links_list.append(base_category_url+'page/'+str(page))
    grabber(links_list)


def collect_extra_data(data):
    pass




print(grabber())
