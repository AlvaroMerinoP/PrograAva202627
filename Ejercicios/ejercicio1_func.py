from math import sqrt


def calcular_raices(a, b, c):
    """Devuelve dos raíces reales, una raíz real o un mensaje."""
    if a == 0:
        return "No es una ecuación de segundo grado: a debe ser distinto de 0."

    discriminante = b ** 2 - 4 * a * c

    if discriminante < 0:
        return "La ecuación no tiene raíces reales."
    elif discriminante == 0:
        return -b / (2 * a)
    else:
        x1 = (-b + sqrt(discriminante)) / (2 * a)
        x2 = (-b - sqrt(discriminante)) / (2 * a)
        return x1, x2


def main():
    try:
        a = float(input("Introduce el coeficiente a: "))
        b = float(input("Introduce el coeficiente b: "))
        c = float(input("Introduce el coeficiente c: "))
    except ValueError:
        print("Los coeficientes deben ser números.")
        return

    resultado = calcular_raices(a, b, c)

    if isinstance(resultado, tuple):
        x1, x2 = resultado
        print(f"La ecuación tiene dos raíces reales: x1 = {x1}, x2 = {x2}.")
    elif isinstance(resultado, float):
        print(f"La ecuación tiene una única raíz real: x = {resultado}.")
    elif isinstance(resultado, str):
        print(resultado)


if __name__ == "__main__":
    main()
