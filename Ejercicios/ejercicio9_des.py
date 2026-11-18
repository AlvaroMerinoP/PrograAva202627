from abc import ABC,abstractmethod

class Transferencia(ABC):
    def __init__(self, tamano, caudal):
        self.tamano = tamano
        self.caudal = caudal

    @abstractmethod
    def tiempo():
        pass

class Directa(Transferencia):
    def tiempo(self):
        return self.tamano/self.caudal

class ConEspera(Transferencia):
    def __init__(self, tamano, caudal, espera):
        super().__init__(tamano, caudal)
        self.espera = espera

   
    def tiempo(self):
        return self.tamano/self.caudal + self.espera

def tiempo_total(transferencias):
    total = 0.0
    for transferencia in transferencias:
        total += transferencia.tiempo()
    return total

envios = [Directa(20, 5), ConEspera(12, 3, 2)]
for envio in envios:
 print(envio.tiempo())
print(tiempo_total(envios))

