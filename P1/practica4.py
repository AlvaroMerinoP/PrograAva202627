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
        encrypted_text += shift_char(char,shift)
    return encrypted_text

        
def decrypt(text:str, shift:int) -> str:
    return encrypt(text, -shift)

def brute_force(cipher_text:str) -> list[str]:
    possibilities = []
    for shift in range(26):
        possibilities.append(decrypt(cipher_text, shift))
    return possibilities
def main() -> None:

    print(shift_char("x", 3))               # a
    print(encrypt("Hola, Mundo!", 3))       # Krod, Pxqgr!
    print(decrypt("Krod, Pxqgr!", 3))      # Hola, Mundo!
    print(brute_force("Krod, Pxqgr!")[3]) # Hola, Mundo!




if __name__ == "__main__":
    main()


    


