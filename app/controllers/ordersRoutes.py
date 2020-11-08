from app import app
from flask import jsonify,request
import copy
from .tables.orders import *
from .tables.products import *



#Rotas para o cadastro de ordens de compra
#A primeira etapa é o de adicionar as ordens ao carrinho

@app.route('/orders/createorder/<int:product_id>')
def CreateOrder(product_id):
    productSearch=[product for product in products if product['id']== product_id ]
    productOrder={"id":len(orderSelect)+1,"product_id":productSearch[0]['id'],"name":productSearch[0]['name'],"price":productSearch[0]['price']}
    orderSelect.append(productOrder)
    
    Price=float(productSearch[0]['price'])
    allPrices.append(Price)
    totalPrice=sum(allPrices)
    orderNumber=len(orders)+1
    
    
    
    

    return jsonify({'Order number':orderNumber,'Products':orderSelect,"Total price":totalPrice})




@app.route('/orders/createorder/submit')
def SubmitOrder():
    
    orders.append(copy.copy(orderSelect))
    orderSelect.clear()   

    return 'Submit!'


@app.route('/orders/<int:item_id>')
def ChangeItem(item_id):
    item_search=[item for item in orderSelect['id']==item_id]
    return jsonify(item_search)


@app.route('/orders/all')
def FindOrder():
    
    return jsonify(orders)