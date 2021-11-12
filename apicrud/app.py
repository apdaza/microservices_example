from flask import Flask, url_for, redirect, request, jsonify
from models import *
import controller
import json
from serialisers import *


@app.route("/apicrud/<tipo>", methods=['GET'])
def get_method(tipo):
    if tipo == 'productos':
        data = controller.get_all(Producto)
        datos = jsonify([
                ProductoSerialiser.serialise(dato)
                for dato in data])
    if tipo == 'clientes':
        data = controller.get_all(Cliente)
        datos = jsonify([
                ClienteSerialiser.serialise(dato)
                for dato in data])
    if tipo == 'carrito':
        data = controller.get_all(Carrito)
        datos = jsonify([
                CarritoSerialiser.serialise(dato)
                for dato in data])
    if tipo == 'cantidad':
        data = controller.get_all(Cantidad)
        datos = jsonify([
                CantidadSerialiser.serialise(dato)
                for dato in data])

    ## REPLICAR PARA ORDENES
    return datos, 200

@app.route("/apicrud/<tipo>", methods=['POST'])
def post_method(tipo):
    datos = json.loads(request.data)
    if tipo == 'productos':
        tipoModel = Producto
    if tipo == 'clientes':
        tipoModel = Cliente
    if tipo == 'carrito':
        tipoModel = Carrito
    if tipo == 'cantidad':
        tipoModel = Cantidad
    ## REPLICAR PARA CLIENTES, ORDENES
    controller.add_instance(tipoModel, datos)
    return json.dumps("Elemento Agregado "+str(datos)), 200


@app.route("/data/eliminar/<int:id>", methods=['DELETE'])
def eliminar(id):
    controller.delete_instance(Producto, id)
    return json.dumps("Elemento Eliminado "+str(id)), 200

@app.route("/data/actualizar/<tipo>/<int:id>", methods=['PATCH'])
def actualizar(tipo, id):
    datos = json.loads(request.data)
    if tipo == 'productos':
        controller.edit_instance_PRODUCT(Producto, id, datos)
    if tipo == 'clientes':
        controller.edit_instance_CUSTOMER(Cliente, id, datos)
    if tipo == 'carrito':
        controller.edit_instance_CART(Carrito, id, datos)
    if tipo == 'cantidad':
        controller.edit_instance_QUANTITY(Cantidad, id, datos)
    ## REPLICAR PARA CLIENTES, ORDENES
    return json.dumps("Elemento Editado "+str(id)), 200

@app.route("/data/buscar/<int:id>", methods=['GET'])
def buscar(id):
    data = controller.get_by_id(Producto, id)
    p = {
        "id": data.id,
        "nombre": data.producto_nombre,
        "cantidad": data.producto_cantidad,
        "valor": data.producto_valor,
        "descripcion": data.producto_descripcion
    }

    return json.dumps(p), 200

if __name__ == "__main__":
    db.init_app(app)
    db.create_all()
    app.run(host='0.0.0.0', debug=True)