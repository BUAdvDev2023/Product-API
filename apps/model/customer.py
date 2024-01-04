from flask import request
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_security import Security, MongoEngineUserDatastore, \
    UserMixin, RoleMixin, auth_required, hash_password, current_user

# from apps.model.user import User, Role
from apps.model.address import Address

from apps import db, app

class Customer(db.Document):
    name = db.StringField(max_length=255, unique=True)
    identification = db.StringField(max_length=255, unique=True)
    contact_info = db.StringField(max_length=255)
    telephone = db.StringField(max_length=255)
    address = db.ReferenceField('Address')
    transactions = db.ListField(db.ReferenceField('Transaction'))
    users = db.ListField(db.ReferenceField('User'))
    suppliers = db.ListField(db.ReferenceField('Supplier'))
    products = db.ListField(db.ReferenceField('Product'))

    @classmethod
    def create_customer(cls, name, identification, contact_info, telephone):
        customer = cls(
            name=name,
            identification=identification,
            contact_info=contact_info,
            telephone=telephone,
        )
        customer.save()
        return "OK", 200
    
    @classmethod
    def get_all_customers(cls):
        customers = cls.objects()
        return customers
    
    # def delete_customer_user(cls, user_id):
    #     try:
    #         # Retrieve the user by ID and remove it from the users list
    #         user = User.objects.get(id=user_id)
    #         cls.objects(users=user).update(pull__users=user)
    #         return "User removed from customer", 200
    #     except User.DoesNotExist:
    #         return "User not found", 404
    #     except Exception as e:
    #         return str(e), 500

# def test():
#     customer_address = Address.create_address("1", "a", "a", "a", "a")
#     customer = Customer(name="ABC Corp", identification="aaaa", contact_info="0000", address=customer_address)
#     customer.save()

# test()
