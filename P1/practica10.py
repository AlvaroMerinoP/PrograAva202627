def starts_with_letter(words: list[str], letter: str) -> None:
    """Imprime las cadenas que empiezan por la letra indicada."""
    for word in words:
        if word.startswith(letter):
            print(word)


def count_substring(words: list[str], substring: str) -> int:
    """Cuenta cuántas cadenas contienen la subcadena."""
    count = 0

    for word in words:
        if substring in word:
            count += 1

    return count


def longest_shortest(words: list[str]) -> tuple[str, str] | None:
    """Devuelve la cadena más larga y la más corta, o None si no hay cadenas."""
    if not words:
        return None

    longest = words[0]
    shortest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

        if len(word) < len(shortest):
            shortest = word

    return longest, shortest


def same_object(words: list[str], first: int, second: int) -> bool:
    """Comprueba si dos posiciones contienen el mismo objeto."""
    return words[first] is words[second]


def check_long_strings(words: list[str]) -> None:
    """Comprueba si alguna cadena tiene más de diez caracteres."""
    for word in words:
        if len(word) > 10:
            print(f"Hay una cadena con más de 10 caracteres: {word}")
            break
    else:
        print("Ninguna cadena tiene más de 10 caracteres.")


def main() -> None:
    """Lee las cadenas y muestra un menú hasta que el usuario salga."""
    # Usamos ; para poder introducir cadenas que contengan espacios.
    text = input("Introduce cadenas separadas por ;: ")
    words = [word.strip() for word in text.split(";")] if text else []

    while True:
        print("\nCadenas:", words)
        print("1. Mostrar cadenas que empiezan por una letra")
        print("2. Contar cadenas que contienen una subcadena")
        print("3. Mostrar la más larga y la más corta")
        print("4. Comprobar si dos posiciones contienen el mismo objeto")
        print("5. Comprobar si hay cadenas de más de 10 caracteres")
        print("0. Salir")

        option = input("Opción: ").strip()

        if option == "0":
            break

        elif option == "1":
            letter = input("Letra: ")
            if len(letter) == 1 and letter.isalpha():
                starts_with_letter(words, letter)
            else:
                print("Introduce una sola letra.")

        elif option == "2":
            substring = input("Subcadena: ")
            print("Cantidad:", count_substring(words, substring))

        elif option == "3":
            result = longest_shortest(words)

            if result is None:
                print("La lista está vacía.")
            else:
                longest, shortest = result
                print("Más larga:", longest)
                print("Más corta:", shortest)

        elif option == "4":
            # Mostramos los índices para que el usuario pueda elegir.
            for index, word in enumerate(words):
                print(index, word)

            try:
                first = int(input("Primera posición: "))
                second = int(input("Segunda posición: "))

                if 0 <= first < len(words) and 0 <= second < len(words):
                    print("¿Mismo objeto?", same_object(words, first, second))
                else:
                    print("Posición fuera de la lista.")

            except ValueError:
                print("Las posiciones deben ser números enteros.")

        elif option == "5":
            check_long_strings(words)

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
