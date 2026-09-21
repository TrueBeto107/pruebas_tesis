"""Controlador para peticiones sobre los componentes de jinja y tailwind."""

from flask import (
    get_template_attribute,
    render_template,
    render_template_string,
    request,
)
from jinja2 import Template


class ComponentesControlador:
    """Controlador para el blueprint de componentes.

    Atiende peticiones relacionadas al funcionamiento dinámico de los componentes
    """

    def renderizar_playground(self) -> str:
        """Regresa el HTML de la página demo para los componentes."""
        return render_template("playground.html")

    def renderizar_input_color(self) -> str:
        """Renderiza un input tipo color.

        Returns:
            str: HTML de un input de color con el valor asignado.

        """
        nombre_input = request.headers.get("HX-Trigger-Name")
        if not nombre_input:
            raise Exception  # TODO(luis): Crear una excepción o respuesta para
            # no actualizar la vista htmx
        valor = request.args.get(nombre_input)
        input_color_macro = get_template_attribute(
            "componentes/form_inputs.html", "input_color"
        )
        return input_color_macro(value=valor)
