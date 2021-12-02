from flask import Flask, url_for, redirect, request, jsonify
import json, sys
import requests
from requests.adapters import HTTPAdapter
import time

BASE_URL = 'http://localhost:8080'

def calcularCantidad(cantidad, product_id, pedido):
    requests.adapters.DEFAULT_RETRIES = 10  
    ENDPOINT = 'apicrud/productos'

    cantidad = (int)(cantidad)
    product_id = (int)(product_id)
    pedido = (int)(pedido)
    payload = {'product_id': product_id}
    response = requests.get(BASE_URL + "/" + ENDPOINT, proxies={"http": "http://apicrud:5000/apicrud"}, params=payload)

    data = response.json()
    
    cantidad_producto = (int)(data[product_id-1]["producto_cantidad"])
    cantidad_producto = cantidad_producto - cantidad
    data[product_id-1]["producto_cantidad"] =  cantidad_producto
    
    data2 = data[product_id-1]
    response = requests.patch(BASE_URL + "/" + ENDPOINT + "/" +str(product_id), proxies={"http": "http://apicrud:5000/apicrud"}, data=json.dumps(data2))


    ENDPOINT = 'apicrud/cantidad'

    datos = {
        "cantidad_seleccionada": cantidad,
        "carrito_id": pedido,
        "producto_id": product_id
    }
    response = requests.post(BASE_URL + "/" + ENDPOINT, proxies={"http": "http://apicrud:5000/apicrud"}, data=json.dumps(datos))




def cargarPedido(data):
    requests.adapters.DEFAULT_RETRIES = 10
    ENDPOINT = 'apicrud/carrito'

    datos = {
        "estado": "Activo",
        "fecha": (str)(time.strftime("%d/%m/%y")),
        "customer_id_fk": data["customer_id_fk"] 
    }
    response = requests.post(BASE_URL + "/" + ENDPOINT, proxies={"http": "http://apicrud:5000/apicrud"}, data=json.dumps(datos))
    
    response2 = requests.get(BASE_URL + "/" + ENDPOINT, proxies={"http": "http://apicrud:5000/apicrud"})

    data2 = response2.json()

    tamano = len(data2)

    return tamano



    
    

