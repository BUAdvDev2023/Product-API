# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

# import Flask 
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect

from .config import Config

# Inject Flask magic
app = Flask(__name__)

# load Configuration
app.config.from_object( Config ) 

# Database Config DEVELOPMENT
app.config['MONGODB_SETTINGS'] = {"db": "BU",'host':'mongodb+srv://jesuspombo01:tOwKZNIwOhJHK4vt@bu.07ajzrl.mongodb.net/'}
app.config['MONGO_URI'] = "mongodb+srv://jesuspombo01:tOwKZNIwOhJHK4vt@bu.07ajzrl.mongodb.net/"

app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", 'bfam6JJ8UVRUMy2pnYBH-fcR7aotAKi3suI2m4Zjq')
app.config['SECURITY_PASSWORD_SALT'] = os.environ.get("SECURITY_PASSWORD_SALT", 'mUkwdEyaoI3ZQOM6bl1S0Y4a7JiIPGo4XcQSojX8')
app.config['WTF_CSRF_SECRET_KEY'] = "mUkwdEyaoI3ZQOM6bl1S0Y4a7JiIPGo4XcQSojX8"

# app.config['SECURITY_REGISTERABLE'] = True
# app.config['SECURITY_POST_REGISTER_VIEW'] = "index.html"

# Security Session tracker information
app.config['SECURITY_TRACKABLE'] = True

db = MongoEngine(app)
mail = Mail(app)
csrf = CSRFProtect(app)

# Import routing to render the pages
from apps import views
