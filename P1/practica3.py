def process_text(
    text: str = "This is a default text with Python and amazing words.",
    words: list[str] = ["Python", "amazing"]
) -> tuple[str, int]:
    """
    Procesa una cadena de texto sustituyendo determinadas palabras
    por asteriscos.

    Args:
        text: Cadena de texto que se quiere procesar.
        words: Lista de palabras que se quieren reemplazar.

    Returns:
        Una tupla formada por el texto procesado y el número
        de palabras reemplazadas.
    """

    text = text.lower().strip()
    replaced = 0
  
    for word in words:
        word = word.lower()

        replaced += text.count(word)
        text = text.replace(word, "*" * len(word))

    return text, replaced

def main() -> None:
    """Prueba process_text con sus valores predeterminados."""
    processed_text, replaced = process_text()

    print(f'Processed text: "{processed_text}"')
    print(f"Palabras reemplazadas: {replaced}")

if __name__ == "__main__":
    main()
