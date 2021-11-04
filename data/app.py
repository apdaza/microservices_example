from flask import Flask, url_for, redirect
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///productos.db'
app.config['SECRET_KEY'] = "123"

db = SQLAlchemy(app)


class producto(db.Model):

    id  = db.Column("product_id", db.Integer, primary_key=True)
    producto_nombre = db.Column(db.String(100))
    producto_valor = db.Column(db.Integer)
    producto_cantidad = db.Column(db.Integer)

    def __init__(self, datos):
        self.producto_nombre = datos["nombre"]
        self.producto_cantidad = datos["cantidad"]
        self.producto_valor = datos["valor"]


@app.route("/data")
def principal():
    data = producto.query.all()
    diccionario_productos = {}
    for d in data:
        p = {"id": d.id,
             "nombre": d.producto_nombre,
             "cantidad": d.producto_cantidad,
             "valor": d.producto_valor
            }
        diccionario_productos[d.id] = p
    return str(diccionario_productos)


@app.route("/data/agregar/<nombre>/<int:cantidad>/<int:valor>")
def agregar(nombre, cantidad, valor):
    datos = {"nombre": nombre,
             "cantidad": cantidad,
             "valor": valor
            }
    p = producto(datos)
    db.session.add(p)
    db.session.commit()
    return str(datos)


@app.route("/data/eliminar/<int:id>")
def eliminar(id):
    p = producto.query.filter_by(id=id).first()
    db.session.delete(p)
    db.session.commit()
    return redirect(url_for('principal'))


@app.route("/data/actualizar/<int:id>/<nombre>/<int:cantidad>/<int:valor>")
def actualizar(id, nombre, cantidad, valor):
    p = producto.query.filter_by(id=id).first()
    p.producto_nombre = nombre
    p.producto_cantidad = cantidad
    p.producto_valor = valor
    db.session.commit()
    return redirect("http://localhost:8080/data")


@app.route("/data/buscar/<int:id>")
def buscar(id):
    d = producto.query.filter_by(id=id).first()
    p = {"id": d.id,
         "nombre": d.producto_nombre,
         "cantidad": d.producto_cantidad,
         "valor": d.producto_valor
         }

    return str(p)


if __name__ == "__main__":
    db.create_all()
    app.run(host='0.0.0.0', debug=True)