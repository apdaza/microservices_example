from flask import Flask, url_for, redirect, request, Response
from flask_sqlalchemy import SQLAlchemy
import json, sys
import requests
from requests.adapters import HTTPAdapter

app = Flask(__name__)
requests.adapters.DEFAULT_RETRIES = 10
BASE_URL = 'http://localhost:8080'
ENDPOINT = 'apicrud/productos'

@app.route("/productos", methods=['GET'])
def principal():
    response = requests.get(BASE_URL + "/" + ENDPOINT, proxies={"http": "http://apicrud:5000/apicrud"})
    return Response(response.content, response.status_code)

@app.route("/productos/agregar", methods=['POST'])
def agregar(): 
    data = json.loads(request.data)
    response = requests.post(BASE_URL + "/" + ENDPOINT, proxies={"http": "http://apicrud:5000/apicrud"}, data=json.dumps(data))
    return Response(response.content, response.status_code)

## AJUSTAR
# @app.route("/productos/eliminar/<int:id>", methods=['DELETE'])
# def eliminar(id):
#     db_crud.delete_instance(Producto, id)
#     return json.dumps("Elemento Eliminado "+str(id)), 200

## AJUSTAR
# @app.route("/productos/actualizar/<int:id>", methods=['PATCH'])
# def actualizar(id):
#     data = json.loads(request.data)
#     db_crud.edit_instance(Producto, id, data)
#     return json.dumps("Elemento Editado "+str(id)), 200

## AJUSTAR
# @app.route("/productos/buscar/<int:id>", methods=['GET'])
# def buscar(id):
#     data = db_crud.get_by_id(Producto, id)
#     p = {
#         "id": data.id,
#         "nombre": data.producto_nombre,
#         "cantidad": data.producto_cantidad,
#         "valor": data.producto_valor,
#         "descripcion": data.producto_descripcion
#     }

#     return json.dumps(p), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)