from dataclasses import dataclass


@dataclass
class CrearDocumentoDto:
    texto: str
    numero: int


@dataclass
class BuscarDocumentoDto:
    id_documento_evento: int


@dataclass
class MostrarDocumentoDTO:
    id_documento_evento: int
    ruta_archivo: str
