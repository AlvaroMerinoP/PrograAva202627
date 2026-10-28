"""Clase base de las personas del registro diario."""

from __future__ import annotations

from Time import Time, format_time


class Ficha:
    """Almacena nombre, edad y hora de nacimiento en atributos privados."""

    def __init__(
        self, nombre: str = "", edad: int = 0, nacio: Time | None = None
    ) -> None:
        """Inicializa la ficha; la hora por defecto es 12:00:00 AM.

        Se crea una hora distinta por ficha para evitar compartir un objeto
        mutable como argumento por defecto.
        """
        self.nombre = nombre
        self.edad = edad
        if nacio is None:
            nacio = Time()
            nacio.set_time(12, 0, 0, "AM")
        self.nacio = nacio

    @property
    def nombre(self) -> str:
        """Devuelve el nombre de la persona."""
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        """Asigna el nombre; admite la cadena vacía del constructor."""
        if not isinstance(valor, str):
            raise TypeError("El nombre debe ser una cadena de texto.")
        self.__nombre: str = valor.strip()

    @property
    def edad(self) -> int:
        """Devuelve la edad en años."""
        return self.__edad

    @edad.setter
    def edad(self, valor: int) -> None:
        """Asigna una edad entera no negativa; rechaza booleanos."""
        if type(valor) is not int:
            raise TypeError("La edad debe ser un número entero.")
        if valor < 0:
            raise ValueError("La edad no puede ser negativa.")
        self.__edad: int = valor

    @property
    def nacio(self) -> Time:
        """Devuelve la hora de nacimiento, representada mediante Time."""
        return self.__nacio

    @nacio.setter
    def nacio(self, valor: Time) -> None:
        """Asigna una hora de nacimiento de la clase Time de la práctica 2."""
        if not isinstance(valor, Time):
            raise TypeError("La hora de nacimiento debe ser un objeto Time.")
        self.__nacio: Time = valor

    def visualizar(self) -> None:
        """Muestra los datos comunes; las clases derivadas lo redefinen."""
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Hora de nacimiento: {format_time(self.nacio)}")
