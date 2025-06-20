from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Ejemplo de ruta
@app.route('/')
def home():
    return "Servidor Flask activo"

# Puedes importar otras rutas si las tienes separadas:
# from app import routes
from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)  # Permite conexión desde Angular

    from .routes import main
    app.register_blueprint(main)

    return app
