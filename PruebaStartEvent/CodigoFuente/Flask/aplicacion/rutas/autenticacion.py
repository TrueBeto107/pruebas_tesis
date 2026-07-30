from flask import current_app as app
from flask import request
from flask_jwt_extended import get_jwt
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended import get_jwt_identity
from aplicacion.servicio.autenticacion import AutenticadorServicio
from aplicacion.controlador.autenticacion import AutenticacionControlador

controlador = AutenticacionControlador(AutenticadorServicio())

@app.route("/login", methods=["POST"])
def login():
    correo = request.form["correo"]
    password = request.form["password"]
    return controlador.iniciar_sesion(correo, password)
    
@app.route('/')
def home():
    return controlador.renderizar_login()

@app.after_request
def refresh(response):
    return controlador.refrescar_tokens_por_expirar(response)
    