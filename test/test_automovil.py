"""Pruebas unitarias para el modelo Automovil.

Note:
    Este archivo contiene pruebas unitarias para el modelo Automovil.

"""

import pytest

from src.dominio.automovil import Automovil  # Ajusta la ruta según tu proyecto


class TestAutomovilSetters:
    """Pruebas unitarias para los setters del modelo Automovil.

    Note:
        Cada método de prueba verifica la funcionalidad de un setter
        específico del modelo Automovil.

    """

    # -------- placa --------
    def test_set_placa_valida(self) -> None:
        """Verifica que el setter de 'placa' acepte un valor válido.

        Comprueba que al asignar una placa con formato correcto (por ejemplo,
        "ABC-123"), el atributo 'placa' del modelo Automovil almacene
        exactamente el valor asignado.

        Note:
            Se considera una placa válida aquella que cumple con el formato
            esperado por el modelo (letras y números separados por guion).

        """
        auto = Automovil()
        auto.placa = "ABC-123"
        assert auto.placa == "ABC-123"

    def test_set_placa_none(self) -> None:
        """Verifica que el setter de 'placa' acepte un valor None.

        Comprueba que al asignar None a la placa, el atributo 'placa' del
        modelo Automovil almacene exactamente ese valor.

        Note:
            Se permite que la placa sea None, lo que indica que no se ha
            asignado ninguna placa al automóvil.

        """
        auto = Automovil()
        auto.placa = None
        assert auto.placa is None

    def test_set_placa_none(self) -> None:
        """Verifica que el setter de 'placa' acepte un valor None.

        Comprueba que al asignar None a la placa, el atributo 'placa' del
        modelo Automovil almacene exactamente ese valor.

        Note:
            Se permite que la placa sea None, lo que indica que no se ha
            asignado ninguna placa al automóvil.

        """
        auto = Automovil()
        auto.placa = None
        assert auto.placa is None


    def test_set_placa_demasiado_larga(self) -> None:
        """Verifica que el setter de 'placa' rechace cadenas demasiado largas.

        Comprueba que al intentar asignar una placa de 11 caracteres se
        lance una excepción ValueError, ya que el máximo permitido es 10.

        Raises:
            ValueError: Si la placa tiene más de 10 caracteres.

        """
        auto = Automovil()
        with pytest.raises(
            ValueError, match="La placa no puede tener más de 10 caracteres"
        ):
            auto.placa = "12345678901"  # 11 caracteres


    def test_set_placa_con_espacios(self) -> None:
        """Verifica que el setter de 'placa' rechace cadenas con espacios.

        Comprueba que al intentar asignar una placa que contiene un espacio
        en blanco se lance una excepción ValueError.

        Raises:
            ValueError: Si la placa contiene espacios en blanco.

        """
        auto = Automovil()
        with pytest.raises(
            ValueError, match="La placa no puede contener espacios en blanco"
        ):
            auto.placa = "ABC 123"


    def test_set_placa_caracteres_invalidos(self) -> None:
        """Verifica que el setter de 'placa' rechace caracteres no permitidos.

        Comprueba que al intentar asignar una placa con caracteres distintos
        de los alfanuméricos o guiones se lance una excepción ValueError.

        Raises:
            ValueError: Si la placa contiene caracteres no alfanuméricos
            ni guiones.

        """
        auto = Automovil()
        with pytest.raises(
            ValueError,
            match = "La placa solo admite letras, números y guiones"
        ):
            auto.placa = "ABC@123"  # @ no permitido


    # -------- modelo --------
    def test_set_modelo_valido(self) -> None:
        """Verifica que el setter de 'modelo' acepte un valor válido.

        Comprueba que al asignar un modelo con formato correcto (por ejemplo,
        "Toyota Corolla"), el atributo 'modelo' del modelo Automovil almacene
        exactamente el valor asignado.

        Note:
            Se considera un modelo válido aquel que contiene caracteres
            alfanuméricos, espacios en blanco y guiones.

        """
        auto = Automovil()
        auto.modelo = "Toyota Corolla"
        assert auto.modelo == "Toyota Corolla"


    def test_set_modelo_none(self) -> None:
        """Verifica que el setter de 'modelo' acepte un valor None.

        Comprueba que al asignar None al modelo, el atributo 'modelo' del
        modelo Automovil almacene exactamente ese valor.

        Note:
            Se permite que el modelo sea None, lo que indica que no se ha
            asignado ningún modelo al automóvil.

        """
        auto = Automovil()
        auto.modelo = None
        assert auto.modelo is None


    def test_set_modelo_demasiado_largo(self) -> None:
        """Verifica que el setter de 'modelo' rechace cadenas demasiado largas.

        Comprueba que al intentar asignar un modelo de 51 caracteres se
        lance una excepción ValueError, ya que el máximo permitido es 50.

        Raises:
            ValueError: Si el modelo tiene más de 50 caracteres.

        """
        auto = Automovil()
        with pytest.raises(
            ValueError, match="El modelo no puede tener más de 50 caracteres"
        ):
            auto.modelo = "A" * 51


    def test_set_modelo_caracteres_invalidos(self) -> None:
        """Verifica que el setter de 'modelo' rechace caracteres no permitidos.

        Comprueba que al intentar asignar un modelo con caracteres distintos
        de los alfanuméricos, espacios en blanco o guiones se lance una
        excepción ValueError.

        Raises:
            ValueError: Si el modelo contiene caracteres no permitidos.

        """
        auto = Automovil()
        with pytest.raises(
            ValueError,
            match="El modelo solo admite caracteres alfanuméricos y guiones",
        ):
            auto.modelo = "Toyota@Corolla"


    # -------- anio --------
    def test_set_anio_valido(self) -> None:
        """Verifica que el setter de 'anio' acepte un valor válido.

        Comprueba que al asignar un año con formato correcto (por ejemplo,
        "2023"), el atributo 'anio' del modelo Automovil almacene
        exactamente el valor asignado.

        Note:
            Se considera un año válido aquel que contiene únicamente
            caracteres numéricos.

        """
        auto = Automovil()
        auto.anio = "2023"
        assert auto.anio == "2023"


    def test_set_anio_none(self) -> None:
        """Verifica que el setter de 'anio' acepte un valor None.

        Comprueba que al asignar None al año, el atributo 'anio' del modelo
        Automovil almacene exactamente ese valor.

        Note:
            Se permite que el año sea None, lo que indica que no se ha
            asignado ningún año al automóvil.

        """
        auto = Automovil()
        auto.anio = None
        assert auto.anio is None


    def test_set_anio_demasiado_largo(self) -> None:
        """Verifica que el setter de 'anio' rechace cadenas demasiado largas.

        Comprueba que al intentar asignar un año de 5 caracteres se lance
        una excepción ValueError, ya que el máximo permitido es 4.

        Raises:
            ValueError: Si el año tiene más de 4 caracteres.

        """
        auto = Automovil()
        with pytest.raises(
            ValueError, match="El año no puede tener más de 4 caracteres"
        ):
            auto.anio = "20201"


    def test_set_anio_no_numerico(self) -> None:
        """Verifica que el setter de 'anio' rechace caracteres no numéricos.

        Comprueba que al intentar asignar un año que contiene letras se
        lance una excepción ValueError.

        Raises:
            ValueError: Si el año contiene caracteres no numéricos.

        """
        auto = Automovil()
        with pytest.raises(
            ValueError, match="El año solo puede contener caracteres numéricos"
        ):
            auto.anio = "20A0"


    # -------- color --------
    def test_set_color_valido(self) -> None:
        """Verifica que el setter de 'color' acepte un valor válido.

        Comprueba que al asignar un color con formato correcto (por ejemplo,
        "Rojo oscuro"), el atributo 'color' del modelo Automovil almacene
        exactamente el valor asignado.

        Note:
            Se considera un color válido aquel que contiene únicamente
            letras y espacios en blanco.

        """
        auto = Automovil()
        auto.color = "Rojo oscuro"
        assert auto.color == "Rojo oscuro"


    def test_set_color_none(self) -> None:
        """Verifica que el setter de 'color' acepte un valor None.

        Comprueba que al asignar None al color, el atributo 'color' del
        modelo Automovil almacene exactamente ese valor.

        Note:
            Se permite que el color sea None, lo que indica que no se ha
            asignado ningún color al automóvil.

        """
        auto = Automovil()
        auto.color = None
        assert auto.color is None


    def test_set_color_demasiado_largo(self) -> None:
        """Verifica que el setter de 'color' rechace cadenas demasiado largas.

        Comprueba que al intentar asignar un color de más de 20 caracteres
        se lance una excepción ValueError.

        Raises:
            ValueError: Si el color tiene más de 20 caracteres.

        """
        auto = Automovil()
        with pytest.raises(
            ValueError, match="El color no puede tener más de 20 caracteres"
        ):
            auto.color = "Rojo oscuro metalizado brillante"  # >20


    def test_set_color_caracteres_invalidos(self) -> None:
        """Verifica que el setter de 'color' rechace caracteres no permitidos.

        Comprueba que al intentar asignar un color con caracteres distintos
        de letras y espacios en blanco (por ejemplo, un guion) se lance una
        excepción ValueError.

        Raises:
            ValueError: Si el color contiene caracteres no permitidos.

        """
        auto = Automovil()
        with pytest.raises(
            ValueError,
            match=(
                "El color solo puede contener caracteres "
                "de letras y espacios en blanco"
            ),
        ):
            # guion no permitido
            auto.color = "Rojo-azul"
