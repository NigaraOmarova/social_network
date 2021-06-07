# import peewee
# from models import Category, Product

# def add_category(name):
#     try:
#         row = Category(name=name.lower().strip())
#         row.save()
#         print('Saved!')
#     except (peewee.IntegrityError,peewee.InternalError):
#         print('Category already exists')

# def add_product(name,price,category_name):
#     category_exists = True
#     try:
#         # select name from categories where name = name
#         category = Category.select(category_name).where(
#             Category.name == category_name.lower().strip().get()
#             )
#     except peewee.DoesNotExist as error:
#         category_exists = False
#     if category_exists:
#         print('dsefds')
#         row = Product(
#             name = name.lower().strip(),
#             price = price,
#             category = category
#         )
#         row.save()
# add_category('Dress')
# add_category('Jeans')
# add_category('Tshirt')
# add_category('hoodie')
# add_product('Makers 001', 1000, 'tshirt')
# add_product('DG 002', 15000, 'jeans')
# add_product('Supreme', 70000, 'hoodie')
# add_product('Zara', 2000, 'dress')


# import peewee
# from models import Category, Product


# def add_category(name):
#     try:
#         row = Category(name=name.lower().strip())
#         row.save()
#         print("Saved!")
#     except (peewee.IntegrityError, peewee.InternalError):
#         print("Такие категории уже существуют")


# def add_product(name, price, category_name):
#     category_exist = True
#     try:
#         category = Category.select().where(Category.name==category_name.strip()).get()
#     except peewee.DoesNotExist as e:
#         category_exist = False
#     if category_exist:
#         row = Product(
#             name=name.lower().strip(),
#             price=price,
#             category=category
#         )
#         row.save()

# # add_category("Платья")
# # add_category("Джинсы")
# # add_category("Футболки")
# # add_category("Худи")

# add_product("Makers 001", 1000.00, "джинсы")
# add_product("DG 002", 15000.00, "платья")
# add_product("Supreme", 70000.00, "футболки")
# add_product("Zara Платье", 4000.00, "худи")

