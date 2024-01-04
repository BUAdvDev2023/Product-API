from flask import request
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_security import Security, MongoEngineUserDatastore, \
    UserMixin, RoleMixin, auth_required, hash_password, current_user

from apps.model.user import User, Role

from apps import db, app

