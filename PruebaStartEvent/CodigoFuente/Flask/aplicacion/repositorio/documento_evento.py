from aplicacion.modelo.documento_evento import DocumentoEvento
from aplicacion.inicializacion.extenciones import db
from aplicacion.interfaces.repositorio.documento_evento import DocumentoEventoRepositorioI

class DocumentoEventoRepositorio(DocumentoEventoRepositorioI):
    
    def select_by_edicion_y_subtipo(self, documento_evento: DocumentoEvento) -> list[DocumentoEvento]:
        resultado = db.session.query(DocumentoEvento).filter(
            DocumentoEvento.id_evento_academico == documento_evento.id_evento_academico,
            DocumentoEvento.tipo_documento == documento_evento.tipo_documento,
            DocumentoEvento.subtipo_documento == documento_evento.subtipo_documento
        ).all()
        return resultado
    
    def select(self, documento_evento: DocumentoEvento) -> DocumentoEvento:
        return db.session.get(DocumentoEvento, documento_evento.id_documento_evento)

    def insert(self, documento: DocumentoEvento):
        db.session.add(documento)
        db.session.commit()

    def select_all(self):
        return db.session.query(DocumentoEvento).all()

  