"""Ejecuta operaciones matemáticas y registra sus resultados."""

from functools import wraps
from typing import Callable


add = lambda *numeros: sum(numeros)
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b

add.__name__ = "add"
subtract.__name__ = "subtract"
multiply.__name__ = "multiply"
divide.__name__ = "divide"


def operation_logger(
    funcion: Callable[..., int | float | None],
) -> Callable[..., int | float | None]:
    """Decora una función para registrar la operación y su resultado."""

    @wraps(funcion)
    def wrapper(
        operacion: Callable[..., int | float],
        *args: int | float,
        **kwargs: int | float,
    ) -> int | float | None:
        """Ejecuta la función original y registra la llamada."""
        nombre = getattr(operacion, "__name__", type(operacion).__name__)
        resultado = funcion(operacion, *args, **kwargs)
        print(
            f"{nombre} | args={args} | kwargs={kwargs} | resultado={resultado}"
        )
        return resultado

    return wrapper


@operation_logger
def math_operation(
    operacion: Callable[..., int | float],
    *args: int | float,
    **kwargs: int | float,
) -> int | float | None:
    """Ejecuta la operación y gestiona la división entre cero."""
    try:
        return operacion(*args, **kwargs)
    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero.")
        return None


if __name__ == "__main__":
    math_operation(add, 5, 3)
    math_operation(subtract, 10, 4)
    math_operation(multiply, 2, 6)
    math_operation(divide, 15, 3)
    math_operation(divide, 10, 0)
    math_operation(add, 1, 2, 3, 4, 5)
    math_operation(divide, 15, b=3)
