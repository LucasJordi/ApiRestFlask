from flask import Flask




app=Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({'message':'Everything ok!'})


from .controllers import productsRoutes
from .controllers import clientsRoutes
from .controllers import ordersRoutes










