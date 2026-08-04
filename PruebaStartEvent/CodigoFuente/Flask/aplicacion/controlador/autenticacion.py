from jwt import ExpiredSignatureError
from aplicacion.dto.autenticacion import IniciarSesionDto
from aplicacion.dto.notificacion import NotificacionDto
from flask import render_template
from flask import make_response
from flask import redirect
from flask import url_for
from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import set_refresh_cookies
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import get_jwt

from aplicacion.servicio.autenticacion import AutenticadorServicio
from aplicacion.dto.autenticacion import RefrescarTokenDto
from datetime import datetime
from datetime import timezone
from datetime import timedelta

class AutenticacionControlador:
    def __init__(self, servicio: AutenticadorServicio):
        self.servicio = servicio

    def _esta_por_expirar(self, jwt) -> bool:
        esta_por_expirar = False
        timestamp_expiracion = jwt["exp"]
        utc_time = datetime.now(timezone.utc)
        timestamp_objetivo = datetime.timestamp(utc_time + timedelta(seconds=30))
        if timestamp_objetivo > timestamp_expiracion:
            esta_por_expirar = True
        return esta_por_expirar
     
    def iniciar_sesion(self, correo, contrasenia):
        dto = IniciarSesionDto(correo=correo, contrasenia=contrasenia)
        dto_salida = self.servicio.validar_credenciales(dto)
        if dto_salida.token_acceso != None:
            response = make_response()
            response.headers["Hx-Redirect"] = url_for('gestion_documentos')
            set_access_cookies(response, dto_salida.token_acceso)
            set_refresh_cookies(response, dto_salida.token_refrescar)
            return response
        else:
            dto = NotificacionDto('Error', 'Correo o contraseña inválidos')
            return render_template('notificacion.html', notificacion=dto)        
    
    def renderizar_login(self):
        return render_template('login.html')

    def refrescar_tokens_por_expirar(self, response):
        try:
            #Hay JWT de acceso válido
            token_acceso = get_jwt()
            if token_acceso and self._esta_por_expirar(token_acceso):
                identidad = get_jwt_identity()
                dto = RefrescarTokenDto(identidad=identidad)
                dto_salida = self.servicio.refrescar_token(dto)
                set_access_cookies(response, dto_salida.token)
            return response
        except ExpiredSignatureError:
            #Hay JWT expirado
            #TODO agregar mensaje de expiracion
            return make_response(redirect(url_for('login')))
        except RuntimeError:
            #No hay JWT
            return response