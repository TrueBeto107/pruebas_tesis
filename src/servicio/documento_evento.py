"""Servicio para la gestión de documentos asociados a eventos."""

from flask import current_app as app
from flask import render_template
from weasyprint import CSS, HTML

from src.dto.documento_evento import (
    BuscarDocumentoDto,
    CrearDocumentoDto,
    MostrarDocumentoDTO,
)
from src.enums import SubtipoDocumento, TipoDocumento
from src.interfaces.repositorio import DocumentoEventoRepositorioI
from src.interfaces.servicio import DocumentoEventoServicioI
from src.modelo.documento_evento import DocumentoEvento


class DocumentoEventoServicio(DocumentoEventoServicioI):
    """Implementa la lógica de negocio para consultar y crear documentos de eventos."""

    def __init__(
        self, repositorio_documento_evento: DocumentoEventoRepositorioI
    ) -> None:
        """Inicializa el servicio con su repositorio de documentos."""
        self.repositorio_documento_evento = repositorio_documento_evento

    def buscar_documento(self, dto: BuscarDocumentoDto) -> MostrarDocumentoDTO:
        """Busca un documento por su identificador y lo devuelve como DTO de salida."""
        documento = self.repositorio_documento_evento.select_by_id(
            dto.id_documento_evento
        )
        if documento:
            return MostrarDocumentoDTO(ruta_archivo=documento.ruta_archivo)
        # TODO(luis): que pasa si no se encuentra el documento con dicha ID
        # quiza lo maneje el controlador, no el servicio
        return MostrarDocumentoDTO()

    def buscar_documentos(self) -> list[MostrarDocumentoDTO]:
        """Obtiene todos los documentos registrados y los transforma a DTOs."""
        # Trae todos los documentos
        lista_documentos = self.repositorio_documento_evento.select_all()

        # Convertir cada documento a DTO de salida
        documentos_dto = []
        for documento in lista_documentos:
            dto_salida = MostrarDocumentoDTO(
                id_documento_evento=documento.id_documento_evento,
                ruta_archivo=documento.ruta_archivo,
            )
            documentos_dto.append(dto_salida)

        return documentos_dto

    def crear_documento(self, dto: CrearDocumentoDto) -> MostrarDocumentoDTO:
        """Genera un PDF para un documento y lo guarda en la base de datos."""
        datos = {"informacion": dto.texto, "nombre_imagen": "prueba.jpg"}

        html = render_template("plantilla_pdf_prueba.html", **datos)
        nombre_archivo = f"{dto.texto}.pdf"

        css = CSS("./src/static/css/cartas.css")
        HTML(
            string=html,
            base_url=app.config["DIRECTORIO_DOCUMENTOS"].joinpath("imagenes"),
        ).write_pdf(
            app.config["DIRECTORIO_DOCUMENTOS"].joinpath(nombre_archivo),
            stylesheets=[css],
        )

        documento_evento = DocumentoEvento()
        documento_evento.id_evento_academico = 1
        documento_evento.tipo_documento = TipoDocumento.DOCUMENTO_ORGANIZADOR
        documento_evento.subtipo_documento = SubtipoDocumento.CARTA_DISPENSA
        documento_evento.ruta_archivo = nombre_archivo

        self.repositorio_documento_evento.insert(documento_evento)

        return MostrarDocumentoDTO(ruta_archivo=documento_evento.ruta_archivo)
