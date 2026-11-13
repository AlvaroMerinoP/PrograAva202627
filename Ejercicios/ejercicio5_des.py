class Paquete:
    def __init__(self, codigo):
        self.codigo = codigo
    def resumen(self):
        return self.codigo

class ConEtiqueta:
    def resumen(self):
        return f"[{super().resumen()}]"

class PaqueteUrgente(ConEtiqueta, Paquete):
    def __init__(self, codigo, prioridad):
        super().__init__(codigo)
        self.prioridad = prioridad

    def resumen(self):
        etiqueta = super().resumen()
        return f"{etiqueta} prioridad {self.prioridad}"
   
print(PaqueteUrgente("P7", 2).resumen())

