from abc import ABC
from abc import abstractmethod
from aplicacion.interfaces.repositorio.repositorio_base import RepositorioInsertarI
from aplicacion.interfaces.repositorio.repositorio_base import RepositorioSelectI
from aplicacion.interfaces.repositorio.repositorio_base import RepositorioSelectAllI
from aplicacion.modelo.documento_evento import DocumentoEvento

class DocumentoEventoRepositorioI(RepositorioInsertarI[DocumentoEvento], RepositorioSelectI[DocumentoEvento], RepositorioSelectAllI[DocumentoEvento]):
    
    @abstractmethod
    def select_by_edicion_y_subtipo(self, documento_evento: DocumentoEvento) -> list[DocumentoEvento]:
        pass
