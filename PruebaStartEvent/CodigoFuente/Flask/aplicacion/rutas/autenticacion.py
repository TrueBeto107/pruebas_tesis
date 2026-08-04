from flask import current_app as app
from flask import request
from aplicacion.servicio.autenticacion import AutenticadorServicio
from aplicacion.controlador.autenticacion import AutenticacionControlador

controlador = AutenticacionControlador(AutenticadorServicio())

@app.post("/login")
def iniciar_sesion():
    correo = request.form["correo"]
    password = request.form["password"]
    return controlador.iniciar_sesion(correo, password)
    
@app.route('/')
def login():
    return controlador.renderizar_login()

@app.after_request
def refresh(response):
    return controlador.refrescar_tokens_por_expirar(response)