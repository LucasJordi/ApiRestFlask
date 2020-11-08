from app import app
from flask import jsonify,request
from .tables.products import products


#Route for view a list of products
@app.route('/products')
def ProductsView():
    return jsonify({'message':'Products List','products':products})

#Acess a specific product in list

@app.route('/products/<int:product_id>')
def FindProduct(product_id):
    search_id=[product for product in products if product['id']== product_id ]
    if len(search_id) > 0:
        return jsonify(search_id)
    return 'Product not Found!'


@app.route('/products',methods=['POST'])
def AddProduct():
    new_product={
        'id':len(products)+1,
        'name':request.json['name'],
        'brand':request.json['brand'],
        'price':request.json['price'],
        'quantity':request.json['quantity']
    }
    products.append(new_product)
    return 'Received'



@app.route('/products/<int:product_id>',methods=['PUT'])
def EditProduct(product_id):
    search_id=[product for product in products if product['id'] == product_id]
    if(len(search_id)>0):
        search_id[0]['name']=request.json['name']
        search_id[0]['brand']=request.json['brand']
        search_id[0]['price']=request.json['price']
        search_id[0]['quantity']=request.json['quantity']
        return 'Save changes!'
    return 'Not found'    
