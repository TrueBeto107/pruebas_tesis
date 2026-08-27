from dataclasses import dataclass


@dataclass
class MostrarEventoDto:
    nombre: str
    edicion: int
    ruta_logotipo: str


@dataclass
class BuscarEventosUsuarioDto:
    id_usuario: int
