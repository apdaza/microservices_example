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
        url = 'http://addition:5000/addition'
    elif operation == 'subtract':
        url = 'http://subtraction:5000/subtraction'
    elif operation == 'multiply':
        url = 'http://multiplication:5000/multiplication'
    elif operation == 'divide':
        url = 'http://division:5000/division'

    data = {'num1': num1, 'num2': num2}
    response = requests.post(url, json=data)
    result = response.json()['result']

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
