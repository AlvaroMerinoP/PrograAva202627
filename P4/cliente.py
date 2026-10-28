"""Persona que visita la empresa como cliente."""

from __future__ import annotations

from types import NotImplementedType

from Time import Time
from ficha import Ficha


class Cliente(Ficha):
    """Extiende Ficha con un DNI privado; se compara por nombre y edad."""

    def __init__(
        self,
        nombre: str = "",
        edad: int = 0,
        nacio: Time | None = None,
        dni: str = "",
    ) -> None:
        """Inicializa los datos heredados y el DNI del cliente."""
        super().__init__(nombre, edad, nacio)
        self.dni = dni

    @property
    def dni(self) -> str:
        """Devuelve el DNI del cliente."""
        return self.__dni

    @dni.setter
    def dni(self, valor: str) -> None:
        """Asigna el DNI como texto, sin imponer un formato adicional."""
        if not isinstance(valor, str):
            raise TypeError("El DNI debe ser una cadena de texto.")
        self.__dni: str = valor.strip()

    def visualizar(self) -> None:
        """Muestra el tipo, los datos comunes y el DNI."""
        print("Tipo: Cliente")
        super().visualizar()
        print(f"DNI: {self.dni}")

    def __eq__(self, otro: object) -> bool | NotImplementedType:
        """Compara clientes por nombre y edad, sin comparar DNI ni hora."""
        if not isinstance(otro, Cliente):
            return NotImplemented
        return self.nombre == otro.nombre and self.edad == otro.edad
