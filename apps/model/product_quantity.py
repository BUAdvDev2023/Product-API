from apps.model.user import User, Role
from apps.model.product import Product

from apps import db, app

class ProductQuantity(db.Document):
    product = db.ReferenceField('Product')
    quantity = db.IntField()
