class Bateria:
    umbral_bajo = 20

    def __init__(self, porcentaje):
        self.porcentaje = porcentaje

    @staticmethod
    def porcentaje_valido(valor): 
        if 0<= valor <= 100:
            return valor
    @classmethod
    def fijar_umbral(cls, valor):
        if not cls.porcentaje_valido(valor):
            return False
        
        cls.umbral_bajo = valor
        return True

    def necesita_carga(self):
        return self.porcentaje <= self.umbral_bajo

b = Bateria(30)
print(b.necesita_carga())
print(Bateria.fijar_umbral(30))
print(b.necesita_carga())
print(Bateria.fijar_umbral(110))
print(Bateria.umbral_bajo)
        
