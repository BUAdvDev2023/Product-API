from webbrowser import get
from flask   import render_template, request, json, jsonify, redirect, url_for
from jinja2  import TemplateNotFound
from flask_security import auth_required

from apps import app

from apps.model.address import *

@app.route('/add-address', methods = ['GET','POST'])
@auth_required()
def add_address():
    data = {
        "house_number": "333",
        "street": "Main St",
        "city": "Cityville",
        "state": "State",
        "postal_code": "12345"
    }

    return Address.create_address(**data)