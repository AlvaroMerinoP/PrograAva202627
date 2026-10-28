"""Pruebas de las opciones del menú con entradas simuladas."""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from cliente import Cliente
from empleado import Empleado
from main import buscar_persona, combinar_registros, main, visualizar_por_indice
from registro_diario import RegistroDiario


class MainTests(unittest.TestCase):
    """Ejercita los flujos completos y la recuperación ante errores."""

    def test_recorrido_de_las_ocho_opciones(self) -> None:
        entradas = [
            "1", "Ana", "30", "12:00:00 AM", "Técnico", "5",
            "2", "Luis", "42", "06:30:00 PM", "12345678Z",
            "3", "Ana", "30",
            "3", "Luis", "42",
            "4", "5", "6", "1",
            "7",
            "1", "Eva", "28", "14:30:00 24 HOURS", "Administrativo", "3",
            "2", "Pablo", "45", "08:10:00 AM", "87654321X",
            "4", "8",
        ]
        salida = io.StringIO()
        with patch("builtins.input", side_effect=entradas) as entrada, redirect_stdout(salida):
            main()
        texto = salida.getvalue()
        self.assertEqual(entrada.call_count, len(entradas))
        self.assertNotIn("Error:", texto)
        for dato in (
            "Empleado añadido", "Cliente añadido", "Coincidencia en el índice 0",
            "Coincidencia en el índice 1", "Total: 4 persona(s)", "Persona [3]",
            "Nombre: Pablo", "14:30:00 24 HOURS", "Programa terminado",
        ):
            self.assertIn(dato, texto)

    def test_busqueda_muestra_todas_las_coincidencias_y_su_tipo(self) -> None:
        registro = RegistroDiario()
        registro.agregar_persona(Empleado("Ana", 30))
        registro.agregar_persona(Cliente("Ana", 30))
        registro.agregar_persona(Cliente("Ana", 31))
        salida = io.StringIO()
        with patch("builtins.input", side_effect=["Ana", "30"]), redirect_stdout(salida):
            buscar_persona(registro)
        texto = salida.getvalue()
        self.assertEqual(texto.count("Coincidencia"), 2)
        self.assertIn("Tipo: Empleado", texto)
        self.assertIn("Tipo: Cliente", texto)
        self.assertNotIn("Edad: 31", texto)

    def test_busqueda_sin_coincidencias(self) -> None:
        registro = RegistroDiario()
        registro.agregar_persona(Cliente("Ana", 30))
        for entradas in (["Ana", "31"], ["Luis", "30"]):
            salida = io.StringIO()
            with patch("builtins.input", side_effect=entradas), redirect_stdout(salida):
                buscar_persona(registro)
            self.assertIn("No se ha encontrado", salida.getvalue())

    def test_indices_invalidos_en_el_menu(self) -> None:
        registro = RegistroDiario()
        registro.agregar_persona(Cliente("Ana"))
        for indice in ("-1", "1"):
            with self.subTest(indice=indice), patch("builtins.input", return_value=indice):
                with self.assertRaises(IndexError):
                    visualizar_por_indice(registro)

    def test_indice_sobre_registro_vacio(self) -> None:
        with patch("builtins.input") as entrada, redirect_stdout(io.StringIO()):
            visualizar_por_indice(RegistroDiario())
        entrada.assert_not_called()

    def test_combinar_exactamente_dos_personas_sin_modificar_original(self) -> None:
        registro = RegistroDiario()
        empleado = Empleado("Ana", 30)
        registro.agregar_persona(empleado)
        entradas = [
            "2", "Luis", "42", "06:30:00 PM", "12345678Z",
            "1", "Eva", "28", "14:30:00 24 HOURS", "Técnico", "3",
        ]
        with patch("builtins.input", side_effect=entradas), redirect_stdout(io.StringIO()):
            resultado = combinar_registros(registro)
        self.assertEqual(len(registro), 1)
        self.assertEqual(len(resultado), 3)
        self.assertIs(resultado[0], empleado)
        self.assertIsInstance(resultado[1], Cliente)
        self.assertIsInstance(resultado[2], Empleado)

    def test_combinacion_fallida_conserva_registro(self) -> None:
        registro = RegistroDiario()
        registro.agregar_persona(Empleado("Ana"))
        entradas = ["2", "Luis", "42", "06:30:00 PM", "12345678Z", "1", "Eva", "-1"]
        with patch("builtins.input", side_effect=entradas), redirect_stdout(io.StringIO()):
            with self.assertRaises(ValueError):
                combinar_registros(registro)
        self.assertEqual(len(registro), 1)
        self.assertEqual(registro[0].nombre, "Ana")

    def test_errores_de_entrada_y_altas_incompletas(self) -> None:
        entradas = [
            "hola", "0", "9", "1", "   ", "2", "Luis", "abc",
            "1", "Ana", "-1",
            "2", "Luis", "42", "25:00:00 24 HOURS",
            "4", "8",
        ]
        salida = io.StringIO()
        with patch("builtins.input", side_effect=entradas), redirect_stdout(salida):
            main()
        self.assertIn("Error:", salida.getvalue())
        self.assertIn("El registro diario está vacío", salida.getvalue())
        self.assertIn("Programa terminado", salida.getvalue())

    def test_fin_de_entrada_e_interrupcion(self) -> None:
        for error in (EOFError, KeyboardInterrupt):
            salida = io.StringIO()
            with patch("builtins.input", side_effect=error), redirect_stdout(salida):
                main()
            self.assertIn("Programa terminado", salida.getvalue())


if __name__ == "__main__":
    unittest.main()
