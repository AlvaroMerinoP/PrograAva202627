"""Práctica 3: matrices float32. Ejecución: python3 matriz.py.

Requiere Python 3.10 o posterior y NumPy.
"""

from __future__ import annotations

import math
from typing import ClassVar

import numpy as np
from numpy.typing import NDArray


class MatrizFloat:
    """Representa una matriz dinámica 1D/2D con NumPy.

    Attributes:
        TIPO_DATO: Tipo de los elementos, compartido por la clase (float32).
        _matriz: Array protegido, o None mientras no se cree la matriz.
        _nfil: Número de filas de la matriz.
        _ncol: Número de columnas de la matriz.

    Las matrices 1D se almacenan como una fila y n columnas.
    """

    TIPO_DATO: ClassVar[type[np.float32]] = np.float32

    def __init__(self) -> None:
        """Inicializa este objeto sin matriz y con las dimensiones a cero."""
        self._matriz: NDArray[np.float32] | None = None
        self._nfil: int = 0
        self._ncol: int = 0

    # De clase: construye un objeto nuevo usando cls y su TIPO_DATO.
    @classmethod
    def matriz_identidad(cls, n: int) -> MatrizFloat:
        """Devuelve una identidad n x n; exige un tamaño entero positivo."""
        if type(n) is not int or n <= 0:
            raise ValueError("El tamaño debe ser un número entero positivo.")
        nueva_matriz = cls()
        nueva_matriz._matriz = np.eye(n, dtype=cls.TIPO_DATO)
        nueva_matriz._nfil = n
        nueva_matriz._ncol = n
        return nueva_matriz

    # Estático: compara dos objetos recibidos, sin necesitar self o cls.
    @staticmethod
    def mismas_dimensiones(m1: MatrizFloat, m2: MatrizFloat) -> bool:
        """Indica si ambas matrices existen y tienen iguales dimensiones."""
        return (
            m1.existe()
            and m2.existe()
            and m1._nfil == m2._nfil
            and m1._ncol == m2._ncol
        )

    def crear_matriz2D(self, nfil: int, ncol: int) -> None:
        """Crea una matriz de ceros con dimensiones enteras positivas.

        Una dimensión inválida provoca ValueError y conserva la matriz previa.
        """
        if type(nfil) is not int or type(ncol) is not int:
            raise ValueError("Las dimensiones deben ser números enteros.")
        if nfil <= 0 or ncol <= 0:
            raise ValueError("El número de filas y columnas debe ser positivo.")
        self._matriz = np.zeros((nfil, ncol), dtype=self.TIPO_DATO)
        self._nfil = nfil
        self._ncol = ncol

    def crear_matriz1D(self, n_elementos: int) -> None:
        """Crea una fila de ceros delegando en crear_matriz2D."""
        self.crear_matriz2D(1, n_elementos)

    def existe(self) -> bool:
        """Devuelve True si el array está creado y contiene elementos."""
        return self._matriz is not None and self._matriz.size > 0

    def introducir(self) -> None:
        """Lee cada elemento; lanza ValueError si la matriz no existe.

        Repite la lectura de valores inválidos o fuera del rango float32.
        Los índices que se muestran al usuario empiezan en cero.
        """
        if not self.existe():
            raise ValueError("Primero debe construir una matriz.")
        limite = float(np.finfo(self.TIPO_DATO).max)
        for fila in range(self._nfil):
            for columna in range(self._ncol):
                while True:
                    valor = leer_float(f"Elemento [{fila}, {columna}]: ")
                    if abs(valor) <= limite:
                        self._matriz[fila, columna] = valor
                        break
                    print("El valor está fuera del rango de float32.")

    def mostrar(self) -> None:
        """Muestra dimensiones y elementos, o avisa si la matriz no existe."""
        if not self.existe():
            print("La matriz no está creada o está vacía.")
            return
        print(f"Dimensiones: {self._nfil} fila(s) x {self._ncol} columna(s)")
        print(self._matriz)

    def sumar_matrices(self, otra_matriz: MatrizFloat) -> MatrizFloat:
        """Devuelve una suma nueva sin modificar los operandos.

        Lanza ValueError si falta alguna matriz o sus dimensiones no coinciden.
        """
        if not self.mismas_dimensiones(self, otra_matriz):
            raise ValueError("Ambas matrices deben existir y tener las mismas dimensiones.")
        resultado = MatrizFloat()
        resultado.crear_matriz2D(self._nfil, self._ncol)
        resultado._matriz = self._matriz + otra_matriz._matriz
        return resultado

    def restar_matrices(self, otra_matriz: MatrizFloat) -> MatrizFloat:
        """Devuelve self - otra_matriz sin modificar los operandos.

        Lanza ValueError si falta alguna matriz o sus dimensiones no coinciden.
        """
        if not self.mismas_dimensiones(self, otra_matriz):
            raise ValueError("Ambas matrices deben existir y tener las mismas dimensiones.")
        resultado = MatrizFloat()
        resultado.crear_matriz2D(self._nfil, self._ncol)
        resultado._matriz = self._matriz - otra_matriz._matriz
        return resultado


