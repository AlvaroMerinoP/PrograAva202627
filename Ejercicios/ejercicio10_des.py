class Equipo:

    def __init__(self, codigo, disponible = True):
        self.codigo = codigo
        self.disponible = disponible

class Laboratorio:
    def __init__(self):
        self.equipos = {}

    def registrar(self, equipo):
        if equipo.codigo in self.equipos:
            return False

        self.equipos[equipo.codigo] = equipo
        return True  
    
    def disponibles(self):
        codigos = []

        for codigo, equipo in self.equipos.items():
            if equipo.disponible:
                codigos.append(codigo)

        return sorted(codigos)

lab = Laboratorio()
print(lab.registrar(Equipo("PC3")))
lab.registrar(Equipo("PC1", False))
lab.registrar(Equipo("PC2"))
print(lab.registrar(Equipo("PC2", False)))
print(lab.disponibles())
print(Laboratorio().disponibles())


