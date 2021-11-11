from models import db

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
def edit_instance(model, id, datos):
    # Mejorar funcionalidad OJOOOOOO
    instance = model.query.filter_by(id=id).all()[0]
    instance.producto_nombre = datos["nombre"]
    instance.producto_descripcion = datos["descripcion"]
    instance.producto_cantidad = datos["cantidad"]
    instance.producto_valor = datos["valor"]
    commit_changes()

# GET
def get_by_id(model, id):
    instance = model.query.filter_by(id=id).first()
    return instance

# COMMIT
def commit_changes():
    db.session.commit()