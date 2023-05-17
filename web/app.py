# web/app.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/web')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']

    if operation == 'sum':
        url = 'http://suma:5000/suma'
    elif operation == 'subtract':
        url = 'http://resta:5000/resta'
    elif operation == 'multiply':
        url = 'http://multiplicacion:5000/multiplicacion'
    elif operation == 'divide':
        url = 'http://division:5000/division'

    data = {'num1': num1, 'num2': num2}
    response = requests.post(url, json=data)
    result = response.json()['result']

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
