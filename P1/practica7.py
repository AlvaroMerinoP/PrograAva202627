def remove_duplicates(numbers):
    """
    Función que elimina los elemento duplicados dentro de una lista
    """
    lista_numeros= []
    for num in numbers:
        if num not in lista_numeros:
            lista_numeros.append(num)
    return lista_numeros

def rotate_left(numbers, k):
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

def split_even_odd(numbers):
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
