
from flask_security import Security, MongoEngineUserDatastore, \
    UserMixin, RoleMixin, auth_required, hash_password, current_user
import datetime
from bson import ObjectId

from apps import db, app

from apps.model.customer import *

# Define Role and User classes
# Fields with lowercase are library needed

class Role(db.Document, RoleMixin):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)
    permissions = db.StringField(max_length=255)

    def __str__(self):
        return self.name

class User(db.Document, UserMixin):
    Name = db.StringField(max_length=255)
    Lastname = db.StringField(max_length=255)
    email = db.StringField(max_length=255, unique=True)
    company = db.ListField(db.ReferenceField(Customer), default=[])
    password = db.StringField(max_length=255)
    TermsAndConditions = db.BooleanField(default=True)

    last_login_at = db.DateTimeField()
    current_login_at = db.DateTimeField()
    last_login_ip = db.StringField(max_length=255)
    current_login_ip = db.StringField(max_length=255)
    login_count = db.IntField()

    UserProfilePicture = db.FileField()
    createdOnUTC = db.DateTimeField(default=datetime.datetime.utcnow)
    fs_uniquifier = db.StringField(max_length=64, unique=True)
    roles = db.ListField(db.ReferenceField(Role), default=[])
    active = db.BooleanField(default=True)
    created_by = db.ReferenceField('User')

    meta = {'strict': False}
    
    @classmethod
    def delete_user(cls, user_id):
        try:
            # Retrieve the user by ID
            user = cls.objects.get(id=user_id)
            
            # Call the delete_customer_user method from the Customer class
            Customer.objects(users=user).update(pull__users=user)
            
            # Delete the user
            user.delete()
            
            return "User deleted successfully", 200
        
        except cls.DoesNotExist:
            return "User not found", 404
        except Exception as e:
            return str(e), 500

    @classmethod
    def get_user_by_id(cls, user_id):
        # Get a user by ID
        user = cls.objects.get(id=user_id)
        return user

    @classmethod
    def get_user_by_email(cls, email):
        # Get a user by email
        user = cls.objects.get(email=email)
        return user

    def get_all_users(self):
        # Get all users in the same company
        return User.objects(company=self)

    def __str__(self):
        # String representation of the user
        return self.email
    
    def is_super_admin(self):
        return any(role.name == 'Super-Admin' for role in self.roles)
    
    def is_admin(self):
        return any(role.name == 'Admin' for role in self.roles)
    
    def is_user(self):
        return any(role.name == 'User' for role in self.roles)

# Setup Flask-Security
user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Define roles and users for setup if not present
def create_roles_and_users_setup():
    roles_to_create = ["Super-Admin", "Admin", "User"]
    
    for role_name in roles_to_create:
        user_datastore.find_or_create_role(role_name)

    if not user_datastore.find_user(email="admin@admin.com"):
        user_datastore.create_user(
            email="admin@admin.com", password=hash_password("password"), roles=['Super-Admin'])
        
        Customer.create_customer('Adkiero', '13503504', 'Jesus Pombo', '07401504495')
        Address.create_address("1 The Briars", "Waterberry Drive", "Waterlooville", "Hampshire", "PO7 7YH")

        adkiero = Customer.objects(name='Adkiero').first()
        address = Address.objects(postal_code="PO7 7YH").first()
        
        new_user_obj = User.objects(email="admin@admin.com").first()
        new_user_obj.company.append(adkiero)
        new_user_obj.name = "Jesus"
        new_user_obj.Lastname = "Pombo"
        new_user_obj.save()

        adkiero.users.append(new_user_obj)
        adkiero.address = address
        adkiero.save()

    # if not user_datastore.find_user(email="user@user.com"):
    #     user_datastore.create_user(
    #         email="user@user.com", password=hash_password("password"), roles=['User'])

with app.app_context():
    create_roles_and_users_setup()

def create_user(data):
    try:
        data['email'] = data['email'].lower()
        
        if current_user.is_super_admin():
            create_user_for_super_admin(data)
        else:
            create_user_for_non_super_admin(data)

        return "OK", 200

    except Exception as e:
        print(str(e))
        return "Error", 400

def create_user_for_super_admin(data):
    if not user_datastore.find_user(email=data['email']):
        user_datastore.create_user(email=data['email'], password=hash_password(data['password']), roles=['Admin'])
        
        new_user_obj = User.objects(email=data['email']).first()
        customer = Customer.objects(id=data['company']).first()
        customerId = ObjectId(data['company'])
        
        update_user_attributes(new_user_obj, data, customerId)
        update_customer_users_list(customer, new_user_obj)

def create_user_for_non_super_admin(data):
    if not user_datastore.find_user(email=data['email']):
        user_datastore.create_user(email=data['email'], password=hash_password(data['password']), roles=['User'])
        
        new_user_obj = User.objects(email=data['email']).first()
        customer = Customer.objects(id=current_user.company[0].id).first()
        customerId = customer.id
        
        update_user_attributes(new_user_obj, data, customerId)
        update_customer_users_list(customer, new_user_obj)

def update_user_attributes(user_obj, data, customerId):
    user_obj.Name = data['name']
    user_obj.Lastname = data['lastname']
    user_obj.RIF = data['rif']
    user_obj.created_by = current_user
    user_obj.company.append(customerId)
    user_obj.save()

def update_customer_users_list(customer, user_obj):
    if customer:
        customer.users.append(user_obj)
        customer.save()
    
def validate_user_email():
    try:
        email = request.form["email"]
        check = User.objects(email=email).first()
        if check is not None:
            status = False
        else:
            status = True
        return str(status), 200

    except Exception as e:
        return "Error", 400

def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")