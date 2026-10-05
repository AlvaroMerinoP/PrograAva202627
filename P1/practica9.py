def format_monomial(coef: float, exp: int) -> str:
    """Representa un monomio con signo explícito, omitiéndolo si vale cero."""
    if coef == 0:
        return ""

    sign = "+" if coef > 0 else "-"
    magnitude = abs(coef)
    if exp == 0:
        return sign + str(magnitude)

    coefficient = "" if magnitude == 1 else str(magnitude)
    variable = "x" if exp == 1 else f"x**{exp}"
    return sign + coefficient + variable


def format_polynomial(coefs: list[float]) -> str:
    """Representa el polinomio de mayor a menor exponente sin términos nulos."""
    polynomial = ""
    for exp in range(len(coefs) - 1, -1, -1):
        monomial = format_monomial(coefs[exp], exp)
        if not monomial:
            continue
        if not polynomial:
            polynomial = monomial[1:] if monomial[0] == "+" else monomial
        else:
            polynomial += f" {monomial[0]} {monomial[1:]}"
    return polynomial if polynomial else "0"


def evaluate(coefs: list[float], x: float) -> float:
    """Evalúa un polinomio cuyos coeficientes están en orden de exponente."""
    value = 0.0
    for exp in range(len(coefs)):
        value += coefs[exp] * x ** exp
    return value


def derivative(coefs: list[float]) -> list[float]:
    """Devuelve los coeficientes de la derivada; una constante produce []."""
    result = []
    for exp in range(1, len(coefs)):
        result.append(coefs[exp] * exp)
    return result


def main() -> None:
    """Prueba las funciones con los ejemplos del enunciado y casos adicionales."""
    for coef, exp in ((2.0, 3), (1.0, 2), (-1.0, 1), (4.0, 0), (0.0, 5)):
        print(f"format_monomial({coef}, {exp}): {format_monomial(coef, exp)!r}")

    for coefs in ([4.0, 1.0, 0.0, 2.0], [0.0, -1.0, 3.0],
                  [-2.5, 0.0, -1.0], [0.0, 0.0], [], [5.0], [0.0, 1.0]):
        print(f"Polinomio: {format_polynomial(coefs)}")
        print(f"Valor en x = 2: {evaluate(coefs, 2)}")
        derived = derivative(coefs)
        print(f"Coeficientes de la derivada: {derived}")
        print(f"Derivada: {format_polynomial(derived)}")


if __name__ == "__main__":
    main()
