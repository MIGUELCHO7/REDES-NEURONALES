from flask import Blueprint, request, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return 'Servidor Flask activo'

@main.route('/predict', methods=['POST'])
def predict():
    data = request.json
    edad = data.get('edad', 0)
    peso = data.get('peso', 0)
    estatura = data.get('estatura', 1.0)  # en metros, evitar división por cero

    # Cálculo del IMC
    imc = peso / (estatura ** 2)

    resultado = ""

    # Clasificación basada en IMC según OMS
    if imc < 18.5:
        resultado = "Bajo peso"
    elif 18.5 <= imc < 24.9:
        resultado = "Peso normal"
    elif 25.0 <= imc < 29.9:
        resultado = "Sobrepeso"
    elif 30.0 <= imc < 34.9:
        resultado = "Obesidad tipo I"
    elif 35.0 <= imc < 39.9:
        resultado = "Obesidad tipo II"
    else:
        resultado = "Obesidad tipo III (mórbida)"

    return jsonify({'resultado': resultado, 'IMC': round(imc, 2)})