def leer_int(mensaje: str = "Introduce un número entero: ") -> int:
    """Lee un entero y repite la petición si la entrada es inválida."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada no válida. Introduce un número entero.")


def leer_float(mensaje: str = "Introduce un número decimal: ") -> float:
    """Lee un decimal finito con punto o coma; repite ante entradas inválidas."""
    while True:
        try:
            valor = float(input(mensaje).replace(",", "."))
            if math.isfinite(valor):
                return valor
        except ValueError:
            pass
        print("Entrada no válida. Introduce un número decimal finito.")


def crear_menu(opciones_menu: list[str]) -> int:
    """Muestra opciones numeradas desde 1 y devuelve una selección válida.

    Lanza ValueError si la lista está vacía.
    """
    if not opciones_menu:
        raise ValueError("El menú debe contener al menos una opción.")
    print()
    for numero, opcion in enumerate(opciones_menu, start=1):
        print(f"{numero}. {opcion}")
    while True:
        seleccion = leer_int("Selecciona una opción: ")
        if 1 <= seleccion <= len(opciones_menu):
            return seleccion
        print(f"Opción no válida. Elige entre 1 y {len(opciones_menu)}.")


def operaciones_matrices(matriz: MatrizFloat) -> None:
    """Ejecuta el submenú de suma y resta sobre la matriz actual.

    Pide dimensiones y valores de una segunda matriz en cada operación.
    Muestra el resultado sin sustituir las matrices originales.
    """
    if not matriz.existe():
        print("Primero debe construir una matriz.")
        return
    opciones = ["Sumar matrices", "Restar matrices", "Volver al menú principal"]
    while True:
        print("\nOperaciones con matrices")
        opcion = crear_menu(opciones)
        if opcion == 3:
            return
        try:
            print("\nSegunda matriz")
            nfil = leer_int("Número de filas (1 para una matriz 1D): ")
            ncol = leer_int("Número de columnas: ")
            otra_matriz = MatrizFloat()
            otra_matriz.crear_matriz2D(nfil, ncol)
            if not MatrizFloat.mismas_dimensiones(matriz, otra_matriz):
                raise ValueError("La segunda matriz debe tener las mismas dimensiones.")
            otra_matriz.introducir()
            if opcion == 1:
                resultado = matriz.sumar_matrices(otra_matriz)
                print("\nResultado de la suma:")
            else:
                resultado = matriz.restar_matrices(otra_matriz)
                print("\nResultado de la resta:")
            resultado.mostrar()
        except ValueError as error:
            print(f"Error: {error}")


def main() -> None:
    """Gestiona el menú principal, las entradas inválidas y la salida."""
    matriz = MatrizFloat()
    opciones = [
        "Construir matriz 1D",
        "Construir matriz 2D",
        "Construir matriz identidad",
        "Introducir matriz",
        "Mostrar matriz",
        "Operaciones con matrices",
        "Terminar",
    ]
    while True:
        try:
            print("\nMenú principal")
            opcion = crear_menu(opciones)
            if opcion == 1:
                n_elementos = leer_int("Número de elementos: ")
                matriz.crear_matriz1D(n_elementos)
                print("Matriz 1D creada.")
            elif opcion == 2:
                nfil = leer_int("Número de filas: ")
                ncol = leer_int("Número de columnas: ")
                matriz.crear_matriz2D(nfil, ncol)
                print("Matriz 2D creada.")
            elif opcion == 3:
                n = leer_int("Tamaño de la matriz identidad: ")
                matriz = MatrizFloat.matriz_identidad(n)
                print("Matriz identidad creada.")
            elif opcion == 4:
                matriz.introducir()
                print("Valores guardados.")
            elif opcion == 5:
                matriz.mostrar()
            elif opcion == 6:
                operaciones_matrices(matriz)
            else:
                print("Programa terminado.")
                return
        except ValueError as error:
            print(f"Error: {error}")
        except (EOFError, KeyboardInterrupt):
            print("\nPrograma terminado.")
            return


if __name__ == "__main__":
    main()
