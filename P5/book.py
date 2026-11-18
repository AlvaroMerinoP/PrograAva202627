class Book:
    def __init__(self, titulo, autor, isbn, estado = "prestado"):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__estado = estado
