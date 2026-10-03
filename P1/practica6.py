def is_prime(n: int) -> bool:
    """Devuelve True si el número recibido es primo y False en otro caso."""
    if n < 2:
        return False

    divisor = 2

    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1

    return True


def prime_list(limit: int) -> list[int]:
    """Devuelve una lista con todos los números primos hasta limit incluido."""
    primes = []

    for number in range(2, limit + 1):
        if is_prime(number):
            primes.append(number)

    return primes


def check_palindrome(primes: list[int]) -> list[int]:
    """Devuelve los números de la lista que se leen igual en ambos sentidos."""
    palindromes = []

    for prime in primes:
        text = str(prime)

        if text == text[::-1]:
            palindromes.append(prime)

    return palindromes


def categorize_prime(prime: int) -> str:
    """Clasifica un primo como pequeño, mediano o grande según su valor."""
    if prime < 10:
        return "pequeño"
    if prime < 100:
        return "mediano"
    return "grande"


def main() -> None:
    """Prueba las funciones de análisis de números primos."""
    limit = 150
    primes = prime_list(limit)

    print(f"Números primos hasta {limit}:")
    print(primes)
    print(f"Primos palíndromos: {check_palindrome(primes)}")

    for prime in (7, 23, 131):
        print(f"{prime} es un primo {categorize_prime(prime)}.")

    for number in (1, 2, 9, 17):
        print(f"¿{number} es primo? {is_prime(number)}")


if __name__ == "__main__":
    main()
