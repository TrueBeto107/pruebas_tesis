from sqlalchemy import select

from src.enums import SubtipoDocumento, TipoDocumento
from src.inicializacion.extenciones import db
from src.interfaces.repositorio import DocumentoEventoRepositorioI
from src.modelo.documento_evento import DocumentoEvento


class DocumentoEventoRepositorio(DocumentoEventoRepositorioI):
    def select_by_edicion_y_subtipo(
        self, id_evento_academico: int, tipo: TipoDocumento, subtipo: SubtipoDocumento
    ) -> list[DocumentoEvento]:

        stmt = select(DocumentoEvento).where(
            DocumentoEvento.id_evento_academico == id_evento_academico
            and DocumentoEvento.tipo_documento == tipo
            and DocumentoEvento.subtipo_documento == subtipo
        )
        return list(db.session.scalars(stmt).all())
