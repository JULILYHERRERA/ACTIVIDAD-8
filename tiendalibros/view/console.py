import sys

from tiendalibros.modelo.tienda_libros import TiendaLibros
from tiendalibros.modelo.existencias_insuficientes_error import ExistenciasInsuficientesError
from tiendalibros.modelo.libro_agotado_error import LibroAgotadoError
from tiendalibros.modelo.libro_existente_error import LibroExistenteError
from tiendalibros.modelo.libro_error import LibroError
from tiendalibros.modelo.libro_faltante_error import LibroFaltanteError

class UIConsola:

    def __init__(self):
        self.tienda_libros: TiendaLibros = TiendaLibros()
        self.opciones = {
            "1": self.adicionar_un_libro_a_catalogo,
            "2": self.agregar_libro_a_carrito_de_compras,
            "3": self.retirar_libro_de_carrito_de_compras,
            "4": self.salir
        }

    @staticmethod
    def salir():
        print("\nGRACIAS POR VISITAR NUESTRA TIENDA DE LIBROS. VUELVA PRONTO")
        sys.exit(0)

    @staticmethod
    def mostrar_menu():
        titulo = "¡Tienda Libros!"
        print(f"\n{titulo:_^30}")
        print("1. Adicionar un libro al catálogo")
        print("2. Agregar libro a carrito de compras")
        print("3. Retirar libro de carrito de compras")
        print("4. Salir de la tienda")
        print(f"{'_':_^30}")

    def ejecutar_app(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")

    def retirar_libro_de_carrito_de_compras(self):
        try:
            isbn = input("Ingrese el isbn del libro que desea eliminar del carrito de compras: ")
            self.tienda_libros.retirar_item_de_carrito(isbn)
        except AttributeError:
            print("El isbn ingresado no pertenece a nada dentro del carrito de compras.")


    def agregar_libro_a_carrito_de_compras(self):
        try:
            isbn = input("Ingrese el isbn del libro que va a agregar al carrito: ")
            cantidad_libros = int(input("Ingrese la cantidad de unidades que desea del libro: "))

            decision = False
            for codigo in self.tienda_libros.catalogo:
                if codigo == isbn:
                    decision = True
            if decision == True:
                self.tienda_libros.agregar_libro_a_carrito(self.tienda_libros.catalogo[isbn], cantidad_libros)
            else:
                print(LibroFaltanteError(isbn))
        except ExistenciasInsuficientesError as err_ie:
            print(f"Error: ExistenciasInsuficientesError - {err_ie}")
        except LibroAgotadoError as err_ae:
            print(f"Error: LibroAgotadoError - {err_ae}")
        except ValueError:
            print("Error: El valor que ingresaste no es un número entero.")

    def adicionar_un_libro_a_catalogo(self):
        try:
            isbn = input("Ingrese el isbn del libro que quiere agregar al catalogo: ")
            titulo = input("Ingrese el titulo del libro que quiere agregar al catalago: ")
            precio = float(input("Ingrese el precio del libro que quiere agregar al catalago (Solo usar el punto en caso de decimales): "))
            existencias = int(input("Ingrese el la cantidad de unidades del libro que quiere agregar al catalago: "))
            self.tienda_libros.adicionar_libro_a_catalogo(isbn, titulo, precio, existencias)

        except LibroExistenteError as err_ee:
            print(f"Error: LibroExistenteError - {err_ee}")
        except ValueError as err:
            print(f"Error: No cumples con el tipo de dato que se pide al ingresar - {err} ")
        except LibroError:
            print("Tiene que ingresar en los campos numeros mayores a 0")