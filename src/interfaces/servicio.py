from abc import ABC, abstractmethod

from src.dto.documento_evento import (
    BuscarDocumentoDto,
    CrearDocumentoDto,
    MostrarDocumentoDTO,
)


class DocumentoEventoServicioI(ABC):
    @abstractmethod
    def buscar_documento(self, dto: BuscarDocumentoDto) -> MostrarDocumentoDTO:
        pass

    @abstractmethod
    def buscar_documentos(self) -> list[MostrarDocumentoDTO]:
        pass

    @abstractmethod
    def crear_documento(self, dto: CrearDocumentoDto) -> MostrarDocumentoDTO:
        pass
