from flask import Flask, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
# from models import Cliente
# import db_crud
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clientes.db'
app.config['SECRET_KEY'] = "123"
db = SQLAlchemy(app)

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


# @app.route("/clientes/eliminar/<int:id>", methods=['DELETE'])
# def eliminar(id):
#     db_crud.delete_instance(Cliente, id)
#     return json.dumps("Elemento Eliminado "+str(id)), 200

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
    db.create_all()
    app.run(host='0.0.0.0', debug=True)