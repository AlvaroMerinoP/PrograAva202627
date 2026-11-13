
def codigos_unicos(datos):
    resultado = []
    
    for texto in datos:
        codigo = texto.strip().upper()

        if codigo != "" and codigo not in resultado:
            resultado.append(codigo)
    return resultado

datos = [" r1 ", "R2", "r1", " ", "sw1 ", "r2"]
print(codigos_unicos(datos))
print(repr(datos[0]))
print(codigos_unicos([]))
