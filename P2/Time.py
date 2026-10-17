"""Práctica 2 de Programación Avanzada: gestión de horas.

Requiere Python 3.10 o posterior. Ejecución: python3 time_management.py.
La clase almacena una hora; no consulta ni actualiza el reloj del sistema.
"""

from __future__ import annotations

import re


class Time:
    """Representa una hora válida en formato AM, PM o 24 HOURS.

    Attributes:
        TIME_FORMATS: Formatos admitidos por la clase.
        time_count: Total de objetos Time creados durante esta ejecución.

    Los datos de cada objeto son privados y se exponen mediante propiedades.
    Cambiar el formato valida la hora existente, pero no realiza conversiones.
    """

    TIME_FORMATS: tuple[str, ...] = ("AM", "PM", "24 HOURS")
    time_count: int = 0

    # Instancia: inicializa los datos de este objeto, recibido como self.
    def __init__(self) -> None:
        """Inicializa una hora válida a 00:00:00 24 HOURS y la cuenta."""
        self.__hours: int = 0
        self.__minutes: int = 0
        self.__seconds: int = 0
        self.__time_format: str = "24 HOURS"
        Time.time_count += 1

    # Instancia: modifica el formato privado del objeto self.
    def __assign_format(self, time_format: str) -> bool:
        """Guarda el formato en mayúsculas si pertenece a TIME_FORMATS.

        Es un auxiliar interno: set_time valida antes la hora completa.
        Un formato no admitido devuelve False sin modificar el objeto.
        """
        if not self.is_valid_format(time_format):
            return False
        self.__time_format = time_format.strip().upper()
        return True

    # Estático: solo necesita la cadena recibida, sin self ni cls.
    @staticmethod
    def __is_24hour_format(time_format: str) -> bool:
        """Indica si la cadena recibida representa el formato de 24 horas."""
        return (
            isinstance(time_format, str)
            and time_format.strip().upper() == "24 HOURS"
        )

    # Estático: comprueba cuatro argumentos sin leer ni modificar un objeto.
    @staticmethod
    def _is_valid_time(
        hours: int, minutes: int, seconds: int, time_format: str
    ) -> bool:
        """Comprueba tipos, formato y rangos de una hora candidata.

        Las horas deben ser 0..23 en 24 HOURS, o 1..12 en AM/PM.
        Minutos y segundos deben ser 0..59. Se rechazan floats y bools.
        """
        if not Time.is_valid_format(time_format):
            return False

        # bool hereda de int: type(...) is int rechaza True y False.
        if any(type(value) is not int for value in (hours, minutes, seconds)):
            return False

        if not (0 <= minutes <= 59 and 0 <= seconds <= 59):
            return False

        if Time.__is_24hour_format(time_format):
            return 0 <= hours <= 23
        return 1 <= hours <= 12

    # Instancia: cambia la hora almacenada en el objeto self.
    def set_time(
        self, hours: int, minutes: int, seconds: int, time_format: str
    ) -> bool:
        """Asigna los cuatro datos solo si todos son válidos.

        Returns:
            True si se asigna la hora; False si se conserva la anterior.
        """
        if not self._is_valid_time(hours, minutes, seconds, time_format):
            return False

        if not self.__assign_format(time_format):
            return False

        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
        return True

    # Instancia: consulta los datos privados del objeto self.
    def get_time(self) -> tuple[int, int, int, str]:
        """Devuelve (horas, minutos, segundos, formato) del objeto."""
        return (
            self.__hours,
            self.__minutes,
            self.__seconds,
            self.__time_format,
        )

    # Clase: crea una instancia usando cls(), sin necesitar un objeto previo.
    @classmethod
    def from_string(cls, time_string: str) -> Time | None:
        """Crea una hora desde 'HH:MM:SS FORMATO', sin distinguir mayúsculas.

        Utiliza re.match, como pide el enunciado. Si falla la sintaxis o
        algún rango, muestra un mensaje y devuelve None sin crear objetos.
        """
        if not isinstance(time_string, str):
            print("Entrada no válida: se esperaba una cadena de texto.")
            return None

        # \Z exige el final de la cadena: no se permite texto sobrante.
        pattern = r"([0-9]{2}):([0-9]{2}):([0-9]{2})\s+(AM|PM|24 HOURS)\Z"
        match = re.match(pattern, time_string.strip(), flags=re.IGNORECASE)
        if match is None:
            print("Cadena no válida. Ejemplo: 02:45:30 PM o 14:30:00 24 HOURS.")
            return None

        hours_text, minutes_text, seconds_text, time_format = match.groups()
        hours = int(hours_text)
        minutes = int(minutes_text)
        seconds = int(seconds_text)

        # Validar antes de cls() evita contar objetos por entradas rechazadas.
        if not cls._is_valid_time(hours, minutes, seconds, time_format):
            print("Hora no válida: revise los rangos de horas, minutos y segundos.")
            return None

        new_time = cls()
        new_time.set_time(hours, minutes, seconds, time_format)
        return new_time

    # Estático: utilidad sin self ni cls; consulta la constante explícitamente.
    @staticmethod
    def is_valid_format(time_format: str) -> bool:
        """Acepta AM, PM o 24 HOURS, con cualquier capitalización."""
        return (
            isinstance(time_format, str)
            and time_format.strip().upper() in Time.TIME_FORMATS
        )

    # Clase: consulta un contador compartido mediante cls, no una hora concreta.
    @classmethod
    def get_time_count(cls) -> int:
        """Devuelve el total de instancias creadas; no los objetos vivos."""
        return cls.time_count

    # Propiedad de instancia: expone en lectura el atributo privado __hours.
    @property
    def hours(self) -> int:
        """Devuelve las horas del objeto."""
        return self.__hours

    # Setter de instancia: valida la nueva hora usando el resto de self.
    @hours.setter
    def hours(self, value: int) -> None:
        """Asigna las horas o lanza ValueError si incumplen el formato actual."""
        if not self.set_time(value, self.minutes, self.seconds, self.time_format):
            raise ValueError("Horas fuera de rango para el formato actual.")

    # Propiedad de instancia: expone el atributo privado __minutes.
    @property
    def minutes(self) -> int:
        """Devuelve los minutos del objeto."""
        return self.__minutes

    # Setter de instancia: modifica los minutos de este objeto tras validarlos.
    @minutes.setter
    def minutes(self, value: int) -> None:
        """Asigna minutos enteros de 0 a 59; si falla, lanza ValueError."""
        if not self.set_time(self.hours, value, self.seconds, self.time_format):
            raise ValueError("Los minutos deben ser enteros entre 0 y 59.")

    # Propiedad de instancia: expone el atributo privado __seconds.
    @property
    def seconds(self) -> int:
        """Devuelve los segundos del objeto."""
        return self.__seconds

    # Setter de instancia: modifica los segundos de este objeto tras validarlos.
    @seconds.setter
    def seconds(self, value: int) -> None:
        """Asigna segundos enteros de 0 a 59; si falla, lanza ValueError."""
        if not self.set_time(self.hours, self.minutes, value, self.time_format):
            raise ValueError("Los segundos deben ser enteros entre 0 y 59.")

    # Propiedad de instancia: expone el formato privado del objeto.
    @property
    def time_format(self) -> str:
        """Devuelve el formato almacenado, siempre en mayúsculas."""
        return self.__time_format

    # Setter de instancia: comprueba la compatibilidad con la hora de self.
    @time_format.setter
    def time_format(self, value: str) -> None:
        """Cambia el formato sin convertir la hora; si falla, lanza ValueError."""
        if not self.set_time(self.hours, self.minutes, self.seconds, value):
            raise ValueError("Formato no válido o incompatible con la hora actual.")


