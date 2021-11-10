import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class Cliente(db.Model):
    __tablename__ = 'cliente'
    id  = db.Column("customer_id", db.Integer, primary_key=True)
    cliente_nombre = db.Column(db.String(100))
    cliente_direccion = db.Column(db.String(100))
    cliente_telefono = db.Column(db.Integer)

    def __init__(self, datos):
        self.cliente_nombre = datos["nombre"]
        self.cliente_direccion = datos["direccion"]
        self.cliente_telefono = datos["telefono"]