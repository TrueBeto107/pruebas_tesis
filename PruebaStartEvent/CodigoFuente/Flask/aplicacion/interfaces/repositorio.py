from abc import ABC
from abc import abstractmethod
from typing import TypeVar
from typing import Generic
from aplicacion.modelo.documento_evento import DocumentoEvento

T = TypeVar('T')

class RepositorioInsertarI(ABC, Generic[T]):
    
    @abstractmethod
    def insert(self, modelo: T) -> None:
        pass

class RepositorioSeleccionarI(ABC, Generic[T]):
    
    @abstractmethod
    def select(self, modelo: T) -> T:
        pass

class RepositorioSeleccionarTodosI(ABC, Generic[T]):
    
    @abstractmethod
    def select_all(self) -> list[T]:
        pass

class DocumentoEventoRepositorioI(
    RepositorioInsertarI[DocumentoEvento],
    RepositorioSeleccionarI[DocumentoEvento],
    RepositorioSeleccionarTodosI[DocumentoEvento]
    ):
    
    @abstractmethod
    def select_by_edicion_y_subtipo(self, documento_evento: DocumentoEvento) -> list[DocumentoEvento]:
        pass






