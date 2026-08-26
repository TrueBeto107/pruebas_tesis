from flask import render_template, request
from flask_jwt_extended import current_user

from src.dto.documento_evento import BuscarDocumentoDto, CrearDocumentoDto
from src.servicio.documento_evento import DocumentoEventoServicio


class DocumentoControlador:
    def __init__(self, servicio: DocumentoEventoServicio):
        self.servicio = servicio

    def _crear_documento(self, texto):
        dto = CrearDocumentoDto(texto=texto)
        return self.servicio.crear_documento(dto)

    def _buscar_todos_documentos(self):
        return self.servicio.buscar_documentos()

    def _buscar_documento_por_id(self, id_documento):
        dto = BuscarDocumentoDto(id_documento_evento=id_documento)
        return self.servicio.buscar_documento(dto)

    def rederizar_gestion_documentos(self):
        documentos = self._buscar_todos_documentos()
        return render_template(
            "buscar_documento.html", documentos=documentos, nombre=current_user.nombre
        )

    def renderizar_tabla(self):
        documentos = self._buscar_todos_documentos()
        return render_template("tabla.html", documentos=documentos)

    def renderizar_documento(self, ruta):
        return render_template("visor.html", ruta_archivo=ruta)

    def renderizar_documento_por_id(self):
        id = request.args.get("id_documento")
        resultado = self._buscar_documento_por_id(id)
        return self.renderizar_documento(resultado.ruta_archivo)

    def renderizar_documento_creado(self, texto):
        resultado = self._crear_documento(texto)

        html_pdf = self.renderizar_documento(resultado.ruta_archivo)
        html_pdf = '<div id="div-pdf" hx-swap-oob="true">\n' + html_pdf + "</div>"

        html_tabla = self.renderizar_tabla()
        html_tabla = '<div id="div-tabla" hx-swap-oob="true">\n' + html_tabla + "</div>"

        return html_pdf + html_tabla
