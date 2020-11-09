from app import app
from flask import jsonify,request
import copy
from .tables.orders import *
from .tables.products import *



#Add produtc in a order list

@app.route('/orders/createorder/<int:product_id>')
def CreateOrder(product_id):
    productSearch=[product for product in products if product['id']== product_id ]
    productOrder={"id":len(orderSelect)+1,"product_id":productSearch[0]['id'],"name":productSearch[0]['name'],"price":productSearch[0]['price']}
    orderSelect.append(productOrder)
    
    Price=float(productSearch[0]['price'])
    allPrices.append(Price)
    totalPrice=sum(allPrices)
    orderId=len(orders)+1

    

    
    
    
    

    return jsonify({'Order number':orderId,'Products':orderSelect,"Total price":totalPrice})


#Submit order 

@app.route('/orders/createorder/submit')
def SubmitOrder():
    
    orders.append(orderSelect[:])
    

    
    orderSelect.clear()   

    return 'Submit!'

#View a especific order

@app.route('/orders/<int:item_id>')
def ChangeItem(item_id):
    item_search=[item for item in orderSelect['id']==item_id]
    return jsonify(item_search)


#View all orders

@app.route('/orders/all')
def FindOrder():
    
    return jsonify(orders)
