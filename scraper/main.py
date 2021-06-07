# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# html = urlopen("https://doska.kg?/")
# # print(html.read())
# soup = BeautifulSoup(html)
# print(soup)
from products import get_products
from products import get_products
from utils import *
print("Welcome to parser: ")
welcome_name = input("Enter your name: ")
category_choise = input("Enter category: ")
for category_url in parse_catefory_links(get_html(BASE_URL)):
    print(get_products(get_html(category_choise)))
    import time
    time.sleep(5)
    print()
    print()
