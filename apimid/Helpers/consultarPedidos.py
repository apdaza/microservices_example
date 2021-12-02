from flask import Flask, url_for, redirect, request, jsonify
import json, sys
import requests
from requests.adapters import HTTPAdapter
import time

BASE_URL = 'http://localhost:8080'


def crearJsonCliente(id_cliente, data_pedidos):
    requests.adapters.DEFAULT_RETRIES = 10
    ENDPOINT = 'apicrud/cantidad'



    pedidos = []
    

    for i in data_pedidos:
        print(i, file=sys.stderr)
        print(i["cliente_id"], file=sys.stderr)

        if(id_cliente == (int)(i["cliente_id"])):
            pedido = []
            pedido.append(i["id"])
            pedido.append(i["status"])
            pedido.append(i["date"])
            pedidos.append(pedido)
            #payload = {'carrito_id': (int)(i["id"])}
            response = requests.get(BASE_URL + "/" + ENDPOINT, proxies={"http": "http://apicrud:5000/apicrud"})#, params=payload)

            data = response.json()

            print("//////////////////////////////////////////////////////////////////////////////////", file=sys.stderr)

            print(data, file=sys.stderr)

            output_dict = [x for x in data if x['carrito_id'] == i["id"]]
            #print(, file=sys.stderr)

            print("Funcional", file=sys.stderr)
            print(output_dict, file=sys.stderr)

            for j in output_dict:
                
                print("-----------------------------------------------------------------------", file=sys.stderr)

                print(j["producto_id"], file=sys.stderr)

                #http://localhost:8080/apicrud/productos/2
                
                ENDPOINT2 = 'apicrud/productos/'+(str)(j["producto_id"])

                response2 = requests.get(BASE_URL + "/" + ENDPOINT2, proxies={"http": "http://apicrud:5000/apicrud"})
                #response = requests.get('http://localhost:8080/productos/2', proxies={"http": "http://productos:5000/productos"})

                print("****************************************************************", file=sys.stderr)
                
                print(response2, file=sys.stderr)

                data2 = response2.json()

                producto = []

                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", file=sys.stderr)

                print(data2, file=sys.stderr)

                #producto.append(data2[""])
                

             #   if()
            
            print("CANTIDAAAAAAAAAAAAAD", file=sys.stderr)

            print(data, file=sys.stderr)

            #for i in data:



    print(pedidos, file=sys.stderr)
    