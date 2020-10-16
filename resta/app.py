from flask import Flask

app = Flask(__name__)

@app.route("/resta/<int:valor1>/<int:valor2>")
def resta(valor1, valor2):
    return str(valor1 - valor2)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)