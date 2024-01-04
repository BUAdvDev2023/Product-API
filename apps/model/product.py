import base64
from apps.model.user import User, Role

from apps import db, app


class ProductCategory(db.Document):
    name = db.StringField(required=True, unique=True)
    description = db.StringField()


class Product(db.Document):
    SKU = db.StringField(default="")
    name = db.StringField()
    description = db.StringField()
    price = db.FloatField(required=True)
    category = db.ReferenceField("ProductCategory")
    # # supplier = db.ReferenceField("Supplier")
    quantity = db.ReferenceField("ProductQuantity")
    image_url = db.StringField()
    # # reviews = db.ListField(db.ReferenceField("Review"))
    # CountryOfManufacture = db.StringField()
    model = db.StringField()
    brand = db.StringField()
    # size = db.StringField()
    # EAN = db.StringField()
    LowStockAlertLevel = db.StringField()
    # Weight = db.StringField()
    # Height = db.StringField()
    # Width = db.StringField()
    # Depth = db.StringField()
    # Volume = db.StringField()
    CostPrice = db.FloatField()

class ProductQuantity(db.Document):
    product = db.ReferenceField("Product")
    quantity = db.IntField()
    customer = db.ReferenceField("Customer")


class StockItem(db.Document):
    product = db.ReferenceField(Product, required=True)
    quantity = db.IntField(required=True, default=0)


class StockTransaction(db.Document):
    stock_item = db.ReferenceField(StockItem, required=True)
    transaction_type = db.StringField(max_length=50, choices=["purchase", "sale"])
    quantity_change = db.IntField(required=True)
    transaction_date = db.DateTimeField()
    # Other transaction-related fields

    def update_stock_quantity(self):
        if self.transaction_type == "purchase":
            self.stock_item.quantity += self.quantity_change
        elif self.transaction_type == "sale":
            self.stock_item.quantity -= self.quantity_change
        self.stock_item.save()


#################### PRODUCT CATEGORY ###################################

def create_product_category(name, description):
    category = ProductCategory(name=name, description=description)
    category.save()

def get_all_product_categories():
    return ProductCategory.objects()

def update_product_category(name, new_description):
    category = get_product_category_by_name(name)
    if category:
        category.description = new_description
        category.save()

def delete_product_category(name):
    category = get_product_category_by_name(name)
    if category:
        category.delete()

def get_product_category_by_name(name):
    return ProductCategory.objects(name=name).first()

############################# PRODUCT ##################################

def create_product(data):

    SKU=data.get('SKU')
    name=data.get('name')
    description=data.get('description')
    price=data.get('price')
    category=data.get('category')
    quantity=data.get('quantity')
    image_url=data.get('image_url')
    LowStockAlertLevel=data.get('LowStockAlertLevel')
    CostPrice=data.get('CostPrice')
    model=data.get('model')
    brand=data.get('brand')


    # Create a new product instance
    product = Product(
        SKU=SKU,
        name=name,
        description= description,
        price=price,
        category=category,
        quantity=quantity,
        image_url=image_url,
        LowStockAlertLevel=LowStockAlertLevel,
        CostPrice=CostPrice,
        model=model,
        brand=brand,
    )

    # Save the new product to the database
    product.save()

    return product


def get_all_products():
    return Product.objects()


def get_product_by_name(name):
    return Product.objects(name=name).first()


def update_product(name, new_description, new_price):
    product = get_product_by_name(name)
    if product:
        product.description = new_description
        product.price = new_price
        product.save()


def delete_product(name):
    product = get_product_by_name(name)
    if product:
        product.delete()

