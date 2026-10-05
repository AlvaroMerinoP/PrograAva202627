def sum_numbers(numbers: list[int]) -> int:
    """Devuelve la suma de todos los números de la lista."""
    total = 0
    for number in numbers:
        total += number
    return total


def sum_positive_negative(numbers: list[int]) -> tuple[int, int]:
    """Devuelve las sumas de positivos y negativos, en ese orden."""
    positive_sum = 0
    negative_sum = 0
    for number in numbers:
        if number > 0:
            positive_sum += number
        elif number < 0:
            negative_sum += number
    return positive_sum, negative_sum


def find_max_min(numbers: list[int]) -> tuple[int, int] | None:
    """Devuelve el máximo y el mínimo, o None si la lista está vacía."""
    if not numbers:
        return None
    maximum = numbers[0]
    minimum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number
    return maximum, minimum


def all_unique(numbers: list[int]) -> bool:
    """Comprueba si todos los números son distintos."""
    seen = []
    for number in numbers:
        if number in seen:
            return False
        seen.append(number)
    return True


def compare_positive_negative(numbers: list[int]) -> str:
    """Compara la cantidad de positivos y negativos; el cero no cuenta."""
    positives = 0
    negatives = 0
    for number in numbers:
        if number > 0:
            positives += 1
        elif number < 0:
            negatives += 1
    if positives == negatives:
        return "Hay la misma cantidad de números positivos y negativos."
    return "Hay más números positivos." if positives > negatives else "Hay más números negativos."


def main() -> None:
    """Prueba las funciones y permite utilizarlas desde un menú repetitivo."""
    example = [3, -2, 0, 5, -2]
    print(f"Ejemplo: {example}")
    print(f"Suma: {sum_numbers(example)}")
    print(f"Sumas de positivos y negativos: {sum_positive_negative(example)}")
    print(f"Máximo y mínimo: {find_max_min(example)}")
    print(f"¿Todos únicos? {all_unique(example)}")
    print(compare_positive_negative(example))
    print(f"Lista vacía: suma = {sum_numbers([])}, máximo y mínimo = {find_max_min([])}")
    print(f"¿Todos únicos en [1, 2, 3]? {all_unique([1, 2, 3])}")
    print(compare_positive_negative([0, 1, 2, -3]))

    while True:
        text = input("Introduce enteros separados por espacios (vacío para lista vacía): ")
        try:
            numbers = [int(word) for word in text.split()]
            break
        except ValueError:
            print("Entrada no válida. Introduce solo números enteros.")

    while True:
        print("\n1. Sumar todos los números")
        print("2. Sumar positivos y negativos por separado")
        print("3. Encontrar máximo y mínimo")
        print("4. Comprobar si todos son únicos")
        print("5. Comparar la cantidad de positivos y negativos")
        print("0. Salir")
        option = input("Elige una opción: ").strip()

        if option == "0":
            break
        elif option == "1":
            print(f"Suma: {sum_numbers(numbers)}")
        elif option == "2":
            positive_sum, negative_sum = sum_positive_negative(numbers)
            print(f"Suma de positivos: {positive_sum}; suma de negativos: {negative_sum}")
        elif option == "3":
            extremes = find_max_min(numbers)
            if extremes is None:
                print("La lista está vacía: no tiene máximo ni mínimo.")
            else:
                maximum, minimum = extremes
                print(f"Máximo: {maximum}; mínimo: {minimum}")
        elif option == "4":
            print(f"¿Todos los números son únicos? {all_unique(numbers)}")
        elif option == "5":
            print(compare_positive_negative(numbers))
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
