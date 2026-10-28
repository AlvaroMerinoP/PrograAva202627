"""Práctica 4: recepción de una empresa. Ejecución: python3 main.py."""

from typing import List, Tuple

from Time import Time
from cliente import Cliente
from empleado import Empleado
from registro_diario import RegistroDiario
from utils import crear_menu, leer_cadena, leer_int


def leer_entero_no_negativo(mensaje: str) -> int:
    """Lee una edad o antigüedad; lanza ValueError si es negativa."""
    valor = leer_int(mensaje)
    if valor < 0:
        raise ValueError("El valor no puede ser negativo.")
    return valor


def leer_datos_comunes() -> Tuple[str, int, Time]:
    """Solicita nombre, edad y hora; los datos inválidos generan errores."""
    nombre = leer_cadena("Nombre: ")
    edad = leer_entero_no_negativo("Edad: ")
    texto_hora = leer_cadena(
        "Hora de nacimiento (ej. 12:00:00 AM o 14:30:00 24 HOURS): "
    )
    nacio = Time.from_string(texto_hora)
    if nacio is None:
        raise ValueError("No se ha guardado la persona: hora de nacimiento inválida.")
    return nombre, edad, nacio


def introducir_empleado() -> Empleado:
    """Solicita todos los datos y devuelve un empleado válido."""
    nombre, edad, nacio = leer_datos_comunes()
    categoria = leer_cadena("Categoría: ")
    antiguedad = leer_entero_no_negativo("Antigüedad en años: ")
    return Empleado(nombre, edad, nacio, categoria, antiguedad)


def introducir_cliente() -> Cliente:
    """Solicita todos los datos y devuelve un cliente válido."""
    nombre, edad, nacio = leer_datos_comunes()
    dni = leer_cadena("DNI: ")
    return Cliente(nombre, edad, nacio, dni)


def buscar_persona(registro: RegistroDiario) -> None:
    """Busca coincidencias exactas de nombre y edad y muestra sus datos."""
    nombre = leer_cadena("Nombre que quieres buscar: ")
    edad = leer_entero_no_negativo("Edad: ")
    encontrada = False
    for indice, persona in enumerate(registro.personas):
        if persona.nombre == nombre and persona.edad == edad:
            print(f"\nCoincidencia en el índice {indice}:")
            persona.visualizar()
            encontrada = True
    if not encontrada:
        print("No se ha encontrado ninguna persona con ese nombre y edad.")


def visualizar_por_indice(registro: RegistroDiario) -> None:
    """Pide un índice no negativo y comprueba los límites del registro."""
    if len(registro) == 0:
        print("El registro diario está vacío.")
        return
    indice = leer_int(f"Índice de la persona (0 a {len(registro) - 1}): ")
    if not 0 <= indice < len(registro):
        raise IndexError(f"El índice debe estar entre 0 y {len(registro) - 1}.")
    registro[indice].visualizar()


def combinar_registros(registro: RegistroDiario) -> RegistroDiario:
    """Crea otro registro con dos personas solicitadas y devuelve la suma.

    El usuario elige el tipo de cada persona. Si una entrada falla, el
    registro actual se conserva y no se realiza una combinación parcial.
    """
    otro_registro = RegistroDiario()
    for numero in range(1, 3):
        print(f"\nPersona {numero} de 2 del otro registro")
        tipo = crear_menu(["Introducir empleado", "Introducir cliente"])
        if tipo == 1:
            persona = introducir_empleado()
        else:
            persona = introducir_cliente()
        otro_registro.agregar_persona(persona)
    return registro + otro_registro


def main() -> None:
    """Gestiona las ocho opciones, los errores de entrada y la salida."""
    registro = RegistroDiario()
    opciones: List[str] = [
        "Introducir empleado",
        "Introducir cliente",
        "Buscar por nombre (y edad)",
        "Mostrar registro diario",
        "Mostrar empleados",
        "Visualizar persona por índice",
        "Combinar registros diarios",
        "Salir",
    ]
    while True:
        try:
            print("\nRegistro diario de recepción")
            opcion = crear_menu(opciones)
            if opcion == 1:
                registro.agregar_persona(introducir_empleado())
                print("Empleado añadido al registro.")
            elif opcion == 2:
                registro.agregar_persona(introducir_cliente())
                print("Cliente añadido al registro.")
            elif opcion == 3:
                buscar_persona(registro)
            elif opcion == 4:
                registro.visualizar_registro()
            elif opcion == 5:
                registro.visualizar_empleados()
            elif opcion == 6:
                visualizar_por_indice(registro)
            elif opcion == 7:
                registro = combinar_registros(registro)
                print(f"Registros combinados. Total: {len(registro)} persona(s).")
            else:
                print("Programa terminado.")
                return
        except (TypeError, ValueError, IndexError) as error:
            print(f"Error: {error}")
        except (EOFError, KeyboardInterrupt):
            print("\nPrograma terminado.")
            return


if __name__ == "__main__":
    main()
