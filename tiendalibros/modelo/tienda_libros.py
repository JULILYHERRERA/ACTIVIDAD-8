from tiendalibros.modelo.libro import Libro
from tiendalibros.modelo.carro_compra import CarroCompras
from tiendalibros.modelo.libro_existente_error import LibroExistenteError
from tiendalibros.modelo.libro_agotado_error import LibroAgotadoError
from tiendalibros.modelo.existencias_insuficientes_error import ExistenciasInsuficientesError
from tiendalibros.modelo.libro_error import LibroError

class TiendaLibros:
    def __init__(self) -> None:
        self.catalogo : dict[str:Libro] = {} 
        self.carrito : CarroCompras = CarroCompras()


    def adicionar_libro_a_catalogo(self, isbn:str, titulo:str,precio:float,existencias:int)-> Libro:
            libro = Libro(isbn,titulo,precio,existencias)
            if existencias < 0 or precio < 0:
                raise LibroError(libro)
            for clave in self.catalogo:
                if clave == isbn:
                   raise LibroExistenteError(self.catalogo[clave])
            self.catalogo[isbn] = libro
            print(f"El libro de isbn: '{isbn}', titulo: '{titulo}' con un precio de: '{precio}' y con una cantidad de existencias de: '{existencias}' se ha adicionado correctamente al catalogo")
            return libro


    def agregar_libro_a_carrito(self,libro:Libro,cantidad_unidades_a_comprar:int):
        if libro.existencias == 0:
            raise LibroAgotadoError(libro)
        if libro.existencias < cantidad_unidades_a_comprar:
            raise ExistenciasInsuficientesError(libro, cantidad_unidades_a_comprar)
        self.carrito.agregar_item(libro, cantidad_unidades_a_comprar)
        print(f"El libro de isbn: '{libro.isbn}' se ha agregado correctamente al carrito de compras") 


    def retirar_item_de_carrito(self,isbn:str):
        self.carrito.quitar_item(isbn)
