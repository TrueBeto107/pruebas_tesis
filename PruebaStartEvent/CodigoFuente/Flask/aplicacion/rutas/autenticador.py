from flask import current_app as app
from flask import request
from flask import jsonify
from flask_jwt_extended import create_access_token
from aplicacion.servicio.autenticador import AutenticadorServicio
from aplicacion.controlador.autenticador import AutenticadorControlador

controlador = AutenticadorControlador(AutenticadorServicio())

@app.route("/login", methods=["POST"])
def login():
    correo = request.form["correo"]
    password = request.form["password"]
    return controlador.iniciar_sesion(correo, password)
    

@app.route('/')
def home():
    return controlador.renderizar_login()
