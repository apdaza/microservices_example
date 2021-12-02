from flask import Flask, url_for, redirect, request, Response
import json, sys
import requests
from requests.adapters import HTTPAdapter
import Helpers
from Helpers import guardarPedido
from Helpers import consultarPedidos


app = Flask(__name__)
requests.adapters.DEFAULT_RETRIES = 10
BASE_URL = 'http://localhost:8080'


@app.route("/apimid/guardarPedido", methods=['POST'])
def post_method():
    datos = json.loads(request.data)
    pedido = guardarPedido.cargarPedido(datos)

    for i in datos["pedido"]:
        print(i, file=sys.stderr)
        print(i["cantidad_seleccionada"], file=sys.stderr)
        print(i["product_id"], file=sys.stderr)
        guardarPedido.calcularCantidad(i["cantidad_seleccionada"], i["product_id"], pedido)     

    return json.dumps("Elemento Agregado "), 200


@app.route("/apimid/consultarPedidos/<int:id>", methods=['GET'])
def get_method(id):

    ENDPOINT = 'apicrud/carrito'
    response = requests.get(BASE_URL + "/" + ENDPOINT, proxies={"http": "http://apicrud:5000/apicrud"})
    data = response.json()
    
    pedidosCliente = consultarPedidos.crearJsonCliente(id, data)
    jsonret = consultarPedidos.crearJsonClienteFinal(pedidosCliente)
    return json.dumps(jsonret), 200
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)