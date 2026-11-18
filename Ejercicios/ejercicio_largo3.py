import numpy as np

class MatrizTrafico:
    TIPO_DATO = np.float32
    def __init__ (self):
        self._matriz = None

    @property
    def matriz(self):
        return self._matriz

    def existe(self):
        if self._matriz:
            return True
    @property
    def forma(self):
        if not self.existe():
            return None
        return self._matriz.shape

    def crear_matriz2D(self, filas, columnas):
        if filas < 1 or columnas < 1:
            raise ValueError("Las dimensiones deben ser positivas.")
        self._matriz = np.zeros((filas,columnas), dtype=self.TIPO_DATO)

    def crear_matriz1D(self, n):
        self.crear_matriz2D(1, n)

    @classmethod
    def desde_filas(cls, filas):
        if not filas:
            raise ValueError("La lista de filas está vacia.")
        columnas = len(filas[0])
        for fila in filas:
            if not fila or len(fila) != columnas:
                raise ValueError("Todas las filas deben tener la misma longitud.")

        matriz = cls()
        matriz.crear_matriz2D(len(filas), columnas)
        matriz._matriz[:,:] = filas

        return matriz

    def como_array(self):
        if not self.existe():
            raise ValueError("La matriz todavía no está creada.")

        return self._matriz().copy()

    @staticmethod
    def mismas_dimensiones(m1, m2):
        return m1.existe() and m2.existe() and m1.forma == m2.forma

    def sumar_matrices(self, otra):






def main():

if __name__ == "__main__":
    main()
