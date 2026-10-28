"""Pruebas de la práctica 3, ejecutables con unittest y NumPy."""

import io
from contextlib import redirect_stdout
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

import numpy as np

from matriz import MatrizFloat, crear_menu, leer_float, leer_int, main


class TestMatrizFloat(unittest.TestCase):
    """Comprueba los resultados y el estado de los objetos."""

    def test_estado_inicial(self):
        matriz = MatrizFloat()
        self.assertIsNone(matriz._matriz)
        self.assertEqual((matriz._nfil, matriz._ncol), (0, 0))
        self.assertFalse(matriz.existe())

    def test_crear_2d(self):
        matriz = MatrizFloat()
        matriz.crear_matriz2D(2, 3)
        self.assertTrue(matriz.existe())
        self.assertEqual((matriz._nfil, matriz._ncol), (2, 3))
        self.assertEqual(matriz._matriz.dtype, np.float32)
        np.testing.assert_array_equal(matriz._matriz, np.zeros((2, 3)))

    def test_crear_1d(self):
        matriz = MatrizFloat()
        matriz.crear_matriz1D(4)
        self.assertEqual((matriz._nfil, matriz._ncol), (1, 4))
        self.assertEqual(matriz._matriz.dtype, np.float32)
        np.testing.assert_array_equal(matriz._matriz, [[0, 0, 0, 0]])

    def test_identidad(self):
        matriz = MatrizFloat.matriz_identidad(3)
        self.assertEqual((matriz._nfil, matriz._ncol), (3, 3))
        self.assertEqual(matriz._matriz.dtype, np.float32)
        np.testing.assert_array_equal(matriz._matriz, np.eye(3))

    def test_identidad_usa_cls(self):
        class MatrizDerivada(MatrizFloat):
            pass

        self.assertIsInstance(MatrizDerivada.matriz_identidad(1), MatrizDerivada)

    def test_dimensiones_invalidas_conservan_matriz(self):
        matriz = MatrizFloat.matriz_identidad(2)
        for nfil, ncol in [(0, 2), (2, -1), (1.5, 2), (2, "3"), (True, 2)]:
            with self.subTest(nfil=nfil, ncol=ncol):
                with self.assertRaises(ValueError):
                    matriz.crear_matriz2D(nfil, ncol)
                self.assertEqual((matriz._nfil, matriz._ncol), (2, 2))
                np.testing.assert_array_equal(matriz._matriz, np.eye(2))

    def test_tamanos_invalidos(self):
        for n in [0, -1, 2.5, "2", True]:
            with self.subTest(n=n):
                with self.assertRaises(ValueError):
                    MatrizFloat.matriz_identidad(n)
                with self.assertRaises(ValueError):
                    MatrizFloat().crear_matriz1D(n)

    def test_mismas_dimensiones(self):
        matriz = MatrizFloat.matriz_identidad(2)
        self.assertTrue(MatrizFloat.mismas_dimensiones(matriz, matriz))
        self.assertFalse(MatrizFloat.mismas_dimensiones(matriz, MatrizFloat()))
        self.assertFalse(MatrizFloat.mismas_dimensiones(MatrizFloat(), matriz))
        self.assertFalse(MatrizFloat.mismas_dimensiones(MatrizFloat(), MatrizFloat()))

    def test_operaciones_y_operandos_independientes(self):
        primera = MatrizFloat()
        primera.crear_matriz2D(2, 2)
        primera._matriz[:] = [[1.5, -2], [3, 0.25]]
        segunda = MatrizFloat()
        segunda.crear_matriz2D(2, 2)
        segunda._matriz[:] = [[0.5, 4], [-1, 2.75]]
        datos_primera = primera._matriz.copy()
        datos_segunda = segunda._matriz.copy()
        casos = [
            (primera.sumar_matrices, [[2, 2], [2, 3]]),
            (primera.restar_matrices, [[1, -6], [4, -2.5]]),
        ]
        for operacion, esperado in casos:
            with self.subTest(operacion=operacion.__name__):
                resultado = operacion(segunda)
                self.assertEqual((resultado._nfil, resultado._ncol), (2, 2))
                self.assertEqual(resultado._matriz.dtype, np.float32)
                np.testing.assert_allclose(resultado._matriz, esperado)
                resultado._matriz[0, 0] = 99
                np.testing.assert_array_equal(primera._matriz, datos_primera)
                np.testing.assert_array_equal(segunda._matriz, datos_segunda)

    def test_operaciones_1d(self):
        primera, segunda = MatrizFloat(), MatrizFloat()
        primera.crear_matriz1D(3)
        segunda.crear_matriz1D(3)
        primera._matriz[:] = [[1, 2, 3]]
        segunda._matriz[:] = [[4, 5, 6]]
        np.testing.assert_array_equal(primera.sumar_matrices(segunda)._matriz, [[5, 7, 9]])
        np.testing.assert_array_equal(primera.restar_matrices(segunda)._matriz, [[-3, -3, -3]])

    def test_operaciones_rechazan_matrices_inexistentes_y_broadcasting(self):
        matriz = MatrizFloat.matriz_identidad(2)
        fila = MatrizFloat()
        fila.crear_matriz1D(2)
        for primera, segunda in [(matriz, fila), (matriz, MatrizFloat()), (MatrizFloat(), matriz)]:
            for nombre in ["sumar_matrices", "restar_matrices"]:
                with self.subTest(operacion=nombre, dimensiones=segunda._nfil):
                    with self.assertRaises(ValueError):
                        getattr(primera, nombre)(segunda)

    def test_introducir_sin_crear(self):
        with self.assertRaises(ValueError):
            MatrizFloat().introducir()

    def test_introducir_valida_y_recorre_filas(self):
        matriz = MatrizFloat()
        matriz.crear_matriz2D(2, 2)
        entradas = ["texto", "1e99", "1.5", "-2", "3,25", "0"]
        with patch("builtins.input", side_effect=entradas), redirect_stdout(io.StringIO()):
            matriz.introducir()
        np.testing.assert_array_equal(matriz._matriz, [[1.5, -2], [3.25, 0]])

    def test_mostrar(self):
        salida = io.StringIO()
        with redirect_stdout(salida):
            MatrizFloat().mostrar()
            MatrizFloat.matriz_identidad(1).mostrar()
        self.assertIn("no está creada", salida.getvalue())
        self.assertIn("1 fila(s) x 1 columna(s)", salida.getvalue())
        self.assertIn("[[1.]]", salida.getvalue())


