from app import app
from flask import jsonify,request
from .tables.clients import clients
from .tables.products import products



#Route for view a list of clients
@app.route('/clients')
def ClientsView():
    return jsonify({'message':'Clients List','Clients':clients})

#Acess a specific clients in list

@app.route('/clients/<int:client_id>')
def FindClient(client_id):
    search_id=[client for client in clients if client['id']== client_id ]
    if len(search_id) > 0:
        return jsonify(search_id)
    return 'Client not Found!'


@app.route('/clients',methods=['POST'])
def AddClient():
    new_client={
        'id':len(clients)+1,
        'name':request.json['name'],
        'email':request.json['email'],
        'number':request.json['number'],
        'password':request.json['password']
    }
    products.append(new_client)
    return 'Received'



@app.route('/clients/<int:client_id>',methods=['PUT'])
def EditClient(client_id):
    search_id=[client for client in clients if client['id'] == client_id]
    if(len(search_id)>0):
        search_id[0]['name']=request.json['name']
        search_id[0]['email']=request.json['email']
        search_id[0]['number']=request.json['number']
        search_id[0]['password']=request.json['password']
        return 'Save changes!'
    return 'Not found'    
