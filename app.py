# app.py
from flask import Flask, jsonify
from bayeta import frotar

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola, mundo desde Flask!'

@app.route('/frotar/<int:n_frases>')
def obtener_frases(n_frases):
    frases = frotar(n_frases)
    return jsonify(frases)

if __name__ == '__main__':
    app.run(debug=True)

from bayeta import frotar

print("Probando la función frotar:")
print(frotar(3))  # Genera 3 frases auspiciosas aleatorias
