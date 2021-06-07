from utils import *
from bs4 import BeautifulSoup

def get_products(html):
    soup = BeautifulSoup(html)
    print(soup)

# get_products(get_html(BASE_URL))