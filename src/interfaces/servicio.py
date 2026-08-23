from abc import ABC
from abc import abstractmethod
from src.dto.documento_evento import BuscarDocumentoDto
from src.dto.documento_evento import MostrarDocumentoDTO
from src.dto.documento_evento import CrearDocumentoDto

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