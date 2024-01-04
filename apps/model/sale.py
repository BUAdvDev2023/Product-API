from apps.model.user import User, Role
from apps.model.product import Product

from apps import db, app

class Sale(db.Document):
    customer = db.ReferenceField('Customer')
    products = db.ListField(db.ReferenceField('ProductQuantity'))
    total_amount = db.IntField()
    timestamp = db.DateTimeField()
