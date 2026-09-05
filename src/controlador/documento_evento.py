"""Controlador de documentos de eventos para gestión y visualización de documentos.

TODOS los Docstrings de este módulo fueron generados con IA y no revisados.

Maneja las peticiones relacionadas con la búsqueda, creación y renderización
de documentos de eventos, proporcionando funcionalidades para visualizar,
crear y listar documentos.
"""

from flask import render_template, request
from flask_jwt_extended import current_user

from src.dto.documento_evento import (
    BuscarDocumentoDto,
    CrearDocumentoDto,
    MostrarDocumentoDTO,
)
from src.servicio.documento_evento import DocumentoEventoServicio


class DocumentoControlador:
    """Controlador para la gestión y visualización de documentos de eventos.

    Proporciona funcionalidades para crear, buscar, renderizar y visualizar
    documentos de eventos, incluyendo generación de PDFs.
    """

    def __init__(self, servicio: DocumentoEventoServicio) -> None:
        """Inicializa el controlador con el servicio de documentos de eventos.

        Args:
            servicio (DocumentoEventoServicio): instancia del servicio de documentos.

        """
        self._servicio = servicio

    def _crear_documento(self, texto: str) -> MostrarDocumentoDTO:
        """Crea un nuevo documento de evento a partir del texto proporcionado.

        Args:
            texto (str): contenido de texto del documento a crear.

        Returns:
            MostrarDocumentoDTO: DTO con información del documento creado.

        """
        dto = CrearDocumentoDto(texto=texto)
        return self._servicio.crear_documento(dto)

    def _buscar_todos_documentos(self) -> list[MostrarDocumentoDTO]:
        """Busca todos los documentos de eventos disponibles.

        Returns:
            list[MostrarDocumentoDTO]: lista de DTOs con información de documentos.

        """
        return self._servicio.buscar_documentos()

    def _buscar_documento_por_id(
        self, id_documento: int
    ) -> MostrarDocumentoDTO:
        """Busca un documento de evento específico por su ID.

        Args:
            id_documento (int): identificador único del documento.

        Returns:
            MostrarDocumentoDTO: DTO con información del documento encontrado.

        """
        dto = BuscarDocumentoDto(id_documento_evento=id_documento)
        return self._servicio.buscar_documento(dto)

    def rederizar_gestion_documentos(self) -> str:
        """Renderiza la página de gestión de documentos.

        Genera HTML con la lista de todos los documentos y el nombre del usuario
        autenticado actual.

        Returns:
            str: HTML de la página de gestión de documentos.

        """
        documentos = self._buscar_todos_documentos()
        return render_template(
            "buscar_documento.html",
            documentos=documentos,
            nombre=current_user.nombres,
        )

    def renderizar_tabla(self) -> str:
        """Renderiza una tabla HTML con todos los documentos.

        Returns:
            str: HTML de la tabla de documentos.

        """
        documentos = self._buscar_todos_documentos()
        return render_template("tabla.html", documentos=documentos)

    def renderizar_documento(self, ruta: str) -> str:
        """Renderiza un visor de documento basado en la ruta del archivo.

        Args:
            ruta (str): ruta del archivo del documento a visualizar.

        Returns:
            str: HTML del visor de documento.

        """
        return render_template("visor.html", ruta_archivo=ruta)

    def renderizar_documento_por_id(self) -> str:
        """Renderiza un documento específico obteniendo su ID de los parámetros de la solicitud.

        Obtiene el ID del documento de los parámetros query de la petición y renderiza
        el visor del documento correspondiente.

        Returns:
            str: HTML del visor de documento.

        """
        id_ = request.args.get("id_documento")
        resultado = self._buscar_documento_por_id(id_)
        return self.renderizar_documento(resultado.ruta_archivo)

    def renderizar_documento_creado(self, texto: str) -> str:
        """Renderiza un documento recién creado con actualización de tabla (HTMX).

        Crea un nuevo documento a partir del texto, renderiza su visor y actualiza
        la tabla de documentos usando intercambio fuera de banda de HTMX.

        Args:
            texto (str): contenido de texto del documento a crear y mostrar.

        Returns:
            str: HTML combinado del visor de documento y tabla actualizada.

        """
        resultado = self._crear_documento(texto)

        html_pdf = self.renderizar_documento(resultado.ruta_archivo)
        html_pdf = (
            '<div id="div-pdf" hx-swap-oob="true">\n' + html_pdf + "</div>"
        )

        html_tabla = self.renderizar_tabla()
        html_tabla = (
            '<div id="div-tabla" hx-swap-oob="true">\n' + html_tabla + "</div>"
        )

        return html_pdf + html_tabla
