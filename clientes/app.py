from flask import Flask, url_for, redirect, request, Response
from flask_sqlalchemy import SQLAlchemy
import json, sys
import requests
from requests.adapters import HTTPAdapter

app = Flask(__name__)
requests.adapters.DEFAULT_RETRIES = 10
BASE_URL = 'http://localhost:8080'
ENDPOINT = 'apicrud/clientes'

@app.route("/clientes", methods=['GET'])
def principal():
    response = requests.get(BASE_URL + "/" + ENDPOINT, proxies={"http": "http://apicrud:5000/apicrud"})
    return Response(response.content, response.status_code)


@app.route("/clientes/agregar", methods=['POST'])
def agregar(): 
    data = json.loads(request.data)
    response = requests.post(BASE_URL + "/" + ENDPOINT, proxies={"http": "http://apicrud:5000/apicrud"}, data=json.dumps(data))
    return Response(response.content, response.status_code)

@app.route("/clientes/eliminar/<int:id>", methods=['DELETE'])
def eliminar(id):
    response = requests.delete(BASE_URL + "/" + ENDPOINT + "/" +str(id), proxies={"http": "http://apicrud:5000/apicrud"})
    return Response(response.content, response.status_code)

@app.route("/clientes/actualizar/<int:id>", methods=['PATCH'])
def actualizar(id):
    data = json.loads(request.data)
    response = requests.patch(BASE_URL + "/" + ENDPOINT + "/" +str(id), proxies={"http": "http://apicrud:5000/apicrud"}, data=json.dumps(data))
    return Response(response.content, response.status_code)

# @app.route("/clientes", methods=['GET'])
# def principal():
#     data = db_crud.get_all(Cliente)
#     diccionario_clientes = []
#     for d in data:
#         p = {
#             "id": d.id,
#             "nombre": d.cliente_nombre,
#             "telefono": d.cliente_telefono,
#             "direccion": d.cliente_direccion
#         }
#         diccionario_clientes.append(p)
#     return json.dumps(diccionario_clientes), 200

# @app.route("/clientes/agregar", methods=['POST'])
# def agregar():
#     data = json.loads(request.data)
#     datos = {
#         "nombre": data["nombre"],
#         "direccion": data["direccion"],
#         "telefono": data["telefono"]
#     }
#     db_crud.add_instance(Cliente, datos)
#     return json.dumps("Elemento Agregado "+str(datos)), 200

# @app.route("/clientes/actualizar/<int:id>", methods=['PATCH'])
# def actualizar(id):
#     data = json.loads(request.data)
#     db_crud.edit_instance(Cliente, id, data)
#     return json.dumps("Elemento Editado "+str(id)), 200

# @app.route("/clientes/buscar/<int:id>", methods=['GET'])
# def buscar(id):
#     data = db_crud.get_by_id(Cliente, id)
#     p = {
#         "id": data.id,
#         "nombre": data.cliente_nombre,
#         "telefono": data.cliente_telefono,
#         "direccion": data.cliente_direccion
#     }

#     return json.dumps(p), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)