def normalize(text: str) -> str:
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
    normalized = normalize(text)
    return normalized == normalized[::-1]


def find_palindromes(sentences: list[str]) -> list[str]:
    result = []

    for sentence in sentences:
        if is_palindrome(sentence):
            result.append(sentence)

    return result


def palindrome_words(text: str) -> list[str]:
    result = []

    for word in text.split():
        if len(word) >= 3 and is_palindrome(word):
            result.append(word)

    return result


def main() -> None:
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
