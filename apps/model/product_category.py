from apps.model.user import User, Role
from apps.model.product import Product

from apps import db, app

class ProductCategory(db.Document):
    name = db.StringField(required=True, unique=True)
    description = db.StringField()
