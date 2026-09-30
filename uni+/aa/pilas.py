import random

pila = []

def insertar():
    n = int(input("¿Cuántos números desea insertar? (máximo 200): "))
    
    if n > 200:
        print("No se pueden insertar mas de 200 numeros.")
        return
    
    for i in range(n):
        numero = random.randint(1,100)
        pila.append(numero)
        print("Numero generado:", numero, "Se ha insertado correctamente en la pila")

def quitar():
    if len(pila) == 0:
        print("La pila esta vacia")
    else:
        eliminado = pila.pop()
        print("Elemento eliminado:", eliminado)

def cima():
    if len(pila) == 0:
        print("La pila esta vacia")
    else:
        print("El elemento en la cima:", pila[-1])

def consultar():
    if len(pila) == 0:
        print("La pila esta vacia")
    else:
        print("Los elementos de la pila son:")
        for elemento in range(len(pila)-1,-1,-1):
            print(pila[elemento])

def menu():
    opcion = 0
    
    while True:
        print("______________ MENU PARA PILA __________________")
        print("1. Insertar")
        print("2. Quitar")
        print("3. Cima")
        print("4. Consultar")
        print("5. Salir")
        
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            insertar()
        elif opcion == 2:
            quitar()
        elif opcion == 3:
            cima()
        elif opcion == 4:
            consultar()
        elif opcion == 5:
            print("Programa terminado.")
            break
        else:
            print("Opción inválida")

menu()