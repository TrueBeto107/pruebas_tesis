from abc import ABC
from abc import abstractmethod
from typing import TypeVar
from typing import Generic
from typing import Type

from aplicacion.enums.tipo_documento import TipoDocumento
from aplicacion.modelo.documento_evento import DocumentoEvento
from aplicacion.modelo.comite_evento import ComiteEvento
from aplicacion.enums.subtipo_documento import SubtipoDocumento
from aplicacion.modelo.persona_academica import PersonaAcademica
from sqlalchemy import select
from aplicacion.inicializacion.extenciones import db

ModeloT = TypeVar('ModeloT')
IdT = TypeVar('IdT')

class RepositorioBase(ABC, Generic[ModeloT, IdT]):
    
    def __init__(self, clase_modelo: Type[ModeloT]) -> None:
        self._clase_modelo = clase_modelo
    
    def insert(self, modelo: ModeloT) -> None:
        db.session.add(modelo)
        db.session.commit()

    def select_by_id(self, id: IdT) -> ModeloT | None:
        return db.session.get(self._clase_modelo, id)

    def select_all(self) -> list[ModeloT]:
        stmt = select(self._clase_modelo)
        return list(db.session.scalars(stmt).all())
    
    def update(self, modelo: ModeloT) -> ModeloT:
        modelo_bd = db.session.merge(modelo)
        db.session.commit(modelo_bd)
        return modelo_bd

    def delete(self, modelo: ModeloT) -> None:
        modelo_bd = db.session.merge(modelo)
        db.session.delete(modelo_bd)
        db.session.commit()

class ComiteEventoRepositorioI(RepositorioBase[ComiteEvento, int], ABC):
    def __init__(self) -> None:
        super().__init__(ComiteEvento)
        
    @abstractmethod
    def select_by_id_persona(self, id_persona: int) -> list[ComiteEvento]:
        pass

class DocumentoEventoRepositorioI(RepositorioBase[DocumentoEvento, int], ABC):
    def __init__(self) -> None:
        super().__init__(DocumentoEvento)
    
    @abstractmethod
    def select_by_edicion_y_subtipo(
        self, 
        id_evento_academico: int,
        tipo: TipoDocumento,
        subtipo: SubtipoDocumento
        ) -> list[DocumentoEvento]:
        pass

class PersonaAcademicaRepositorioI(RepositorioBase[PersonaAcademica, int], ABC):
    def __init__(self) -> None:
        super().__init__(PersonaAcademica)
    
    @abstractmethod
    def select_by_correo(self, correo: str) -> PersonaAcademica | None:
        pass


