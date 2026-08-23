from datetime import datetime, timezone

from flask import current_app as app
from flask_jwt_extended import create_access_token

from aplicacion.dto.autenticacion import OtorgarNuevoTokenDto, RefrescarTokenDto


class StarteventServicio():
    
    def refrescar_token(self, dto: RefrescarTokenDto) -> OtorgarNuevoTokenDto:
        token = create_access_token(identity=dto.identidad)
        dto_salida = OtorgarNuevoTokenDto(token=token)
        return dto_salida
    
    def esta_por_expirar(self, timestamp_expiracion) -> bool:
        esta_por_expirar = False
        utc_time = datetime.now(timezone.utc)
        timestamp_objetivo = datetime.timestamp(utc_time + app.config['JWT_POR_EXPIRAR'])
        if timestamp_objetivo > timestamp_expiracion:
            esta_por_expirar = True
        return esta_por_expirar