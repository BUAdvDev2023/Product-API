from apps.model.user import User, Role
from apps.model.product import Product

from apps import db, app

class Notification(db.Document):
    message = db.StringField()
    recipient = db.ReferenceField('User')
    is_read = db.BooleanField(default=False)
    timestamp = db.DateTimeField()
