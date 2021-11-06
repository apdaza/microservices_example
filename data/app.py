from flask import Flask, url_for, redirect, request
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from models import Producto
import db_crud
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///producto.db'
app.config['SECRET_KEY'] = "123"
db = SQLAlchemy(app)


@app.route("/data", methods=['GET'])
def principal():
    data = db_crud.get_all(Producto)
    diccionario_productos = []
    for d in data:
        p = {
            "id": d.id,
            "nombre": d.producto_nombre,
            "cantidad": d.producto_cantidad,
            "valor": d.producto_valor,
            "descripcion": d.producto_descripcion
        }
        diccionario_productos.append(p)
    return json.dumps(diccionario_productos), 200

@app.route("/data/agregar", methods=['POST'])
def agregar(): 
    data = json.loads(request.data)
    datos = {
        "nombre": data["nombre"],
        "descripcion": data["descripcion"],
        "cantidad": data["cantidad"],
        "valor": data["valor"]
    }
    db_crud.add_instance(Producto, datos)
    return json.dumps("Elemento Agregado "+str(datos)), 200


@app.route("/data/eliminar/<int:id>", methods=['DELETE'])
def eliminar(id):
    db_crud.delete_instance(Producto, id)
    return json.dumps("Elemento Eliminado "+str(id)), 200

@app.route("/data/actualizar/<int:id>", methods=['PATCH'])
def actualizar(id):
    data = json.loads(request.data)
    db_crud.edit_instance(Producto, id, data)
    return json.dumps("Elemento Editado "+str(id)), 200

@app.route("/data/buscar/<int:id>", methods=['GET'])
def buscar(id):
    data = db_crud.get_by_id(Producto, id)
    p = {
        "id": data.id,
        "nombre": data.producto_nombre,
        "cantidad": data.producto_cantidad,
        "valor": data.producto_valor,
        "descripcion": data.producto_descripcion
    }

    return json.dumps(p), 200


if __name__ == "__main__":
    db.create_all()
    app.run(host='0.0.0.0', debug=True)