from dataclasses import dataclass


@dataclass
class MostrarEventoDto:
    nombre: str = None
    edicion: int = None
    ruta_logotipo: str = None


@dataclass
class BuscarEventosUsuarioDto:
    id_usuario: int = None
