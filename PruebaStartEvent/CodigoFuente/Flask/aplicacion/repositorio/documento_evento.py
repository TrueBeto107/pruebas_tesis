from aplicacion.modelo.documento_evento import DocumentoEvento
from aplicacion.inicializacion.extenciones import db

class DocumentoEventoRepositorio:
    def select(self, documento_evento: DocumentoEvento) -> DocumentoEvento:
        return db.session.get(DocumentoEvento, documento_evento.id_documento_evento)

    def insert(self, documento: DocumentoEvento):
        db.session.add(documento)
        db.session.commit()

    def select_all(self):
        return db.session.query(DocumentoEvento).all()

    def update():
        pass
    def delete():
        pass