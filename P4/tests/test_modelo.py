"""Pruebas de herencia, encapsulación y operaciones del registro."""

import io
import unittest
from contextlib import redirect_stdout

from Time import Time
from cliente import Cliente
from empleado import Empleado
from ficha import Ficha
from registro_diario import RegistroDiario


class ModeloTests(unittest.TestCase):
    """Verifica los contratos de las clases del enunciado."""

    def test_ficha_por_defecto_y_horas_independientes(self) -> None:
        primera, segunda = Ficha(), Ficha()
        self.assertEqual((primera.nombre, primera.edad), ("", 0))
        self.assertEqual(primera.nacio.get_time(), (12, 0, 0, "AM"))
        self.assertIsNot(primera.nacio, segunda.nacio)
        primera.nacio.set_time(5, 30, 0, "PM")
        self.assertEqual(segunda.nacio.get_time(), (12, 0, 0, "AM"))

    def test_herencia_y_propiedades(self) -> None:
        hora = Time()
        hora.set_time(14, 30, 15, "24 HOURS")
        empleado = Empleado(" Ana ", 30, hora, "Técnico", 4)
        cliente = Cliente("Luis", 45, hora, "12345678Z")
        self.assertIsInstance(empleado, Ficha)
        self.assertIsInstance(cliente, Ficha)
        self.assertEqual(empleado.nombre, "Ana")
        self.assertIs(empleado.nacio, hora)
        empleado.nombre, empleado.edad = "Eva", 31
        empleado.categoria, empleado.antiguedad = "Administrativo", 5
        cliente.dni = "87654321X"
        self.assertEqual((empleado.nombre, empleado.edad), ("Eva", 31))
        self.assertEqual((empleado.categoria, empleado.antiguedad), ("Administrativo", 5))
        self.assertEqual(cliente.dni, "87654321X")
        self.assertNotIn("nombre", vars(empleado))
        self.assertNotIn("categoria", vars(empleado))

    def test_propiedades_rechazan_tipos_y_conservan_valores(self) -> None:
        empleado = Empleado("Ana", 30, categoria="Técnico", antiguedad=4)
        cliente = Cliente("Luis", 45, dni="12345678Z")
        casos = [
            (empleado, "nombre", 5),
            (empleado, "edad", 2.5),
            (empleado, "edad", True),
            (empleado, "nacio", "12:00:00 AM"),
            (empleado, "categoria", None),
            (empleado, "antiguedad", "4"),
            (empleado, "antiguedad", False),
            (cliente, "dni", 12345678),
        ]
        for persona, atributo, valor in casos:
            with self.subTest(atributo=atributo, valor=valor):
                anterior = getattr(persona, atributo)
                with self.assertRaises(TypeError):
                    setattr(persona, atributo, valor)
                self.assertEqual(getattr(persona, atributo), anterior)

    def test_rechaza_edades_y_antiguedades_negativas(self) -> None:
        with self.assertRaises(ValueError):
            Ficha(edad=-1)
        with self.assertRaises(ValueError):
            Empleado(antiguedad=-1)

    def test_clientes_iguales_por_nombre_y_edad(self) -> None:
        primero = Cliente("Ana", 30, dni="11111111A")
        segundo = Cliente("Ana", 30, dni="22222222B")
        segundo.nacio.set_time(6, 15, 0, "PM")
        self.assertEqual(primero, segundo)
        self.assertNotEqual(primero, Cliente("Ana", 31))
        self.assertNotEqual(primero, Cliente("Luis", 30))
        self.assertNotEqual(primero, Empleado("Ana", 30))
        self.assertNotEqual(primero, None)
        self.assertIs(primero.__eq__(object()), NotImplemented)

    def test_registro_solo_admite_empleados_y_clientes(self) -> None:
        registro = RegistroDiario()
        for persona in (Ficha(), "Ana", None, 5):
            with self.subTest(persona=persona), self.assertRaises(TypeError):
                registro.agregar_persona(persona)
        self.assertEqual(len(registro), 0)
        empleado, cliente = Empleado(), Cliente()
        registro.agregar_persona(empleado)
        registro.agregar_persona(cliente)
        self.assertEqual(len(registro), 2)
        self.assertIs(registro[0], empleado)
        self.assertIs(registro[1], cliente)

    def test_la_lista_publica_no_permite_eludir_validacion(self) -> None:
        registro = RegistroDiario()
        empleado = Empleado("Ana")
        registro.agregar_persona(empleado)
        copia = registro.personas
        copia.clear()
        copia.append(Ficha())
        self.assertEqual(len(registro), 1)
        self.assertIs(registro[0], empleado)

    def test_indices_y_limites(self) -> None:
        registro = RegistroDiario()
        with self.assertRaises(IndexError):
            registro[0]
        cliente = Cliente()
        registro.agregar_persona(cliente)
        self.assertIs(registro[-1], cliente)
        for indice in (1, -2):
            with self.subTest(indice=indice), self.assertRaises(IndexError):
                registro[indice]
        for indice in ("0", 0.0, True, slice(0, 1)):
            with self.subTest(indice=indice), self.assertRaises(TypeError):
                registro[indice]

    def test_suma_conserva_originales_orden_y_duplicados(self) -> None:
        primero, segundo = RegistroDiario(), RegistroDiario()
        empleado, cliente = Empleado("Ana"), Cliente("Luis")
        primero.agregar_persona(empleado)
        segundo.agregar_persona(cliente)
        segundo.agregar_persona(empleado)
        combinado = primero + segundo
        self.assertEqual((len(primero), len(segundo), len(combinado)), (1, 2, 3))
        self.assertIs(combinado[0], empleado)
        self.assertIs(combinado[1], cliente)
        self.assertIs(combinado[2], empleado)
        combinado.agregar_persona(Cliente("Eva"))
        self.assertEqual((len(primero), len(segundo)), (1, 2))
        self.assertEqual(len(primero + RegistroDiario()), 1)
        self.assertEqual(len(RegistroDiario() + segundo), 2)
        self.assertEqual(len(RegistroDiario() + RegistroDiario()), 0)
        self.assertEqual(len(primero + primero), 2)
        with self.assertRaises(TypeError):
            primero + 5

    def test_visualizacion_polimorfica_y_filtro(self) -> None:
        registro = RegistroDiario()
        registro.agregar_persona(Empleado("Ana", 30, categoria="Técnico", antiguedad=4))
        registro.agregar_persona(Cliente("Luis", 45, dni="12345678Z"))
        salida = io.StringIO()
        with redirect_stdout(salida):
            registro.visualizar_registro()
        texto = salida.getvalue()
        for dato in ("Tipo: Empleado", "Tipo: Cliente", "Técnico", "12345678Z", "12:00:00 AM"):
            self.assertIn(dato, texto)
        salida = io.StringIO()
        with redirect_stdout(salida):
            registro.visualizar_empleados()
        self.assertIn("Ana", salida.getvalue())
        self.assertNotIn("Luis", salida.getvalue())
        self.assertTrue(RegistroDiario.es_empleado(registro[0]))
        self.assertFalse(RegistroDiario.es_empleado(registro[1]))
        self.assertFalse(RegistroDiario.es_empleado(None))

    def test_visualizacion_vacia(self) -> None:
        registro = RegistroDiario()
        salida = io.StringIO()
        with redirect_stdout(salida):
            registro.visualizar_registro()
            registro.visualizar_empleados()
        self.assertIn("vacío", salida.getvalue())
        self.assertIn("No hay empleados", salida.getvalue())


if __name__ == "__main__":
    unittest.main()
