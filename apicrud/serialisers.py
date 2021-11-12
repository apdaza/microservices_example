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

class CarritoSerialiser:
    @staticmethod
    def serialise(d) -> dict:
        return {
            "id": d.id,
            "status": d.status_carrito,
            "date": d.date_carrito,
            "cliente_id": d.cliente_id_fk,
        }

class CantidadSerialiser:
    @staticmethod
    def serialise(d) -> dict:
        return {
            "id": d.id,
            "cantidad_seleccionada": d.cantidad_seleccionada,
            "carrito_id": d.carrito_id,
            "producto_id": d.producto_id,
        }



## CREAR SERIALIZER PARA ORDEN