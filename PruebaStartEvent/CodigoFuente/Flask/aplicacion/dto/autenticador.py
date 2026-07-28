from dataclasses import dataclass

@dataclass
class IniciarSesionDto:
    correo: str = None
    contrasenia: str = None

@dataclass
class ValiadarCredencialesDto:
    token: str = None
    codigo: int = None
    mensaje: str = None