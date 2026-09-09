class Automovil():
    id_automovil: int
    id_persona_academica: int
    placa: str
    modelo: str
    anio: str
    color: str

    def __init__(self, placa=None, modelo=None, anio=None, color=None, id_persona_academica=None):
        self.id_persona_academica = id_persona_academica
        # Usamos los setters para que validen
        self.placa = placa
        self.modelo = modelo
        self.anio = anio
        self.color = color

    @property
    def placa(self):
        return self._placa

    @placa.setter
    def placa(self, valor: str | None):
        if valor is not None:
            # Validar espacios en blanco (mensaje específico)
            if any(c.isspace() for c in valor):
                raise ValueError("La placa no puede contener espacios en blanco")
            # Validar longitud máxima
            if len(valor) > 10:
                raise ValueError("La placa no puede tener más de 10 caracteres")
            # Validar caracteres permitidos: alfanuméricos y guiones (sin espacios)
            if not all(c.isalnum() or c == '-' for c in valor):
                raise ValueError("La placa solo puede contener caracteres alfanuméricos y guiones")
        self._placa = valor

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, valor: str | None):
        if valor is not None:
            if len(valor) > 50:
                raise ValueError("El modelo no puede tener más de 50 caracteres")
            if not all(c.isalnum() or c.isspace() or c == '-' for c in valor):
                raise ValueError("El modelo solo puede contener caracteres alfanuméricos, espacios en blanco y guiones")
        self._modelo = valor

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, valor: str | None):
        if valor is not None:
            if len(valor) > 4:
                raise ValueError("El año no puede tener más de 4 caracteres")
            if not valor.isdigit():
                raise ValueError("El año solo puede contener caracteres numéricos")
        self._anio = valor

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, valor: str | None):
        if valor is not None:
            if len(valor) > 20:
                raise ValueError("El color no puede tener más de 20 caracteres")
            if not all(c.isalpha() or c.isspace() for c in valor):
                raise ValueError("El color solo puede contener caracteres de letras y espacios en blanco")
        self._color = valor