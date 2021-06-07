import peewee
from models import Category,Product

def find_all_categories():
    return Category.select()

def find_all_products():
    return Product.select()

products = find_all_products()
categories = find_all_categories()
for product in products:
    print(product.name)
    print(product.price)
    print(product.category)
for category in categories:
    print(category.name)