"""Pruebas de las entradas y de los errores solicitados en utils.py."""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from utils import crear_menu, leer_cadena, leer_float, leer_int


class UtilsTests(unittest.TestCase):
    """Verifica conversiones, textos vacíos, tipos y límites del menú."""

    def test_enteros_validos(self) -> None:
        for entrada, esperado in (("0", 0), (" -4 ", -4), ("+12", 12)):
            with self.subTest(entrada=entrada), patch("builtins.input", return_value=entrada):
                self.assertEqual(leer_int(), esperado)

    def test_enteros_invalidos_generan_errores(self) -> None:
        for entrada in ("", "hola", "2.5", "3,5"):
            with self.subTest(entrada=entrada), patch("builtins.input", return_value=entrada):
                with self.assertRaises(ValueError):
                    leer_int()

    def test_decimales_validos(self) -> None:
        for entrada, esperado in (("2,5", 2.5), (" -4.25 ", -4.25), ("1e2", 100.0)):
            with self.subTest(entrada=entrada), patch("builtins.input", return_value=entrada):
                self.assertEqual(leer_float(), esperado)

    def test_decimales_invalidos_o_no_finitos(self) -> None:
        for entrada in ("", "texto", "nan", "inf", "-inf", "1e400"):
            with self.subTest(entrada=entrada), patch("builtins.input", return_value=entrada):
                with self.assertRaises(ValueError):
                    leer_float()

    def test_cadena_y_espacios_exteriores(self) -> None:
        with patch("builtins.input", return_value="  Ana López  "):
            self.assertEqual(leer_cadena("Nombre: "), "Ana López")
        for entrada in ("", "   ", "\t"):
            with self.subTest(entrada=entrada), patch("builtins.input", return_value=entrada):
                with self.assertRaises(ValueError):
                    leer_cadena("Nombre: ")

    def test_mensajes_de_tipo_incorrecto(self) -> None:
        for funcion in (leer_int, leer_float, leer_cadena):
            with self.subTest(funcion=funcion.__name__), self.assertRaises(TypeError):
                funcion(123)

    def test_menu_numerado_y_seleccion(self) -> None:
        salida = io.StringIO()
        with patch("builtins.input", return_value="2"), redirect_stdout(salida):
            self.assertEqual(crear_menu(["Primera", "Segunda"]), 2)
        self.assertIn("1. Primera", salida.getvalue())
        self.assertIn("2. Segunda", salida.getvalue())

    def test_menu_rechaza_argumentos_incorrectos(self) -> None:
        for opciones in ("Salir", ("Salir",), None, ["Salir", 2]):
            with self.subTest(opciones=opciones), self.assertRaises(TypeError):
                crear_menu(opciones)
        for opciones in ([], [""], ["   "]):
            with self.subTest(opciones=opciones), self.assertRaises(ValueError):
                crear_menu(opciones)

    def test_menu_rechaza_selecciones_invalidas(self) -> None:
        for entrada in ("0", "3", "-1", "hola", "1.5"):
            with self.subTest(entrada=entrada):
                with patch("builtins.input", return_value=entrada), redirect_stdout(io.StringIO()):
                    with self.assertRaises(ValueError):
                        crear_menu(["Primera", "Segunda"])


if __name__ == "__main__":
    unittest.main()
