from dataclasses import dataclass

@dataclass
class IniciarSesionDto:
    correo: str = None
    contrasenia: str = None