from apps.model.user import User, Role
from apps.model.product import Product

from apps import db, app

class Review(db.Document):
    user = db.ReferenceField('User')
    product = db.ReferenceField('Product')
    rating = db.IntField(required=True)
    comment = db.StringField()
    timestamp = db.DateTimeField()
