from flask import jsonify, render_template

from apps import app

from apps.model.customer import *

@app.route('/add-customers', methods=['GET', 'POST'])
def create_customers():
    if request.method == 'GET':
        if current_user.is_super_admin():
            return render_template('/home/add-customers.html')
    else:
        data = request.json
        return Customer.create_customer(**data)
