from aplicacion.dto.autenticacion import IniciarSesionDto
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from aplicacion.dto.autenticacion import ValiadarCredencialesDto
from aplicacion.repositorio.persona_academica import PersonaAcademicaRepositorio
from aplicacion.modelo.persona_academica import PersonaAcademica
from aplicacion.dto.autenticacion import OtorgarNuevoTokenDto
from aplicacion.dto.autenticacion import RefrescarTokenDto
import hashlib

class AutenticadorServicio():
    
    repositorio_persona = PersonaAcademicaRepositorio()

    def validar_credenciales(self, dto: IniciarSesionDto):
        persona = PersonaAcademica(correo=dto.correo, contrasenia=dto.contrasenia)
        persona = self.repositorio_persona.select(persona)
        
        if persona and persona.contrasenia == hashlib.sha256(dto.contrasenia.encode()).hexdigest():
            jwt = create_access_token(
                identity=str(persona.id_persona_academica)
                )
            token_refrescar = create_refresh_token(identity=str(persona.id_persona_academica))
            return ValiadarCredencialesDto(token_acceso=jwt, token_refrescar=token_refrescar, codigo=200, mensaje='Credenciales válidas')
        return ValiadarCredencialesDto(token_acceso=None, token_refrescar=None, codigo=401, mensaje='Correo o contraseña inválidos')
    
    def refrescar_token(self, dto: RefrescarTokenDto) -> OtorgarNuevoTokenDto:
        token = create_access_token(identity=dto.identidad)
        dto_salida = OtorgarNuevoTokenDto(token_acceso=token)
        print('###########Token refrescado')
        return dto_salida
                
