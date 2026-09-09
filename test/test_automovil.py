import pytest
from src.dominio.automovil import Automovil  # Ajusta la ruta según tu proyecto

class TestAutomovilSetters:

    # -------- placa --------
    def test_set_placa_valida(self):
        auto = Automovil()
        auto.placa = "ABC-123"
        assert auto.placa == "ABC-123"

    def test_set_placa_none(self):
        auto = Automovil()
        auto.placa = None
        assert auto.placa is None

    def test_set_placa_demasiado_larga(self):
        auto = Automovil()
        with pytest.raises(ValueError, match="La placa no puede tener más de 10 caracteres"):
            auto.placa = "12345678901"  # 11 caracteres

    def test_set_placa_con_espacios(self):
        auto = Automovil()
        with pytest.raises(ValueError, match="La placa no puede contener espacios en blanco"):
            auto.placa = "ABC 123"

    def test_set_placa_caracteres_invalidos(self):
        auto = Automovil()
        with pytest.raises(ValueError, match="La placa solo puede contener caracteres alfanuméricos y guiones"):
            auto.placa = "ABC@123"  # @ no permitido

    # -------- modelo --------
    def test_set_modelo_valido(self):
        auto = Automovil()
        auto.modelo = "Toyota Corolla"
        assert auto.modelo == "Toyota Corolla"

    def test_set_modelo_none(self):
        auto = Automovil()
        auto.modelo = None
        assert auto.modelo is None

    def test_set_modelo_demasiado_largo(self):
        auto = Automovil()
        with pytest.raises(ValueError, match="El modelo no puede tener más de 50 caracteres"):
            auto.modelo = "A" * 51

    def test_set_modelo_caracteres_invalidos(self):
        auto = Automovil()
        with pytest.raises(ValueError, match="El modelo solo puede contener caracteres alfanuméricos, espacios en blanco y guiones"):
            auto.modelo = "Toyota@Corolla"

    # -------- anio --------
    def test_set_anio_valido(self):
        auto = Automovil()
        auto.anio = "2023"
        assert auto.anio == "2023"

    def test_set_anio_none(self):
        auto = Automovil()
        auto.anio = None
        assert auto.anio is None

    def test_set_anio_demasiado_largo(self):
        auto = Automovil()
        with pytest.raises(ValueError, match="El año no puede tener más de 4 caracteres"):
            auto.anio = "20201"

    def test_set_anio_no_numerico(self):
        auto = Automovil()
        with pytest.raises(ValueError, match="El año solo puede contener caracteres numéricos"):
            auto.anio = "20A0"

    # -------- color --------
    def test_set_color_valido(self):
        auto = Automovil()
        auto.color = "Rojo oscuro"
        assert auto.color == "Rojo oscuro"

    def test_set_color_none(self):
        auto = Automovil()
        auto.color = None
        assert auto.color is None

    def test_set_color_demasiado_largo(self):
        auto = Automovil()
        with pytest.raises(ValueError, match="El color no puede tener más de 20 caracteres"):
            auto.color = "Rojo oscuro metalizado brillante"  # >20

    def test_set_color_caracteres_invalidos(self):
        auto = Automovil()
        with pytest.raises(ValueError, match="El color solo puede contener caracteres de letras y espacios en blanco"):
            auto.color = "Rojo-azul"  # guion no permitido