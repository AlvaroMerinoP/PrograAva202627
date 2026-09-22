def is_integer(text):
    """
    Comprueba si una cadena representa un número entero.

    Args:
        text: cadena que se quiere comprobar.

    Returns: 
        True si representa un entero, False en caso contrario.
    """
    try:
        int(text)
        return True
    except ValueError:
        return False

def seconds_to_dhms(total_seconds):
    """
    Convierte una cantidad de seundos en días, horas, minutos y segundos.

    Args:
        total_seconds: Cantidad toal de segundos

    Returns:
        Una tupla con (días, horas, minutos, segundos).
    """
    dias = total_seconds // 86400
    resto = total_seconds % 86400

    horas = resto // 3600
    resto = resto % 3600

    minutos = resto // 60
    segundos = resto % 60

    return dias, horas, minutos, segundos

def main():
    """
    Solicita al usuario una cantidad de segundos válida 
    y muestra su equivalencia en días, horas, minutos y segundos.
    """
    while True:
        texto = input("Introduzca los segundos: ")

        if is_integer(texto):
            total_seconds = int(texto)

            if total_seconds >= 0:
                break

            print("Entrada no válida. Introduzca un entero no negativo.")

    dias, horas, minutos, segundos = seconds_to_dhms(total_seconds)
    print(
            f"{total_seconds} segundos son "
            f"{dias} d, {horas} h, {minutos} min y {segundos} s."
    )

if __name__ == "__main__":
    main()

