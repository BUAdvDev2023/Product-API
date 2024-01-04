from flask import request
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_security import Security, MongoEngineUserDatastore, \
    UserMixin, RoleMixin, auth_required, hash_password, current_user

from apps import db, app

class Address(db.Document):
    house_number = db.StringField(max_length=255)
    street = db.StringField(max_length=255)
    city = db.StringField(max_length=255)
    state = db.StringField(max_length=255)
    postal_code = db.StringField(max_length=255)

    @classmethod
    def create_address(cls, house_number, street, city, state, postal_code):
        address = cls(
            house_number=house_number,
            street=street,
            city=city,
            state=state,
            postal_code=postal_code
        )
        address.save()
        return "OK", 200

    def get_full_address(self):
        return f"{self.house_number}, {self.street}, {self.city}, {self.state}, {self.postal_code}"

    def update_address(self, house_number=None, street=None, city=None, state=None, postal_code=None):
        if house_number:
            self.house_number = house_number
        if street:
            self.street = street
        if city:
            self.city = city
        if state:
            self.state = state
        if postal_code:
            self.postal_code = postal_code
        self.save()

    def __str__(self):
        return self.get_full_address()
    
    def delete_address(self):
        self.delete()
    