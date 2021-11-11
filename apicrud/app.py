from flask import Flask, url_for, redirect, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import *
import controller
import json, sys
from serialisers import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tienda.db'
app.config['SECRET_KEY'] = "123"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
app.app_context().push()

@app.route("/apicrud/<tipo>", methods=['GET'])
def get_method(tipo):
    if (tipo == 'productos'):
        data = controller.get_all(Producto)
        datos = jsonify([
                ProductoSerialiser.serialise(dato)
                for dato in data])
    ## REPLICAR PARA CLIENTES, ORDENES                
    return datos, 200

@app.route("/apicrud/<tipo>", methods=['POST'])
def post_method(tipo):
    datos = json.loads(request.data) 
    if (tipo == 'productos'):
        tipoModel = Producto
    ## REPLICAR PARA CLIENTES, ORDENES
    controller.add_instance(tipoModel, datos)
    return json.dumps("Elemento Agregado "+str(datos)), 200

if __name__ == "__main__":
    db.init_app(app)
    db.create_all()
    app.run(host='0.0.0.0', debug=True)