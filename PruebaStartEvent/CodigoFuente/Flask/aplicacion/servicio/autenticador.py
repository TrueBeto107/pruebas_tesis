from flask import current_app as app
from flask import render_template
from aplicacion.dto.autenticador import IniciarSesionDto
from flask import jsonify
from flask_jwt_extended import create_access_token

class AutenticadorServicio():
    def validar_credenciales(dto: IniciarSesionDto):
        if dto.correo != "test" or dto.contrasenia != "test":
            return jsonify({"msg": "Correo o contraseña inválidos"}), 401
        access_token = create_access_token(identity=dto.correo)
        return jsonify(access_token=access_token)
