from apps.model.user import User, Role
from apps.model.product import Product

from apps import db, app

class Transaction(db.Document):
    product = db.ReferenceField('Product')
    user = db.ReferenceField('Customer')
    transaction_type = db.StringField(choices=('Purchase', 'Sale', 'Return'))
    quantity = db.IntField(required=True)
    timestamp = db.DateTimeField()
