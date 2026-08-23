from flask import current_app as app
from flask import render_template
from src.interfaces.repositorio import DocumentoEventoRepositorioI
from src.dto.documento_evento import MostrarDocumentoDTO
from src.dto.documento_evento import BuscarDocumentoDto
from src.dto.documento_evento import CrearDocumentoDto
from weasyprint import HTML
from weasyprint import CSS
from src.modelo.documento_evento import DocumentoEvento
from src.enums import TipoDocumento
from src.enums import SubtipoDocumento
from src.interfaces.servicio import DocumentoEventoServicioI

class DocumentoEventoServicio(DocumentoEventoServicioI):
    
    def __init__(self, repositorio_documento_evento: DocumentoEventoRepositorioI) -> None:
        self.repositorio_documento_evento = repositorio_documento_evento

    def buscar_documento(self, dto: BuscarDocumentoDto) -> MostrarDocumentoDTO:
        documento = self.repositorio_documento_evento.select_by_id(dto.id_documento_evento)
        if documento:
            dto_salida = MostrarDocumentoDTO(ruta_archivo=documento.ruta_archivo)
            return dto_salida
        else:
            #TODO que pasa si no se encuentra el documento con dicha ID, quiza lo maneje el controlador, no el servicio            
            return MostrarDocumentoDTO()
    
    def buscar_documentos(self) -> list[MostrarDocumentoDTO]:
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

        datos = {
        "informacion": dto.texto,
        "nombre_imagen": 'prueba.jpg'
        }

        html = render_template(
            "plantilla_pdf_prueba.html",
            **datos
        )
        nombre_archivo = f'{dto.texto}.pdf'

        css = CSS('./src/static/css/cartas.css')
        HTML(string=html, base_url=app.config['DIRECTORIO_DOCUMENTOS'].joinpath('imagenes')).write_pdf(app.config['DIRECTORIO_DOCUMENTOS'].joinpath(nombre_archivo), stylesheets=[css])
        
        documento_evento = DocumentoEvento()
        documento_evento.id_evento_academico = 1
        documento_evento.tipo_documento = TipoDocumento.DOCUMENTO_ORGANIZADOR
        documento_evento.subtipo_documento = SubtipoDocumento.CARTA_DISPENSA
        documento_evento.ruta_archivo = nombre_archivo

        self.repositorio_documento_evento.insert(documento_evento)

        dto_salida = MostrarDocumentoDTO(ruta_archivo=documento_evento.ruta_archivo)
        return dto_salida


