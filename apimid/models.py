class pedidosSerializer:
    @staticmethod
    def serialise(pedido, productos) -> dict:
        return {
            "id": pedido[0],
            "status": pedido[1],
            "date": pedido[2],
            "valor_pedido": pedido[3],
            "productos": productos
        }


class productoSerializer:
    @staticmethod
    def serialise(producto) -> dict:
        return {
            "id_producto": producto[0],
            "nombre": producto[1],
            "cantidad": producto[2],
            "valor": producto[3],
            "descripcion": producto[4],
            "valor_total_p": producto[5] 
        }