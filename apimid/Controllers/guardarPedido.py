from flask import Flask, url_for, redirect, request, jsonify
from models import *
import Helpers
import json
from Helpers import guardarpedido


BASE_URL = 'http://localhost:8080'

@app.route("/apimid/guardarpedido", methods=['POST'])
def post_method:
    requests.adapters.DEFAULT_RETRIES = 10
    ENDPOINT = 'apicrud/carrito'

    datos = json.loads(request.data)
    for i in datos.pedido:
        guardarpedido.calcularCantidad(i.cantidad_seleccionada, i.product_id)
    
    data = 

    response = requests.post(BASE_URL + "/" + ENDPOINT, proxies={"http": "http://apicrud:5000/apicrud"}, data=json.dumps(data))




    
    
    #return Response(response.content, response.status_code)


    
    return json.dumps("Elemento Agregado "), 200
    

    #controller.add_instance(tipoModel, datos)
    #return json.dumps("Elemento Agregado "+str(datos)), 200


