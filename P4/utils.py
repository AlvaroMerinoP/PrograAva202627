"""Funciones de entrada y menús; los errores se gestionan desde main.py."""

import math
from typing import List


def _leer_entrada(mensaje: str) -> str:
    """Lee texto tras comprobar que el mensaje es una cadena."""
    if not isinstance(mensaje, str):
        raise TypeError("El mensaje debe ser una cadena de texto.")
    return input(mensaje)


def leer_int(mensaje: str = "Introduce un número entero: ") -> int:
    """Lee un entero; lanza ValueError si el texto no representa un entero.

    Un mensaje de otro tipo provoca TypeError. No repite la lectura, para
    que el programa que llama pueda capturar y gestionar la excepción.
    """
    return int(_leer_entrada(mensaje))


def leer_float(mensaje: str = "Introduce un número decimal: ") -> float:
    """Lee un decimal finito con punto o coma; errores de valor: ValueError."""
    valor = float(_leer_entrada(mensaje).replace(",", "."))
    if not math.isfinite(valor):
        raise ValueError("El número decimal debe ser finito.")
    return valor


def leer_cadena(mensaje: str) -> str:
    """Lee texto sin espacios exteriores; una cadena vacía da ValueError."""
    valor = _leer_entrada(mensaje).strip()
    if not valor:
        raise ValueError("La cadena no puede estar vacía.")
    return valor


def crear_menu(opciones_menu: List[str]) -> int:
    """Muestra una lista de opciones y lee una selección entre 1 y su tamaño.

    Lanza TypeError si el argumento no es una lista de cadenas, y ValueError
    si está vacía, hay opciones en blanco o la selección está fuera de rango.
    Una selección no entera también provoca ValueError mediante leer_int.
    """
    if not isinstance(opciones_menu, list):
        raise TypeError("Las opciones del menú deben estar en una lista.")
    if any(not isinstance(opcion, str) for opcion in opciones_menu):
        raise TypeError("Cada opción del menú debe ser una cadena de texto.")
    if not opciones_menu or any(not opcion.strip() for opcion in opciones_menu):
        raise ValueError("El menú debe contener opciones de texto no vacías.")
    print()
    for numero, opcion in enumerate(opciones_menu, start=1):
        print(f"{numero}. {opcion}")
    seleccion = leer_int("Selecciona una opción: ")
    if not 1 <= seleccion <= len(opciones_menu):
        raise ValueError(f"Elige una opción entre 1 y {len(opciones_menu)}.")
    return seleccion
