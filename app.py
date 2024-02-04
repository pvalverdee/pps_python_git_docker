# app.py
from flask import Flask, jsonify
from bayeta import frotar

app = Flask(__name__)

@app.route('/')
def index():
    # Llama a la función frotar sin limitar la cantidad de frases
    resultadofrotar = frotar()

    # Devuelve una frase auspiciosa aleatoria en la respuesta de la ruta raíz
    return resultadofrotar[0]

@app.route('/frotar/<int:nfrases>', methods=['GET'])
def obtenerfrases(nfrases):
    frases = frotar(nfrases)
    return jsonify({"frases": frases})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
