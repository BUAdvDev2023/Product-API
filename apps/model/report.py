from apps.model.user import User, Role
from apps.model.product import Product

from apps import db, app

class Report(db.Document):
    report_type = db.StringField(choices=('Sales', 'Inventory', 'Custom'))
    data = db.StringField()
    date_range_start = db.DateTimeField()
    date_range_end = db.DateTimeField()
