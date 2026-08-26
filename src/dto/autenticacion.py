from dataclasses import dataclass


@dataclass
class IniciarSesionDto:
    correo: str = None
    contrasenia: str = None
    pimienta: str = None


@dataclass
class ValiadarCredencialesDto:
    token_acceso: str = None
    token_refrescar: str = None
    codigo: int = None
    mensaje: str = None


@dataclass
class RefrescarTokenDto:
    identidad: str = None


@dataclass
class OtorgarNuevoTokenDto:
    token: str
