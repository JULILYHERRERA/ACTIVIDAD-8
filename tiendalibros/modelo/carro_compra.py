from tiendalibros.modelo.item_compra import ItemCompra
from tiendalibros.modelo.libro import Libro

class CarroCompras:
    def __init__(self):
        self.item : list[ItemCompra] = []

    def agregar_item(self,libro:Libro,cantidad_unidades_libro: int) -> ItemCompra:
        objeto = ItemCompra(libro, cantidad_unidades_libro)
        self.item.append(objeto)
        return objeto


    def calcular_total(self) -> float:
        total = 0
        for x in self.item:
            total += x.calcular_subtotal() 
        return total


    def quitar_item(self, isbn)-> list[ItemCompra]:
        decision = False
        for items in self.item:
            if items.libro.isbn == isbn:
                decision = True

        if decision == True:
            self.item = [item for item in self.item if item.libro.isbn != isbn]
            print(f"El libro con isbn: '{isbn}' se ha retirado con exito del carrito de compras. ")
        else:
            print(f"El libro con isbn: {isbn} no esta en el carrito de compras.")
        return self.item

