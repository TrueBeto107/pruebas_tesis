from dataclasses import dataclass


@dataclass
class IniciarSesionDto:
    correo: str
    contrasenia: str
    pimienta: str


@dataclass
class ValiadarCredencialesDto:
    token_acceso: str | None
    token_refrescar: str | None
    codigo: int
    mensaje: str


@dataclass
class RefrescarTokenDto:
    identidad: str


@dataclass
class OtorgarNuevoTokenDto:
    token: str
