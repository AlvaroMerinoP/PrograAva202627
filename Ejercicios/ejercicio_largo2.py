from abc import ABC, abstractmethod

class Sesion(ABC):
    def __init__(self, usuario, minutos):
        self.usuario = usuario
        self.minutos = minutos

    @abstractmethod
    def unidades(self):
        pass
    
    def resumen(self):
        return f"{self.usuario} - {self.unidades()} unidades"

class SesionLocal(Sesion):
    def unidades(self):
        return self.minutos

class SesionRemota(Sesion):
    multiplicador = 2

    def __init__(self,usuario, minutos, reconexiones):
        super().__init__(usuario, minutos)
        self.reconexiones = reconexiones

    def unidades(self):
        return self.minutos * self.multiplicador + 3 * self.reconexiones

    @classmethod
    def fijar_multiplicador(cls, valor):
        if valor > 0:
            cls.multiplicador = valor
            return True
        else:
            return False

def consumo_por_usuario(sesiones):
    consumos = {}

    for sesion in sesiones:
        usuario = sesion.usuario
        unidades = sesion.unidades()
        consumos[usuario] = consumos.get(usuario, 0) + unidades

    return consumos

sesiones = [
 SesionLocal("Ana", 12),
 SesionRemota("Luis", 8, 2),
 SesionRemota("Ana", 5, 1),
]
for sesion in sesiones:
 print(sesion.resumen())
print(consumo_por_usuario(sesiones))
print(SesionRemota.fijar_multiplicador(3))
print(SesionRemota.fijar_multiplicador(0))
print(consumo_por_usuario(sesiones))




