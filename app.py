from flask import Flask, render_template, request, jsonify
from codigo_morse import LIBRO

app = Flask(__name__)


def obtener_morse(palabra):
    ESPACIO_MENOR = '   '
    ESPACIO_MAYOR = '          '
    letras_codificadas = []
    letra_anterior = None
    for char in palabra:
        if char == ' ':
            letras_codificadas.append(ESPACIO_MAYOR)
            letra_anterior = ESPACIO_MAYOR
            continue

        if char in LIBRO:
            codigo_morse = LIBRO[char]
            if char == letra_anterior:
                letras_codificadas.append(' ')
            elif letra_anterior and letra_anterior != ESPACIO_MAYOR:
                letras_codificadas.append(ESPACIO_MENOR)
            letras_codificadas.append(codigo_morse)
            letra_anterior = char
    return ''.join(letras_codificadas)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    text = data['text']
    morse_code = obtener_morse(text)
    return jsonify({'morse_code': morse_code})


if __name__ == '__main__':
    app.run(debug=True)
