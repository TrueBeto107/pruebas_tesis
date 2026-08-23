from aplicacion.enums import SubtipoDocumento
from aplicacion.enums import TipoDocumento
from aplicacion.modelo.documento_evento import DocumentoEvento
from aplicacion.inicializacion.extenciones import db
from aplicacion.interfaces.repositorio import DocumentoEventoRepositorioI
from sqlalchemy import select

class DocumentoEventoRepositorio(DocumentoEventoRepositorioI):
    
    def select_by_edicion_y_subtipo(
        self, 
        id_evento_academico: int,
        tipo: TipoDocumento,
        subtipo: SubtipoDocumento
        ) -> list[DocumentoEvento]:
        
        stmt = select(DocumentoEvento).where(
            DocumentoEvento.id_evento_academico == id_evento_academico and
            DocumentoEvento.tipo_documento == tipo and
            DocumentoEvento.subtipo_documento == subtipo
            )
        return list(db.session.scalars(stmt).all())
  