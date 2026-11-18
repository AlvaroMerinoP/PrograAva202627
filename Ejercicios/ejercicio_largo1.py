class Incidencia:
    def __init__(self, codigo, equipo, minutos):
        self.codigo = codigo
        self.equipo = equipo
        self.minutos = minutos
        self._estado = "abierta"

    @property
    def cerrada(self):
        return self._estado == "cerrada"

    def cerrar(self):
        if self.cerrada:
            return False
        self._estado = "cerrada"
        return True


class RegistroIncidencias:
    def __init__(self):
        self.incidencias = {}

    def registrar(self, incidencia):
        codigo = incidencia.codigo
        if codigo in self.incidencias:
            return False
        self.incidencias[codigo] = incidencia
        return True

    def cerrar(self, codigo):
        incidencia = self.incidencias.get(codigo)
        if incidencia is None:
            return False

        return incidencia.cerrar()

    def minutos_pendientes(self):
        pendientes = {}
        for incidencia in self.incidencias.values():
            if not incidencia.cerrada:
                equipo = incidencia.equipo
                pendientes[equipo] = pendientes.get(equipo, 0) + incidencia.minutos

        return pendientes


registro = RegistroIncidencias()
print(registro.registrar(Incidencia("I1", "PC1", 20)))
registro.registrar(Incidencia("I2", "PC1", 10))
registro.registrar(Incidencia("I3", "PC2", 15))
print(registro.registrar(Incidencia("I1", "PC3", 99)))
print(registro.minutos_pendientes())
print(registro.cerrar("I1"))
print(registro.cerrar("I1"))
print(registro.cerrar("I0"))
print(registro.minutos_pendientes())
