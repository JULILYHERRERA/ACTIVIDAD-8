from tiendalibros.modelo.libro import Libro
class ItemCompra:

    def __init__(self, libro, cantidad_de_tipo_libro : int):
        self.libro : Libro = libro
        self.cantidad_de_tipo_libro = cantidad_de_tipo_libro

    def calcular_subtotal(self):
        subtotal = self.cantidad_de_tipo_libro * self.libro.precio
        return subtotal
