from flask import Flask, url_for, redirect, request, jsonify
import json, sys
import requests
from requests.adapters import HTTPAdapter
import time
from models import *


BASE_URL = 'http://localhost:8080'


def crearJsonCliente(id_cliente, data_pedidos):
    requests.adapters.DEFAULT_RETRIES = 10
    ENDPOINT = 'apicrud/cantidad'
    
    pedidos = []

    for i in data_pedidos:
        if(id_cliente == (int)(i["cliente_id"])):
            pedido = []
            pedido.append(i["id"])
            pedido.append(i["status"])
            pedido.append(i["date"])
            response = requests.get(BASE_URL + "/" + ENDPOINT, proxies={"http": "http://apicrud:5000/apicrud"})#, params=payload)

            data = response.json()

            output_dict = [x for x in data if x['carrito_id'] == i["id"]]
            productos = []
            valor_pedido = 0

            for j in output_dict:
             
                ENDPOINT2 = 'apicrud/productos/'+(str)(j["producto_id"])

                response2 = requests.get(BASE_URL + "/" + ENDPOINT2, proxies={"http": "http://apicrud:5000/apicrud"})

                data2 = response2.json()

                producto = []

                producto.append(data2["id"])
                producto.append(data2["nombre"])
                producto.append(j["cantidad_seleccionada"])
                producto.append(data2["valor"])
                producto.append(data2["descripcion"])
                cantidad_cliente = (int)(j["cantidad_seleccionada"])
                valor_prod = (int)(data2["valor"])
                valor_tot_prod = cantidad_cliente*valor_prod
                valor_pedido = valor_pedido + valor_tot_prod
                producto.append(valor_tot_prod)
                productos.append(producto)

            pedido.append(valor_pedido)
            pedido.append(productos)      
            pedidos.append(pedido)

    return pedidos

def crearJsonClienteFinal(pedidosCliente):
    pedidos = []
    for pedido in pedidosCliente:
        productos = []
        for producto in pedido[4]:
            productos.append(productoSerializer.serialise(producto))
        pedidos.append(pedidosSerializer.serialise(pedido, productos))

    return pedidos

