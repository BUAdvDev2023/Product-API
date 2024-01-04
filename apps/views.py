# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Flask modules
from flask   import render_template, request
from jinja2  import TemplateNotFound
from flask_security import auth_required, current_user

# App modules
from apps import app

from apps.view import user
from apps.view import register
from apps.view import address
from apps.view import customer
from apps.view import notification
from apps.view import product_category
from apps.view import product_quantity
from apps.view import product
from apps.view import purchase
from apps.view import report
from apps.view import returns
from apps.view import review
from apps.view import sale
from apps.view import supplier
from apps.view import transaction

# App main route + generic routing
@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path>')
@auth_required()
def index(path):

    try:

        # Detect the current page
        segment = get_segment( request )

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template( 'home/' + path, segment=segment )
    
    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

def get_segment( request ): 

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment    

    except:
        return None  
