from flask import current_app as app
from aplicacion.dto.autenticador import IniciarSesionDto
from flask_jwt_extended import create_access_token
from aplicacion.dto.autenticador import ValiadarCredencialesDto
from aplicacion.repositorio.persona_academica import PersonaAcademicaRepositorio
from aplicacion.modelo.persona_academica import PersonaAcademica
import hashlib
class AutenticadorServicio():
    
    repositorio_persona = PersonaAcademicaRepositorio()
    
    def validar_credenciales(self, dto: IniciarSesionDto):
        persona = PersonaAcademica(correo=dto.correo, contrasenia=dto.contrasenia)
        
        resultado = self.repositorio_persona.select(persona)
        
        hashed = hashlib.sha256(dto.contrasenia.encode())
        
        if resultado and resultado.contrasenia == hashlib.sha256(dto.contrasenia.encode()).hexdigest():
            jwt = create_access_token(
                identity=str(resultado.id_persona_academica),
                additional_claims={'nombre':resultado.nombre}
                )
            return ValiadarCredencialesDto(jwt, 200, 'Credenciales válidas')
        return ValiadarCredencialesDto(None, 401, 'Correo o contraseña inválidos')
        
