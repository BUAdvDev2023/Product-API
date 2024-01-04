from apps.model.user import User, Role
from apps.model.product import Product

from apps import db, app

class Supplier(db.Document):
    name = db.StringField(required=True)
    contact_name = db.StringField()
    contact_lastname = db.StringField()
    contact_email = db.StringField()
    supplier_telephone = db.StringField()
    products_supplied = db.ListField(db.ReferenceField('Product'))
    Customer = db.ReferenceField('Customer')
    address = db.ReferenceField('Address')