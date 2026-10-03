def normalize(text: str) -> str:
    """Normaliza un texto eliminando tildes y caracteres no alfanuméricos."""
    text = text.lower()

    for original, replacement in (
        ("á", "a"), ("é", "e"), ("í", "i"),
        ("ó", "o"), ("ú", "u"), ("ü", "u")
    ):
        text = text.replace(original, replacement)

    result = ""
    for char in text:
        if char.isalnum():
            result += char

    return result


def is_palindrome(text: str) -> bool:
    """Devuelve True si el texto es un palíndromo después de normalizarlo."""
    normalized = normalize(text)
    return normalized == normalized[::-1]


def find_palindromes(sentences: list[str]) -> list[str]:
    """Devuelve las frases de la lista que son palíndromos."""
    result = []

    for sentence in sentences:
        if is_palindrome(sentence):
            result.append(sentence)

    return result


def palindrome_words(text: str) -> list[str]:
    """Devuelve las palabras palíndromas que tienen al menos tres letras."""
    result = []

    for word in text.split():
        if len(word) >= 3 and is_palindrome(word):
            result.append(word)

    return result


def main() -> None:
    """Prueba las funciones de detección de palíndromos."""
    sentences = [
        "Anita lava la tina",
        "Dábale arroz a la zorra el abad",
        "Esto no es un palíndromo",
        "¿Acaso hubo búhos acá?",
        "Reconocer",
    ]

    print(normalize("¿Acaso hubo búhos acá?"))
    print(is_palindrome("Anita lava la tina"))

    for phrase in find_palindromes(sentences):
        print(phrase)

    print(palindrome_words("Ana vio un oso en el ojo de Anita"))


if __name__ == "__main__":
    main()
