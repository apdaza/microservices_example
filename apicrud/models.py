from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/tienda.db'
app.config['SECRET_KEY'] = "123"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
app.app_context().push()
db = SQLAlchemy(app)


# NO OLVIDAR COLOCAR LOS __INIT__

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

    def __init__(self, datos):
        self.cliente_nombre = datos["cliente_nombre"]
        self.cliente_direccion = datos["cliente_direccion"]
        self.cliente_telefono = datos["cliente_telefono"]

# class Orden(db.Model):
#     __tablename__ = 'orden'
#     id  = db.Column("order_id", db.Integer, primary_key=True)
#     fecha_orden = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     estado_orden = db.Column(db.String(50), nullable=False)
#     cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.customer_id'), nullable=False)
#     cliente = db.relationship('Cliente')

class Cantidad(db.Model):
    __tablename__ = 'cantidad'
    id  = db.Column("quantity_id", db.Integer, primary_key=True)
    cantidad_seleccionada = db.Column(db.Integer, nullable=False)
    carrito_id = db.Column(db.Integer, db.ForeignKey('carrito.carrito_id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.product_id'), nullable=False)
    carrito = db.relationship('Carrito')
    producto = db.relationship('Producto')

    def __init__(self, datos):
        self.cantidad_seleccionada = datos["cantidad_seleccionada"]
        self.carrito_id = datos["carrito_id"]
        self.producto_id = datos["producto_id"]

class Carrito(db.Model):
    __tablename__ = 'carrito'
    id  = db.Column("carrito_id", db.Integer, primary_key=True)
    status_carrito = db.Column(db.String(100))
    date_carrito = db.Column(db.String(100))
    customer_id_fk  = db.Column(db.Integer, db.ForeignKey('cliente.customer_id'), nullable=False)
    cliente = db.relationship('Cliente')

    def __init__(self, datos):
        self.status_carrito = datos["estado"]
        self.date_carrito = datos["fecha"]
        self.customer_id_fk = datos["customer_id_fk"]
