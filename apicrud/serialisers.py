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

## CREAR SERIALIZER PARA CADA CLASE