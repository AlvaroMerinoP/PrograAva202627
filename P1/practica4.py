def shift_char(char: str, shift: int) -> str:
    """
    Desplaza un carácter utilizando el cifrado César.
    Si no es una letra inglesa, lo devuelve sin modificar.
    """
    if "a" <= char <= "z":
        base = ord("a")
        new_position = (ord(char) - base + shift) % 26
        return chr(base + new_position)

    if "A" <= char <= "Z":
        base = ord("A")
        new_position = (ord(char) - base + shift) % 26
        return chr(base + new_position)

    return char

def encrypt(text: str, shift: int) -> str:
    """Cifra un texto utilizando el cifrado César."""
    encrypted_text = ""

    for char in text:
        # Añadir shift_char(char, shift) a encrypted_text.
        ...

    return encrypted_text


