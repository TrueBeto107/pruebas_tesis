from dataclasses import dataclass


@dataclass
class MostrarInformacionUsuarioDto:
    nombre_completo: str
    ruta_foto_perfil: str
    roles: list[str]
    es_administrador: bool
