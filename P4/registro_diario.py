"""Registro diario de empleados y clientes de una empresa."""

from __future__ import annotations

from types import NotImplementedType
from typing import List

from cliente import Cliente
from empleado import Empleado
from ficha import Ficha


class RegistroDiario:
    """Agrupa personas y utiliza sus métodos visualizar de forma polimórfica."""

    def __init__(self) -> None:
        """Crea una lista privada y vacía de personas."""
        self.__personas: List[Ficha] = []

    @property
    def personas(self) -> List[Ficha]:
        """Devuelve una copia de la lista; las altas usan agregar_persona.

        Los objetos contenidos son los mismos, no copias de las personas.
        """
        return self.__personas.copy()

    def agregar_persona(self, persona: Ficha) -> None:
        """Añade empleados o clientes; otros objetos provocan TypeError."""
        if not isinstance(persona, (Empleado, Cliente)):
            raise TypeError("El registro solo admite objetos Empleado o Cliente.")
        self.__personas.append(persona)

    def visualizar_registro(self) -> None:
        """Muestra cada persona llamando a su versión de visualizar."""
        if not self.__personas:
            print("El registro diario está vacío.")
            return
        for indice, persona in enumerate(self.__personas):
            print(f"\nPersona [{indice}]")
            persona.visualizar()

    def visualizar_empleados(self) -> None:
        """Muestra solo empleados, conservando sus índices en el registro."""
        hay_empleados = False
        for indice, persona in enumerate(self.__personas):
            if self.es_empleado(persona):
                print(f"\nPersona [{indice}]")
                persona.visualizar()
                hay_empleados = True
        if not hay_empleados:
            print("No hay empleados en el registro.")

    @staticmethod
    def es_empleado(persona: object) -> bool:
        """Comprueba el tipo sin necesitar una instancia de RegistroDiario."""
        return isinstance(persona, Empleado)

    def __getitem__(self, indice: int) -> Ficha:
        """Accede por índice, incluidos negativos, como una lista de Python.

        Lanza TypeError si no es un entero e IndexError si está fuera de rango.
        """
        if type(indice) is not int:
            raise TypeError("El índice debe ser un número entero.")
        return self.__personas[indice]

    def __len__(self) -> int:
        """Devuelve el número de personas registradas."""
        return len(self.__personas)

    def __add__(self, otro: object) -> RegistroDiario | NotImplementedType:
        """Crea un registro con ambas listas, sin modificar los originales.

        Conserva el orden, los duplicados y las referencias a las personas.
        """
        if not isinstance(otro, RegistroDiario):
            return NotImplemented
        combinado = RegistroDiario()
        for persona in self.__personas + otro.__personas:
            combinado.agregar_persona(persona)
        return combinado
