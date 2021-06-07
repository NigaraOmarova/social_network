# import requests
# from bs4 import BeautifulSoup
# import csv

# def get_html(url):
#     response = requests.get(url)
#     return response.text

# def write_to_csv(data):
#     with open("project.csv", "a") as csv_file:
#         writer = csv.writer(csv_file, delimiter=' ')
#         writer.writerow([data["news"]])

# def get_names(html):
#     soup = BeautifulSoup(html, 'lxml')
#     titles = soup.find("div", class_ = "itemList").find_all("div", class_ = "itemBody")
#     for title in titles:
#         news = title.a.text
#         print()
#         print()
#         news.strip()
#         print(news)
#         data = {"news": news}
#         write_to_csv(data)

# def main():
#     news_url = "https://vesti.kg/"
#     print(get_html(news_url))
#     print(get_names(get_html(news_url)))

# main()

import requests
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    return response.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    last_page = soup.find_all("li")[-19]
    total_page = last_page.find('a').get("href").split('=')[-1]
    return int(total_page)

# with open("project.csv", "a") as csv_file:
#         writer = csv.writer(csv_file, delimiter='/')
#         writer.writerow((data["title"],
#                          data["price"],
#                          data["properties"],
#                          data["image"]))

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    product_list_1 = soup.find("div", class_= "search-results-table").find_all('div', class_ = 'list-item list-label')
    product_list_2 = soup.find("div", class_= "search-results-table").find_all('div', class_ = 'list-item list-label new-line')
    product_all = product_list_1 + product_list_2
    
    for product in product_all:
        try:
            image = product.a.find("div", {"class":"thumb-item-carousel"}).find("img").get("data-src")
            print(image)
        except:
            image = ''
        try:
            price = product.find("p", {"class":"price"}).find("strong").text
            print(price)
        except:
            price = ''
        try:
            description = product.find("div", {"class":"item-info-wrapper"}).find("p")
            print(description)
        except:
            description =" "
        try:
            title = product.find('h2', class_='name').text.replace(' ','')
            print(title)
        except:
            title = " "

       
        # data = {"title":title, "price": price, "properties": properties, "image":image}
        # write_to_csv(data)     
        
def main():
    cars_url = "https://m.mashina.kg/search/all/"
    pages = '?page='
    print(get_total_pages(get_html(cars_url)))
    print(get_page_data(get_html(cars_url)))
   


main()