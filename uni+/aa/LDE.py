import gc

from numpy import rint

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None 


class LDE:
    def __init__(self):
        self.inicio = None

    #Verificamos lista vacia
    def listaVacia(self):
        if self.inicio == None:
            return 1 #la lista esta vacia
        else:
            return 0 #tiene almenos un elemento

    # Insertar según DatoDer y Valor
    def insertar(self, datoDer, valor):
        nuevo = Nodo(valor)

        # Lista vacía
        if(self.listaVacia()==1):
            self.inicio = nuevo
            print(f"Lista vacía. Se insertó {valor} como primer nodo")
            return

        # Buscar DatoDer
        aux = self.inicio
        while aux and aux.dato != datoDer:
            aux = aux.siguiente

        if aux is None:
            print("Error: DatoDer no existe en la lista")
            return

        # Insertar después de DatoDer
        nuevo.siguiente = aux.siguiente
        nuevo.anterior = aux

        if aux.siguiente:
            aux.siguiente.anterior = nuevo

        aux.siguiente = nuevo

        print(f"Elemento {valor} insertado después de {datoDer}")

    # Desplegar de cabeza a final

    def mostrarAdelante(self):
        if(self.listaVacia()==1):
            print("Lista vacía")
        else:
            aux = self.inicio
            print("Cabeza -> Final:")
            while aux:
                print(aux.dato, end=" <-> ")
                aux = aux.siguiente
            print("None")

    # Desplegar de final a cabeza
    def mostrarAtras(self):
        if(self.listaVacia()==1):
            print("Lista vacía")
        else:
            aux = self.inicio
            while aux.siguiente:
                aux = aux.siguiente

            print("Final -> Cabeza:")
            while aux:
                print(aux.dato, end=" <-> ")
                aux = aux.anterior
            print("None")

    # Programa principal con menú
def menu():
    lista = LDE()

    while True:
        print("\n--- MENÚ LISTA DOBLEMENTE ENLAZADA ---")
        print("1. Insertar")
        print("2. Desplegar de cabeza a final")
        print("3. Desplegar de final a cabeza")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            if lista.listaVacia():
                valor = input("Lista vacía, ingresa el primer valor: ")
                lista.insertar(None, valor)
            else:
                datoDer = input("Ingresa el DatoDer (nodo existente): ")
                valor = input("Ingresa el nuevo valor: ")
                lista.insertar(datoDer, valor)

        elif opcion == "2":
            lista.mostrarAdelante()

        elif opcion == "3":
            lista.mostrarAtras()


        elif opcion == "4":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu()