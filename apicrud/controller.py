from models import db
import json, sys


# GET
def get_all(model):
    data = model.query.all()
    return data


# POST
def add_instance(model, datos):
    instance = model(datos)
    db.session.add(instance)
    commit_changes()


# DELETE
def delete_instance(model, id):
    model.query.filter_by(id=id).delete()
    commit_changes()


# PATCH
# PATCH PRODUCT
def edit_instance_PRODUCT(model, id, datos):
    instance = model.query.filter_by(id=id).all()[0]
    instance.producto_nombre = datos["producto_nombre"]
    instance.producto_descripcion = datos["producto_descripcion"]
    instance.producto_cantidad = datos["producto_cantidad"]
    instance.producto_valor = datos["producto_valor"]
    commit_changes()


# PATCH CUSTOMER
def edit_instance_CUSTOMER(model, id, datos):
    instance = model.query.filter_by(id=id).all()[0]
    instance.cliente_nombre = datos["cliente_nombre"]
    instance.cliente_direccion = datos["cliente_direccion"]
    instance.cliente_telefono = datos["cliente_telefono"]
    commit_changes()


# PATCH CART
def edit_instance_CART(model, id, datos):
    instance = model.query.filter_by(id=id).all()[0]
    instance.status_carrito = datos["estado"]
    instance.date_carrito = datos["fecha"]
    instance.customer_id_fk = datos["customer_id_fk"]
    commit_changes()


# PATCH QUANTITY
def edit_instance_QUANTITY(model, id, datos):
    instance = model.query.filter_by(id=id).all()[0]
    instance.cantidad_seleccionada = datos["cantidad_seleccionada"]
    instance.carrito_id = datos["carrito_id"]
    instance.producto_id = datos["producto_id"]
    commit_changes()


# GET
def get_by_id(model, id):
    instance = model.query.filter_by(id=id).first()
    print("API CRUUUUUUUUUUUUUUUUUUUUUUUUUUD", file=sys.stderr)
    return instance


# COMMIT
def commit_changes():
    db.session.commit()