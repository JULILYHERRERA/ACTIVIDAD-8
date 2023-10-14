from tiendalibros.modelo.libro import Libro
from tiendalibros.modelo.libro_error import LibroError


class LibroAgotadoError(LibroError):


    def __init__(self, libro: Libro):
        super().__init__(libro)


    def __str__(self) -> str:
        return (f"El libro  '{self.libro.titulo}' e isbn: '{self.libro.isbn}'  está agotado")