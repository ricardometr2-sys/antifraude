# Practica: Pilas y Colas dinamicas
# Nombre: Imanol Dominguez Vences
# Fecha: 29/04/2026

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.cima = None
        self.tamaño = 0

    def push(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cima # El nuevo nodo apunta a la cima actual
        self.cima = nuevo # La cima ahora es el nuevo nodo
        self.tamaño = self.tamaño + 1

    def pop(self):
        if self.cima is None:
            print("Pila vacía. No se puede hacer pop.")
            return None
        dato = self.cima.dato # Guardamos el dato de la cima
        self.cima = self.cima.siguiente # La cima ahora es el siguiente nodo
        self.tamaño = self.tamaño - 1
        return dato
    
    def ver_cima(self):
        if self.cima is None:
            return None
        return self.cima.dato
    
    def esta_vacia(self):
        return self.cima is None
    
print ("===  Prueba dePila ===")
pila = Pila()
pila.push(10)
pila.push(20)
pila.push(30)
print("Cima de la pila:", pila.ver_cima()) #DEBE IMPRIMIR 30
print("Saco:", pila.pop()) #DEBE IMPRIMIR 30
print("Saco:", pila.pop()) #DEBE IMPRIMIR 20
print("Cima de la pila:", pila.ver_cima()) #DEBE IMPRIMIR 10
print("¿Está vacía?", pila.esta_vacia()) #DEBE IMPRIMIR False


class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamaño = 0

    def encolar(self, dato):
        nuevo = Nodo(dato)
        if self.frente is None:
             # Si la cola está vacía: el nuevo es frente y final
            self.frente = nuevo
            self.final = nuevo
        else:
            self.final.siguiente = nuevo # El final actual apunta al nuevo nodo
            self.final = nuevo # El nuevo nodo ahora es el final
        self.tamaño = self.tamaño + 1

    def desencolar(self):
        if self.frente is None:
            print("Cola vacía. No se puede hacer desencolar.")
            return None
        dato = self.frente.dato # Guardamos el dato del frente
        self.frente = self.frente.siguiente # El frente ahora es el siguiente nodo
        if self.frente is None: # Si la cola quedó vacía, también actualizamos el final
            self.final = None
        self.tamaño = self.tamaño - 1
        return dato
    
    def ver_frente(self):
        if self.frente is None:
            return None
        return self.frente.dato
    
    def esta_vacia(self):
        return self.frente is None
    
print("\n=== Prueba de Cola ===")
c=Cola()
c.encolar("Ana")
c.encolar("Luis")
c.encolar("Maria")
print("Frente de la cola:", c.ver_frente()) #DEBE IMPRIMIR "Ana"
print("Atiendo a:", c.desencolar()) #DEBE IMPRIMIR "Ana"
print("Atiendo a:", c.desencolar()) #DEBE IMPRIMIR "Luis"
print("Frente de la cola:", c.ver_frente()) #DEBE IMPRIMIR "Maria"


class Invertir_palabra:
    def __init__(self):
        self.pila = Pila()

    def invertir(self, palabra):
        for letra in palabra:
            self.pila.push(letra)
        
        resultado = ""
        while not self.pila.esta_vacia():
            resultado += self.pila.pop()
        
        return resultado
    
print("\n=== RETO A ===")
invertir = Invertir_palabra()
Palabra = input("Ingrese una palabra para invertir: ")
print(invertir.invertir(Palabra))