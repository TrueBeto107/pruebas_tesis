from flask import render_template
from flask_jwt_extended import get_jwt
from flask_jwt_extended import current_user
from flask_jwt_extended import set_access_cookies

from aplicacion.dto.autenticacion import RefrescarTokenDto
from aplicacion.servicio.startevent import StarteventServicio

class StarteventControlador():
    
    def __init__(self, servicio: StarteventServicio) -> None:
        self.servicio = servicio
    
    def _esta_por_expirar(self, jwt) -> bool:
        return self.servicio.esta_por_expirar(jwt['exp'])

    def renderizar_login(self):
        return render_template('login.html')

    def refrescar_tokens_por_expirar(self, response):
        try:
            token_acceso = get_jwt()
            if token_acceso and self._esta_por_expirar(token_acceso):
                dto = RefrescarTokenDto(identidad=current_user)
                dto_salida = self.servicio.refrescar_token(dto)
                set_access_cookies(response, dto_salida.token)
            return response
        except RuntimeError:
            return response