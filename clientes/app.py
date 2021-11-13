from flask import Flask, url_for, redirect, request, Response
import json
import requests
from requests.adapters import HTTPAdapter

app = Flask(__name__)
requests.adapters.DEFAULT_RETRIES = 10
BASE_URL = 'http://localhost:8080'
ENDPOINT = 'apicrud/clientes'

@app.route("/clientes", methods=['GET'])
def principal():
    response = requests.get(BASE_URL + "/" + ENDPOINT, proxies={"http": "http://apicrud:5000/apicrud"})
    return Response(response.content, response.status_code)


@app.route("/clientes/agregar", methods=['POST'])
def agregar(): 
    data = json.loads(request.data)
    response = requests.post(BASE_URL + "/" + ENDPOINT, proxies={"http": "http://apicrud:5000/apicrud"}, data=json.dumps(data))
    return Response(response.content, response.status_code)

@app.route("/clientes/eliminar/<int:id>", methods=['DELETE'])
def eliminar(id):
    response = requests.delete(BASE_URL + "/" + ENDPOINT + "/" +str(id), proxies={"http": "http://apicrud:5000/apicrud"})
    return Response(response.content, response.status_code)

@app.route("/clientes/actualizar/<int:id>", methods=['PATCH'])
def actualizar(id):
    data = json.loads(request.data)
    response = requests.patch(BASE_URL + "/" + ENDPOINT + "/" +str(id), proxies={"http": "http://apicrud:5000/apicrud"}, data=json.dumps(data))
    return Response(response.content, response.status_code)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)