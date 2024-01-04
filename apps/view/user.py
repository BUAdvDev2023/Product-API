from flask import jsonify, render_template, request

from apps import app

from apps.model.user import *
from apps.model.customer import *

@app.route('/super-admins', methods=['GET'])
def admin_users():
    try:

        if current_user.is_super_admin():
            super_admin_users = User.get_all_users()
            print(super_admin_users)
            return render_template('/home/admins.html', super_admin_users=super_admin_users)
        else:
            return "You don't have permission to access this page."

    except Exception as e:
        print(str(e))
        return "Error", 400
        

@app.route('/customers', methods=['GET'])
def users():
    try:
        all_users = User.get_all_users()
        return render_template('/home/customers.html', users=all_users)
    
    except Exception as e:
        print(str(e))
        return "Error", 400
            
@app.route('/customer-users', methods=['GET'])
def customers_users():
    try:
        all_users = User.get_all_users(current_user.company)
        return render_template('/home/customers-users.html', users=all_users)
    
    except Exception as e:
        print(str(e))
        return "Error", 400
        

@app.route('/validate_user_email', methods = ['POST'])
@auth_required()
def validate_user_email_view():
    return validate_user_email()

@app.route('/add-user', methods = ['POST'])
@auth_required()
def add_user():
    try:
        data = request.json
        # data += Customer.get_all_customers()
        return create_user(data)

    except Exception as e:
        print(str(e))
        return "Error", 400
        
@app.route('/add-admin', methods = ['GET', 'POST'])
@auth_required()
def add_admin():
    try:
        if request.method == 'GET':
            return render_template('/home/admins.html')
        else:  # if the request is POSTs
            if current_user.is_super_admin():
                data = request.json
            return create_user(data)

    except Exception as e:
        print(str(e))
        return "Error", 400
        
@app.route('/sign-up', methods = ['GET'])
@auth_required()
def add():
    try:
        all_customers = Customer.get_all_customers()
        print(all_customers) 
        return render_template('/home/sign-up.html', customers=all_customers)
    
    except Exception as e:
        print(str(e))
        return "Error", 400

# Route to delete a user
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        User.delete_user(user_id)
        return jsonify({'message': 'User deleted successfully'}), 204
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
    #  window.location.href = "/users"; // Redirect to user list or another page