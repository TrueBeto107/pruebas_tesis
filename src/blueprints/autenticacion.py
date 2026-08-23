from flask import current_app as app
from flask import request
from src.servicio.autenticacion import AutenticadorServicio
from src.controlador.autenticacion import AutenticacionControlador
from flask import Blueprint

def crear_autenticacion_blueprint(controlador: AutenticacionControlador):
    
    autenticacion_bp = Blueprint(
        'autenticacion',
        __name__,
        url_prefix='/autenticacion',
        template_folder=app.config['DIRECTORIO_TEMPLATES'] / 'autenticacion'
        )

    @autenticacion_bp.post("/login")
    def iniciar_sesion():
        correo = request.form["correo"]
        password = request.form["password"]
        return controlador.iniciar_sesion(correo, password)

    return autenticacion_bp