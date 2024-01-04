from apps.model.user import User, Role
from apps.model.product import Product

from apps import db, app

class Return(db.Document):
    product = db.ReferenceField('Product')
    user = db.ReferenceField('User')
    quantity = db.IntField(required=True)
    reason = db.StringField()
    timestamp = db.DateTimeField()
