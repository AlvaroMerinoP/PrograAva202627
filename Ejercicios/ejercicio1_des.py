class Bicicleta:
    _count = 0
    def __init__(self, marca = "Sin marca", anio = 2020):
        self.marca = marca
        self.anio = anio
        Bicicleta._count += 1

    @classmethod
    def total_creadas(cls):
        return cls._count
    
    @staticmethod
    def clasificar(anio, umbral):
        if anio >= umbral:
            return "nueva"
        else:
            return "usada"
        




b1 = Bicicleta("Orbea", 2024)
b2 = Bicicleta()

print(b2.marca, b2.anio)              # Sin marca 2020
print(Bicicleta.total_creadas())       # 2
print(Bicicleta.clasificar(2024, 2024)) # nueva

        


