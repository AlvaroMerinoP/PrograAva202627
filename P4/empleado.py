"""Persona que trabaja en la empresa."""

from __future__ import annotations

from Time import Time
from ficha import Ficha


class Empleado(Ficha):
    """Extiende Ficha con categoría y años de antigüedad privados."""

    def __init__(
        self,
        nombre: str = "",
        edad: int = 0,
        nacio: Time | None = None,
        categoria: str = "",
        antiguedad: int = 0,
    ) -> None:
        """Inicializa los datos heredados y los específicos del empleado."""
        super().__init__(nombre, edad, nacio)
        self.categoria = categoria
        self.antiguedad = antiguedad

    @property
    def categoria(self) -> str:
        """Devuelve la categoría profesional."""
        return self.__categoria

    @categoria.setter
    def categoria(self, valor: str) -> None:
        """Asigna una categoría expresada como cadena de texto."""
        if not isinstance(valor, str):
            raise TypeError("La categoría debe ser una cadena de texto.")
        self.__categoria: str = valor.strip()

    @property
    def antiguedad(self) -> int:
        """Devuelve los años de antigüedad en la empresa."""
        return self.__antiguedad

    @antiguedad.setter
    def antiguedad(self, valor: int) -> None:
        """Asigna años enteros no negativos; rechaza booleanos."""
        if type(valor) is not int:
            raise TypeError("La antigüedad debe ser un número entero.")
        if valor < 0:
            raise ValueError("La antigüedad no puede ser negativa.")
        self.__antiguedad: int = valor

    def visualizar(self) -> None:
        """Muestra el tipo, los datos comunes, la categoría y la antigüedad."""
        print("Tipo: Empleado")
        super().visualizar()
        print(f"Categoría: {self.categoria}")
        print(f"Antigüedad: {self.antiguedad} año(s)")
