from apps.model.user import User, Role
from apps.model.product import Product

from apps import db, app

class Purchase(db.Document):
    supplier = db.ReferenceField('Supplier')
    products = db.ListField(db.ReferenceField('ProductQuantity'))
    total_amount = db.IntField()
    timestamp = db.DateTimeField()
