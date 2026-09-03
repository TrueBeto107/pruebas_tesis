"""Interfaces de servicio para la capa de servicio."""

from abc import ABC, abstractmethod

from src.dto.documento_evento import (
    BuscarDocumentoDto,
    CrearDocumentoDto,
    MostrarDocumentoDTO,
)


class DocumentoEventoServicioI(ABC):
    """Contrato para las operaciones de negocio relacionadas con documentos."""

    @abstractmethod
    def buscar_documento(self, dto: BuscarDocumentoDto) -> MostrarDocumentoDTO:
        """Busca un documento específico según el criterio indicado en el DTO."""

    @abstractmethod
    def buscar_documentos(self) -> list[MostrarDocumentoDTO]:
        """Devuelve la colección completa de documentos disponibles."""

    @abstractmethod
    def crear_documento(self, dto: CrearDocumentoDto) -> MostrarDocumentoDTO:
        """Genera y persiste un nuevo documento a partir de los datos recibidos."""
