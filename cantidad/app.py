from flask import Flask, url_for, redirect, request, Response
from flask_sqlalchemy import SQLAlchemy
import json, sys
import requests
from requests.adapters import HTTPAdapter

app = Flask(__name__)
requests.adapters.DEFAULT_RETRIES = 10
BASE_URL = 'http://localhost:8080'
ENDPOINT = 'apicrud/cantidad'

@app.route("/cantidad", methods=['GET'])
def principal():
    response = requests.get(BASE_URL + "/" + ENDPOINT, proxies={"http": "http://apicrud:5000/apicrud"})
    return Response(response.content, response.status_code)


@app.route("/cantidad/agregar", methods=['POST'])
def agregar(): 
    data = json.loads(request.data)
    response = requests.post(BASE_URL + "/" + ENDPOINT, proxies={"http": "http://apicrud:5000/apicrud"}, data=json.dumps(data))
    return Response(response.content, response.status_code)


# @app.route("/cantidad", methods=['GET'])
# def principalcantidad():
#     data = db_crud_cantidad.get_all(cantidad)
#     diccionario_cantidad = []
#     for d in data:
#         p = {
#             "id": d.id,
#             "estado": d.status_cantidad,
#             "fecha": d.date_cantidad,
#             "customer_id_fk": d.customer_id_fk
#         }
#         diccionario_cantidad.append(p)
#     return json.dumps(diccionario_cantidad), 200

# @app.route("/cantidad", methods=['GET'])
# def principalCantidad():
#     data = db_crud_cantidad.get_all(Cantidad)
#     diccionario_cantidad = []
#     for d in data:
#         p = {
#             "cantidad_total": d.quantity,
#             "producto_id": d.producto_id_fk,
#             "id": d.cantidad_id_fk
#         }
#         diccionario_cantidad.append(p)
#     return json.dumps(diccionario_cantidad), 200




# @app.route("/cantidad/agregar", methods=['POST'])
# def agregarcantidad():
#     data = json.loads(request.data)
#     datos = {
#         "status_cantidad": data["estado"],
#         "date_cantidad":date.today() ,
#         "customer_id_fk": data["customer_id_fk"]
#     }
    
#     db_crud_cantidad.add_instance(cantidad, datos)
#     return json.dumps("Elemento Agregado "+str(datos)), 200


# @app.route("/cantidad/agregar", methods=['POST'])
# def agregarCantidad():
#     data = json.loads(request.data)
#     datos = {
#         "cantidad_total": data["cantidad_total"],
#         "product_id": data["product_id"],
#         "cantidad_id": data["id"]
#     }
#     db_crud_cantidad.add_instance(Cantidad, datos)
#     return json.dumps("Elemento Agregado "+str(datos)), 200

# #i need a method tho delete a specific cantidad
# @app.route("/cantidad/eliminar/<int:id>", methods=['DELETE'])
# def eliminarcantidad(id):
#     db_crud_cantidad.delete_instance(cantidad, id)
#     return json.dumps("Elemento Eliminado"), 200

# #i need a method tho delete a specific cantidad
# @app.route("/cantidad/eliminar/<int:id_producto>/<int:id_cantidad>", methods=['DELETE'])
# def eliminarCantidad(id_producto,id_cantidad):
#     db_crud_cantidad.delete_instance(Cantidad, id_producto,id_cantidad)
#     return json.dumps("Elemento Eliminado"), 200


# @app.route("/cantidad/actualizar/<int:id>", methods=['PATCH'])
# def actualizarcantidad(id):
#     data = json.loads(request.data)
#     db_crud_cantidad.edit_instance(cantidad, id, data)
#     return json.dumps("Elemento Editado "+str(id)), 200

# @app.route("/cantidad/actualizar/<int:id_producto>/<int:id_cantidad>", methods=['PATCH'])
# def actualizarCantidad(id_producto,id_cantidad):
#     data = json.loads(request.data)
#     datos = {
#         "cantidad_total": data["cantidad_total"]
#     }
#     db_crud_cantidad.edit_instance(Cantidad, id_producto,id_cantidad, datos)
#     return json.dumps("Elemento Editado "+str(id_producto,id_cantidad)), 200


# #i need a method to search specific cantidad
# @app.route("/cantidad/buscar/<int:id>", methods=['GET'])
# def buscarcantidad(id):
#     data = db_crud_cantidad.get_by_id(cantidad, id)
#     p = {
#         "id": data.id,
#         "estado": data.status_cantidad,
#         "fecha": data.date_cantidad,
#         "customer_id_fk": data.customer_id_fk
#         }
        
#     return json.dumps(p), 200


# #i need a method to search specific cantidad
# @app.route("/cantidad/buscar/<int:id_producto>/<int:id_cantidad>", methods=['GET'])
# def buscarCantidad(id_producto,id_cantidad):
#     data = db_crud_cantidad.get_by_id(Cantidad, id_producto,id_cantidad)
#     p = {
#         "cantidad_total": data.cliente_nombre,
#         "producto_id": data.producto_id_fk,
#         "cantidad_id": data.cantidad_id_fk
#         }
        
#     return json.dumps(p), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)