def minutos_por_aula(reservas):
    totales = {}
    for aula, minutos in reservas:
        if aula in totales:
            totales[aula] += minutos
        else:
            totales[aula] = minutos
    return totales

def aula_mas_ocupada(reservas):
    totales = minutos_por_aula(reservas)

    if not totales:
        return None
    mayor = max(totales.values())
    candidatas = []

    for aula, minutos in totales.items():
        if minutos == mayor:
            candidatas.append(aula)

    return min(candidatas)

reservas = [("A02", 30), ("A01", 45), ("A02", 15), ("A03", 20)]
print(minutos_por_aula(reservas))
print(aula_mas_ocupada(reservas))
print(aula_mas_ocupada([]))


