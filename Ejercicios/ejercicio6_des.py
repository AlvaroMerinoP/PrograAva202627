class Lectura:
    def __init__(self, enlace, milisegundos):
        self.enlace = enlace
        self.milisegundos = milisegundos

    @classmethod
    def desde_texto(cls, texto):
        text = texto.split("|")

        if len(text) != 2:
            return None
        enlace = text[0].strip()
        medida = text[1].strip()

        if not enlace or not medida.isdecimal():
            return None

        return cls(enlace, int(medida))

class LecturaLocal(Lectura):
 pass
r = LecturaLocal.desde_texto(" R1 | 45 ")
print(type(r).__name__, r.enlace, r.milisegundos)
print(Lectura.desde_texto("R1|-3"))
print(Lectura.desde_texto("R1|3|2"))
        

