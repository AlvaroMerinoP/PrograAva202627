class Dispositivo:
    def __init__(self, nombre):
        self.nombre = nombre

    def descripcion(self):
        return self.nombre


class Router(Dispositivo):
    def __init__(self,nombre, puerto):
        super().__init__(nombre)
        self.puerto = puerto

    def descripcion(self):
        return f"{super().descripcion()} ({self.puerto} puertos)"

dispositivos = [Dispositivo("PC1"), Router("R1", 4)]
for dispositivo in dispositivos:
    print(dispositivo.descripcion())

