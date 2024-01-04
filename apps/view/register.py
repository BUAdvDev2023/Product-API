from webbrowser import get
from flask   import render_template, request, json, jsonify, redirect, url_for
from jinja2  import TemplateNotFound
from flask_security import auth_required, current_user


from apps import app, csrf

from apps.model.register import *
from apps.model.user import *
    
