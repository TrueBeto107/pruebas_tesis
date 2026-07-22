from dataclasses import dataclass

@dataclass
class CrearDocumentoDto:
    texto: str = None
    numero: int = None

@dataclass
class BuscarDocumentoDto:
    id_documento_evento: int = None

@dataclass
class MostrarDocumentoDTO:
    id_documento_evento: int = None
    ruta_archivo: str = None
