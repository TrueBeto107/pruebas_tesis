from jwt import ExpiredSignatureError
from aplicacion.dto.autenticacion import IniciarSesionDto
from aplicacion.dto.notificacion import NotificacionDto
from flask import render_template
from flask import make_response
from flask import url_for
from flask import current_app as app

from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import set_refresh_cookies
from flask_jwt_extended import get_jwt
from flask_jwt_extended import current_user

from aplicacion.servicio.autenticacion import AutenticadorServicio
from aplicacion.dto.autenticacion import RefrescarTokenDto
from datetime import datetime
from datetime import timezone
from datetime import timedelta

class AutenticacionControlador:
    def __init__(self, servicio: AutenticadorServicio):
        self.servicio = servicio
     
    def iniciar_sesion(self, correo, contrasenia):
        dto = IniciarSesionDto(correo=correo, contrasenia=contrasenia, pimienta=app.config['PIMIENTA'])
        dto_salida = self.servicio.validar_credenciales(dto)
        if dto_salida.token_acceso != None:
            response = make_response()
            response.headers["Hx-Redirect"] = url_for('documento.gestion_documentos')
            set_access_cookies(response, dto_salida.token_acceso)
            set_refresh_cookies(response, dto_salida.token_refrescar)
            return response
        else:
            dto = NotificacionDto('Error', 'Correo o contraseña inválidos')
            return render_template('notificacion.html', notificacion=dto)        
    
