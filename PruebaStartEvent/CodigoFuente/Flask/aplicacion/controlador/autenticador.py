from aplicacion.dto.autenticador import IniciarSesionDto
from flask import render_template
from flask import make_response
from flask import redirect
from flask import url_for
from flask_jwt_extended import set_access_cookies

from aplicacion.servicio.autenticador import AutenticadorServicio

class AutenticadorControlador:
    def __init__(self, servicio: AutenticadorServicio):
        self.servicio = servicio

    def iniciar_sesion(self, correo, contrasenia):
        dto = IniciarSesionDto(correo=correo, contrasenia=contrasenia)
        dto = self.servicio.validar_credenciales(dto)
        if dto.token != None:
            response = make_response(redirect(url_for('gestion_documentos')))
            set_access_cookies(response, dto.token)
            return response
        else:
            #Error
            return 'Error'
    
    def renderizar_login(self):
        return render_template('login.html')
