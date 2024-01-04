from flask import jsonify, render_template
from bson import json_util

from apps import app

from apps.model.customer import *
from apps.model.product import *

###################### PRODUCT CATEGORY ###############################

@app.route('/product-category', methods=['GET', 'POST'])
def products_category():
    try:
        if request.method == 'GET':
            return render_template('/home/product-category.html')
        else:
            data = request.json
            create_product_category(data['name'], data['description'])
            return "OK", 200
    except Exception as e:
        print(str(e))
        return jsonify({'success': False, 'error': str(e)})
    
@app.route('/get-all-products-categories', methods=['GET', 'POST'])
def get_all_products_categories():
    try:
        if request.method == 'GET':
            categories = get_all_product_categories()
            return jsonify(categories)
        else:
            data = request.json
            # return Customer.create_customer(**data)
    except Exception as e:
        print(str(e))
        return jsonify({'success': False, 'error': str(e)})
    
@app.route('/delete-category/<category_name>', methods=['DELETE'])
def delete_category(category_name):
    try:
        # Call a function to delete the category
        delete_product_category(category_name)
        return "OK", 200
    except Exception as e:
        print(str(e))
        return jsonify({'success': False, 'error': str(e)})
    
###################### PRODUCTS ###############################


@app.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'GET':
        categories = get_all_product_categories()
        products = get_all_products()
        return render_template('/home/products.html', categories=categories, products=products)
    else:
        data = request.json
        # return Customer.create_customer(**data)

    
@app.route('/add-products', methods=['GET', 'POST'])
def add_products():
        data = request.json
        create_product(data)
        return "OK", 200

@app.route('/get-all-products', methods=['GET', 'POST'])
def get_all_products_view():
    try:
        if request.method == 'GET':
            products = get_all_products()
            return jsonify(products)
        else:
            data = request.json
            # return Customer.create_customer(**data)
    except Exception as e:
        print(str(e))
        return jsonify({'success': False, 'error': str(e)})
    
@app.route('/add-products-new', methods=['GET', 'POST'])
def add_products_new():
    try:
            # data = {
            #     "SKU": "ABC123",
            #     "name": "Running Shoe 1",
            #     "description": "A high-performance running shoe",
            #     "price": 99.99,
            #     "category": "6565015d4104b5035524a13c",
            #     "quantity": 100,
            #     "image_url": "https://example.com/shoe1.jpg",
            #     "LowStockAlertLevel": "10",
            #     "CostPrice": 79.99,
            #     "model": "X123",
            #     "brand": "Athletic Co."
            # }
            data = [
            {
                "SKU": "ABC123",
                "name": "Running Shoe 1",
                "description": "A high-performance running shoe",
                "price": 99.99,
                "category": "6565015d4104b5035524a13c",
                "quantity": 100,
                "image_url": "https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/cdc79cf3-ca49-4318-a15e-a7b137cf9884/dunk-low-twist-shoes-FKMnSq.png",
                "LowStockAlertLevel": "10",
                "CostPrice": 79.99,
                "model": "X123",
                "brand": "Athletic Co."
            },
            {
                "SKU": "DEF456",
                "name": "Training Shoe 2",
                "description": "Versatile training shoe for all activities",
                "price": 89.99,
                "category": "6565015d4104b5035524a13c",
                "quantity": 150,
                "image_url": "https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/cdc79cf3-ca49-4318-a15e-a7b137cf9884/dunk-low-twist-shoes-FKMnSq.png",
                "LowStockAlertLevel": "15",
                "CostPrice": 69.99,
                "model": "Y456",
                "brand": "Fitness Pro"
            },
            # Continue with 48 more shoes...
            # Ensure 'category' and 'image_url' remain the same
            # Adjust SKU, name, description, and other details accordingly
        ]
    
            for i in range(3, 51):
                data.append({
                    "SKU": f"GHI{i}JKL",
                    "name": f"Performance Shoe {i}",
                    "description": f"A versatile athletic shoe for various activities",
                    "price": 79.99 + i,
                    "category": "6565015d4104b5035524a13c",
                    "quantity": 120,
                    "image_url": f"https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/cdc79cf3-ca49-4318-a15e-a7b137cf9884/dunk-low-twist-shoes-FKMnSq.png",
                    "LowStockAlertLevel": "12 + {i}",
                    "CostPrice": 59.99 + i,
                    "model": f"Z{i}789",
                    "brand": "Sportive"
            })


            # create_product(data)
            for shoe_data in data:
                create_product(shoe_data)
            return "OK", 200

    except Exception as e:
        print(str(e))
        return jsonify({'success': False, 'error': str(e)})