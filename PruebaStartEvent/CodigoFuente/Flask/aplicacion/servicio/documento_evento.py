from flask import current_app as app
from flask import render_template
from aplicacion.repositorio.documento_evento import DocumentoEventoRepositorio
from aplicacion.dto.documento_evento import MostrarDocumentoDTO
from aplicacion.dto.documento_evento import BuscarDocumentoDto
from aplicacion.dto.documento_evento import CrearDocumentoDto
from flask import send_from_directory
from weasyprint import HTML
from weasyprint import CSS
from aplicacion.modelo.documento_evento import DocumentoEvento
from aplicacion.enums.tipo_documento import TipoDocumento
from aplicacion.enums.subtipo_documento import SubtipoDocumento

class DocumentoEventoServicio:
    
    repositorio = DocumentoEventoRepositorio()
    
    def documento(self):
        return render_template('buscar_documento.html')

    def buscar_documento(self, dto_entrada: BuscarDocumentoDto):
        documento = DocumentoEvento(id_documento_evento=dto_entrada.id_documento_evento)
        documento = self.repositorio.select(documento)
        dto_salida = MostrarDocumentoDTO(ruta_archivo=documento.ruta_archivo)
        return dto_salida
    
    def buscar_documentos(self):
        # Trae todos los documentos
        lista_documentos = self.repositorio.select_all()
        
        # Convertir cada documento a DTO de salida
        documentos_dto = []
        for documento in lista_documentos:
            dto_salida = MostrarDocumentoDTO(
                id_documento_evento=documento.id_documento_evento,
                ruta_archivo=documento.ruta_archivo,
            )
            documentos_dto.append(dto_salida)
        
        return documentos_dto

    def crear_documento(self, dto: CrearDocumentoDto):

        datos = {
        "informacion": dto.texto,
        "nombre_imagen": 'prueba.jpg'
        }

        html = render_template(
            "plantilla_pdf_prueba.html",
            **datos
        )
        nombre_archivo = f'{dto.texto}.pdf'

        css = CSS('./aplicacion/static/css/cartas.css')
        HTML(string=html, base_url=app.config['DIRECTORIO_DOCUMENTOS'].joinpath('imagenes')).write_pdf(app.config['DIRECTORIO_DOCUMENTOS'].joinpath(nombre_archivo), stylesheets=[css])
        
        documento_evento = DocumentoEvento()
        documento_evento.id_evento = 3
        documento_evento.tipo_documento = TipoDocumento.DOCUMENTO_ORGANIZADOR
        documento_evento.subtipo_documento = SubtipoDocumento.CARTA_DISPENSA
        documento_evento.ruta_archivo = nombre_archivo

        self.repositorio.insert(documento_evento)

        dto_salida = MostrarDocumentoDTO(ruta_archivo=documento_evento.ruta_archivo)
        return dto_salida


