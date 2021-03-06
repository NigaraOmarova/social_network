import peewee
from datetime import datetime

from index import db

class BaseModel(peewee.Model):
    class Meta:
        database = db
class Category(BaseModel):
    category_id = peewee.PrimaryKeyField(null=False)
    name = peewee.CharField(max_length= 100,unique = True)
    created_at = peewee.DateTimeField(default=datetime.now())
    updated_at = peewee.DateTimeField(default=datetime.now())
class Meta:
    db_table = 'categories'
    order_by = ('created_at', )

class Product(BaseModel):
    product_id = peewee.PrimaryKeyField(null = False)
    name = peewee.CharField(max_length=150)
    price = peewee.DecimalField(max_digits=10, decimal_places=2, default=None)
    category = peewee.ForeignKeyField(Category, 
                                                related_name='fk_cat_prod', 
                                                to_field='category_id', 
                                                on_delete='cascade',
                                                on_update = 'cascade')
    created_at = peewee.DateTimeField(default=datetime.now())
    updated_at = peewee.DateTimeField(default=datetime.now())
class Meta:
    db_table = 'categories'
    order_by = ('created_at', )


db.connect()
Category.create_table()
Product.create_table()