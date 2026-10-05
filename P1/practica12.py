def is_anagram(word1: str, word2: str) -> bool:
    """Comprueba si dos cadenas son anagramas ignorando mayúsculas y espacios."""
    normalized1 = word1.lower().replace(" ", "")
    normalized2 = word2.lower().replace(" ", "")

    # Al ordenar las letras, los anagramas producen la misma lista.
    return sorted(normalized1) == sorted(normalized2)


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Agrupa los anagramas conservando el orden de primera aparición."""
    groups = []

    for word in words:
        for group in groups:
            # Basta comparar con la primera palabra de cada grupo.
            if is_anagram(word, group[0]):
                group.append(word)
                break
        else:
            # Si no se ha ejecutado break, no existe un grupo adecuado.
            groups.append([word])

    return groups


def largest_group(groups: list[list[str]]) -> list[str]:
    """Devuelve el primer grupo más numeroso, o [] si no hay grupos."""
    largest = []

    for group in groups:
        # Usamos > para conservar el primer grupo en caso de empate.
        if len(group) > len(largest):
            largest = group

    return largest


def find_anagrams(word: str, words: list[str]) -> list[str]:
    """Busca anagramas en la lista excluyendo la propia palabra."""
    anagrams = []

    for candidate in words:
        if candidate != word and is_anagram(word, candidate):
            anagrams.append(candidate)

    return anagrams


def main() -> None:
    """Prueba los ejemplos del enunciado y algunos casos adicionales."""
    words = ["roma", "amor", "pelo", "mora", "casa", "lope", "ramo"]

    print(is_anagram("Roma", "amor"))
    print(is_anagram("casa", "caso"))
    print(is_anagram("dormitory", "dirty room"))

    groups = group_anagrams(words)
    print(groups)
    print(largest_group(groups))
    print(find_anagrams("amor", words))
    print(find_anagrams("sol", words))

    # Casos adicionales: empate, letras repetidas y listas vacías.
    print(group_anagrams(["sol", "los", "sal", "las", "pan"]))
    print(largest_group([["sol", "los"], ["sal", "las"]]))
    print(is_anagram("aab", "abb"))
    print(group_anagrams([]))
    print(largest_group([]))
    print(find_anagrams("sol", []))


if __name__ == "__main__":
    main()
