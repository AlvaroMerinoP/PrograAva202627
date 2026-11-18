class Aforo:
    def __init__(self, capacidad, ocupadas = 0):
        self._capacidad = capacidad
        self.__ocupadas = ocupadas

    @property
    def ocupadas(self):
        return self.__ocupadas

    @ocupadas.setter
    def ocupadas(self, valor):
        if not 0 <= valor <= self._capacidad:
            raise ValueError("Las plazas ocupadas deben estar entre 0 y la capacidad")
        self.__ocupadas = valor

    @property
    def libres(self):
        return self._capacidad - self.__ocupadas

a = Aforo(10, 3)
print(a.ocupadas, a.libres)
a.ocupadas = 10
print(a.ocupadas, a.libres)