class TestConsola(unittest.TestCase):
    """Comprueba lecturas y recorridos del programa con entradas simuladas."""

    def test_leer_int_reintenta(self):
        with patch("builtins.input", side_effect=["hola", "1.5", "-3"]), redirect_stdout(io.StringIO()):
            self.assertEqual(leer_int(), -3)

    def test_leer_float_reintenta(self):
        entradas = ["hola", "nan", "inf", "1e999", "-2,5"]
        with patch("builtins.input", side_effect=entradas), redirect_stdout(io.StringIO()):
            self.assertEqual(leer_float(), -2.5)

    def test_menu_valida_opcion(self):
        with patch("builtins.input", side_effect=["x", "0", "4", "2"]), redirect_stdout(io.StringIO()):
            self.assertEqual(crear_menu(["Primera", "Segunda"]), 2)
        with self.assertRaises(ValueError):
            crear_menu([])

    def test_main_controla_errores_y_conserva_matriz(self):
        entradas = ["5", "4", "6", "3", "1", "1", "0", "5", "6", "1", "2", "2", "3", "7"]
        salida = io.StringIO()
        with patch("builtins.input", side_effect=entradas), redirect_stdout(salida):
            main()
        texto = salida.getvalue()
        self.assertIn("Primero debe construir", texto)
        self.assertIn("debe ser positivo", texto)
        self.assertIn("[[1.]]", texto)
        self.assertIn("La segunda matriz debe tener las mismas dimensiones", texto)
        self.assertIn("Programa terminado.", texto)

    def test_main_interrupciones(self):
        for interrupcion in [EOFError, KeyboardInterrupt]:
            with self.subTest(interrupcion=interrupcion):
                salida = io.StringIO()
                with patch("builtins.input", side_effect=interrupcion), redirect_stdout(salida):
                    main()
                self.assertIn("Programa terminado.", salida.getvalue())

    def test_programa_completo_desde_terminal(self):
        entradas = [
            "1", "2", "4", "1.5", "-2", "5",  # Vector y valores.
            "6", "1", "1", "2", "0.5", "4",  # Suma: [2, 2].
            "2", "1", "2", "0.5", "4", "3",  # Resta: [1, -6]; volver.
            "5",  # La matriz original sigue siendo [1.5, -2].
            "2", "2", "1", "4", "3", "4", "5",  # Matriz 2D.
            "3", "2", "5", "7",  # Identidad y terminar.
        ]
        programa = Path(__file__).resolve().parents[1] / "matriz.py"
        proceso = subprocess.run(
            [sys.executable, "-W", "error", str(programa)],
            input="\n".join(entradas) + "\n",
            capture_output=True,
            text=True,
            timeout=10,
        )
        self.assertEqual(proceso.returncode, 0, proceso.stderr)
        self.assertEqual(proceso.stderr, "")
        self.assertIn("[[2. 2.]]", proceso.stdout)
        self.assertIn("[[ 1. -6.]]", proceso.stdout)
        self.assertEqual(proceso.stdout.count("[[ 1.5 -2. ]]"), 2)
        self.assertIn("Matriz 2D creada.", proceso.stdout)
        self.assertIn("Matriz identidad creada.", proceso.stdout)
        self.assertIn("Programa terminado.", proceso.stdout)


if __name__ == "__main__":
    unittest.main()
