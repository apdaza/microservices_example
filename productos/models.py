import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class Producto(db.Model):
    __tablename__ = 'producto'
    id  = db.Column("product_id", db.Integer, primary_key=True)
    producto_nombre = db.Column(db.String(100))
    producto_valor = db.Column(db.Integer)
    producto_cantidad = db.Column(db.Integer)
    producto_descripcion = db.Column(db.String(100))

    def __init__(self, datos):
        self.producto_nombre = datos["nombre"]
        self.producto_cantidad = datos["cantidad"]
        self.producto_valor = datos["valor"]
        self.producto_descripcion = datos["valor"]