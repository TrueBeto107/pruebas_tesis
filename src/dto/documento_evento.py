"""Data Transfer Objects para documento evento.

Contiene las clases DTO utilizadas para transferir información sobre
documentos entre capas de la aplicación
"""

from dataclasses import dataclass


@dataclass
class CrearDocumentoDto:
    """DTO para solicitud de creación de documento de evento.

    Attributes:
        texto (str): contenido de texto del documento a crear.
        numero (int): número del documento.

    """

    texto: str
    numero: int


@dataclass
class BuscarDocumentoDto:
    """DTO para solicitud de búsqueda de un documento.

    Attributes:
        id_documento_evento (int): identificador único del documento a buscar.

    """

    id_documento_evento: int


@dataclass
class MostrarDocumentoDTO:
    """DTO para respuesta con información del documento a mostrar.

    Attributes:
        id_documento_evento (int): identificador único del documento.
        ruta_archivo (str): ruta del archivo del documento en sistema de archivos.

    """

    id_documento_evento: int
    ruta_archivo: str
