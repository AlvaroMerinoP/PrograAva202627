def remove_duplicates(numbers: list[int]) -> list[int]:
    """
    Función que elimina los elemento duplicados dentro de una lista
    """
    lista_numeros = []
    for num in numbers:
        if num not in lista_numeros:
            lista_numeros.append(num)
    return lista_numeros

def rotate_left(numbers: list[int], k: int) -> list[int]:
    """
    Devuelve una lista rotada k posiciones hacia la izquierda.
    """
    if len(numbers) == 0:
        return []
    k = k % len(numbers)
    rotated = []

    for index in range(len(numbers)):
        new_index = (index + k) % len(numbers)
        rotated.append(numbers[new_index])

    return rotated

def split_even_odd(numbers: list[int]) -> tuple[list[int], list[int]]:
    """
    Separa los números pares e impares manteniendo su orden.
    """
    even_numbers = []
    odd_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    return even_numbers, odd_numbers


def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    """
    Combina dos listas ordenadas en una nueva lista también ordenada.
    """
    merged = []
    index_a = 0
    index_b = 0

    while index_a < len(a) and index_b < len(b):
        if a[index_a] <= b[index_b]:
            merged.append(a[index_a])
            index_a += 1
        else:
            merged.append(b[index_b])
            index_b += 1

    while index_a < len(a):
        merged.append(a[index_a])
        index_a += 1

    while index_b < len(b):
        merged.append(b[index_b])
        index_b += 1

    return merged


def second_largest(numbers: list[int]) -> int | None:
    """
    Devuelve el segundo valor más grande distinto del máximo.

    Si no existe un segundo valor distinto, devuelve None.
    """
    largest = None
    second = None

    for number in numbers:
        if largest is None or number > largest:
            second = largest
            largest = number
        elif number != largest and (second is None or number > second):
            second = number

    return second


def main() -> None:
    """Prueba todas las funciones con los ejemplos del enunciado."""
    print(remove_duplicates([3, 1, 3, 2, 1]))
    print(rotate_left([1, 2, 3, 4, 5], 2))
    print(rotate_left([1, 2, 3, 4, 5], 7))
    print(rotate_left([1, 2, 3, 4, 5], -1))
    print(split_even_odd([1, 2, 3, 4, 5, 6]))
    print(merge_sorted([1, 4, 9], [2, 3, 10, 11]))
    print(second_largest([4, 9, 2, 9, 7]))
    print(second_largest([5, 5]))

    # Casos adicionales.
    print(remove_duplicates([]))
    print(rotate_left([], 3))
    print(merge_sorted([], [1, 2]))
    print(second_largest([-5, -2, -8, -2]))


if __name__ == "__main__":
    main()
