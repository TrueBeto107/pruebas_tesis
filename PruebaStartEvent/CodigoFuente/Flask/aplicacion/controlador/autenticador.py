from aplicacion.dto.autenticador import IniciarSesionDto
from flask import render_template

class AutenticadorControlador:
    def __init__(self, servicio):
        self.servicio = servicio

    def validar_credenciales(self, correo, contrasenia):
        dto = IniciarSesionDto(correo=correo, contrasenia=contrasenia)
        resultado = self.servicio.validar_credenciales(dto)
        #cookie
        #return render_template('buscar_documento.pdf')

    def renderizar_login(self):
        return render_template('login.html')