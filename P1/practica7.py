def remove_duplicates(numbers):
    lista_numeros= []
    for num in numbers:
        if num not in lista_numeros:
            lista_numeros.append(num)
    return lista_numeros

def rotate_left(numbers, k):