def format_time(time_value: Time) -> str:
    """Devuelve la hora como HH:MM:SS FORMATO; es externa a la clase."""
    hours, minutes, seconds, time_format = time_value.get_time()
    return f"{hours:02d}:{minutes:02d}:{seconds:02d} {time_format}"


def main() -> None:
    """Ejecuta el menú y gestiona entradas incorrectas sin perder la hora."""
    current_time = Time()

    while True:
        print("\n1. Introducir una nueva hora")
        print("2. Visualizar hora")
        print("3. Crear una hora a partir de una cadena")
        print("4. Terminar")

        try:
            option = input("Seleccione una opción: ").strip()

            if option == "1":
                try:
                    hours = int(input("Horas: "))
                    minutes = int(input("Minutos: "))
                    seconds = int(input("Segundos: "))
                except ValueError:
                    print("Entrada no válida: horas, minutos y segundos deben ser enteros.")
                    continue

                time_format = input("Formato (AM, PM o 24 HOURS): ")
                if current_time.set_time(hours, minutes, seconds, time_format):
                    print("Hora guardada:", format_time(current_time))
                else:
                    print("Hora no válida. Se conserva la hora anterior.")
                    print("Horas: 0-23 en 24 HOURS; 1-12 en AM/PM.")
                    print("Minutos y segundos: 0-59. Formatos: AM, PM o 24 HOURS.")

            elif option == "2":
                print("Hora actual:", format_time(current_time))

            elif option == "3":
                time_string = input("Introduzca HH:MM:SS FORMATO: ")
                new_time = Time.from_string(time_string)
                if new_time is not None:
                    current_time = new_time
                    print("Hora creada:", format_time(current_time))
                else:
                    print("Se conserva la hora anterior.")

            elif option == "4":
                print("Programa terminado.")
                break

            else:
                print("Opción no válida. Elija 1, 2, 3 o 4.")

        except (EOFError, KeyboardInterrupt):
            print("\nPrograma terminado.")
            break


if __name__ == "__main__":
    main()
