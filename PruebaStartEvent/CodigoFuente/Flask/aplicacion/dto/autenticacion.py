from dataclasses import dataclass

@dataclass
class IniciarSesionDto:
    correo: str = None
    contrasenia: str = None

@dataclass
class ValiadarCredencialesDto:
    token_acceso: str = None
    token_refrescar: str = None
    codigo: int = None
    mensaje: str = None

@dataclass
class RefrescarTokenDto:
    identidad: str = None
    claims: dict = None

@dataclass
class OtorgarNuevoTokenDto:
    token_acceso: str