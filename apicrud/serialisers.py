class ProductoSerialiser:
    @staticmethod
    def serialise(d) -> dict:
        return {
            "id": d.id,
            "nombre": d.producto_nombre,
            "cantidad": d.producto_cantidad,
            "valor": d.producto_valor,
            "descripcion": d.producto_descripcion
        }

class ClienteSerialiser:
    @staticmethod
    def serialise(d) -> dict:
        return {
            "id": d.id,
            "nombre": d.cliente_nombre,
            "direccion": d.cliente_direccion,
            "telefono": d.cliente_telefono,
        }

## CREAR SERIALIZER PARA ORDEN