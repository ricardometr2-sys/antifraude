import random

pila = []

#DEFINIMOS LA FUNCIÓN PARA INSERTAR ELEMENTOS EN LA PILA
def insertar():
    n = int(input("Ingrese la cantidad de elementos a insertar, con un máximo de 200: "))
    if n > 200:
        print("El número ingresado excede el máximo permitido. Por favor, ingrese un número menor o igual a 200.")
        return
    
    for i in range(n):
        elemento = random.randint(1, 100)
        pila.append(elemento)
        print("Número insertado en la pila:" , elemento)

#DEFINIMOS LA FUNCIÓN PARA ELIMINAR ELEMENTOS DE LA PILA
def quitar():
    if len(pila) == 0:
        print("La pila está vacía. No hay elementos para eliminar.")
    else:
        elemento_eliminado = pila.pop()
        print(f"Elemento {elemento_eliminado} eliminado de la pila.")

#DEFINIMOS LA FUNCIÓN PARA MOSTRAR EL ELEMENTO EN LA CIMA DE LA PILA
def cima():
    if len(pila) == 0:
        print("La pila está vacía. No hay elementos en la cima.")
    else:
        print(f"El elemento en la cima de la pila es: {pila[-1]}")

#DEFINIMOS LA FUNCIÓN PARA CONSULTAR TODOS LOS ELEMENTOS DE LA PILA
def consultar():
    if len(pila) == 0:
        print("La pila está vacía. No hay elementos para consultar.")
    else:
        print("Elementos en la pila:")
        for elemento in range(len(pila)-1, -1, -1):
            print(pila[elemento])


#DEFINIMOS LA FUNCIÓN PARA SALIR DEL PROGRAMA
def salir():
    print("Saliendo del programa. ¡Hasta luego!")
    exit()

print("Bienvenido al programa de pilas.")
p = input("Desea iniciar la pila? (s/n): ")
if p.lower() == "s":
    insertar()
else:
    print("Pila no iniciada. Saliendo del programa.")
    exit()

if pila is not None:
    while pila is not None:
        print("Menú de opciones:")
        print("""
    1. Eliminar elemento de la pila
    2. Mostrar elemento en la cima de la pila
    3. Consultar elementos de la pila
    4. Editar elementos de la pila
    5. Salir del programa
    """)
        opcion = input("Seleccione una opción del 1 al 5: ")

        if opcion == "1":
            quitar()  
        elif opcion == "2":
            cima()
        elif opcion == "3":
            consultar()
        elif opcion == "4":
            insertar()
        elif opcion == "5":
            salir()
        else:
            print("Opción no válida, seleccione un número del 1 al 5.")