# import urllib.request
from bs4 import BeautifulSoup
# from urllib.request import urlopen
# from header import header
import time
from utils import *

# BASE_URL = "http://lalafo.kg"
# def get_html(url):
#     request = urllib.request.Request(url=url,headers=header)
#     html = urlopen(request)
#     return html

def parse_catefory_links(html):
    soup = BeautifulSoup(html)
    div_nav_container = soup.find("div", {"class": "main-nav__container"})
    li_tags = div_nav_container.find("ul",{"class":"main-nav__first-level-list"}).children
    category_links = set ()
    for li in li_tags:
        if not li.a:
            continue
        category_links.add(BASE_URL + li.a["href"])
    return category_links
# if __name__ == '__main__'
    # print(category_links)
        # print(li)
        # time.sleep(3)
        # print()
        # print()
        # print(li.a.get("href"))
parse_catefory_links(utils.get_html(BASE_URL))


