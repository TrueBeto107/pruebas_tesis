from dataclasses import dataclass


@dataclass
class MostrarInformacionUsuarioDto:
    nombre_completo: str = None
    ruta_foto_perfil: str = None
    roles: list[str] = None
    es_administrador: bool = None
