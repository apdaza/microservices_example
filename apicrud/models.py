from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

## NO OLVIDAR COLOCAR LOS __INIT__

class Producto(db.Model):
    __tablename__ = 'producto'
    id  = db.Column("product_id", db.Integer, primary_key=True)
    producto_nombre = db.Column(db.String(100), nullable=False)
    producto_valor = db.Column(db.Integer, nullable=False)
    producto_cantidad = db.Column(db.Integer, nullable=False)
    producto_descripcion = db.Column(db.String(100), nullable=False)

    def __init__(self, datos):
        self.producto_nombre = datos["producto_nombre"]
        self.producto_cantidad = datos["producto_cantidad"]
        self.producto_valor = datos["producto_valor"]
        self.producto_descripcion = datos["producto_descripcion"]

class Cliente(db.Model):
    __tablename__ = 'cliente'
    id  = db.Column("customer_id", db.Integer, primary_key=True)
    cliente_nombre = db.Column(db.String(100), nullable=False)
    cliente_direccion = db.Column(db.String(100), nullable=False)
    cliente_telefono = db.Column(db.Integer, nullable=False)

class Orden(db.Model):
    __tablename__ = 'orden'
    id  = db.Column("order_id", db.Integer, primary_key=True)
    fecha_orden = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    estado_orden = db.Column(db.String(50), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.customer_id'), nullable=False)
    cliente = db.relationship('Cliente')

class Cantidad(db.Model):
    __tablename__ = 'cantidad'
    id  = db.Column("quantity_id", db.Integer, primary_key=True)
    cantidad_seleccionada = db.Column(db.Integer, nullable=False)
    orden_id = db.Column(db.Integer, db.ForeignKey('orden.order_id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.product_id'), nullable=False)
    orden = db.relationship('Orden')
    producto = db.relationship('Producto')