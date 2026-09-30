# ==============================
# SISTEMA DE REGISTRO DE EMPLEADOS
# ==============================

def agregar_empleado(lista, empleado):
    # Validar ID duplicado
    for e in lista:
        if e["id"] == empleado["id"]:
            print("Error: ID duplicado.")
            return
    
    # Validaciones
    if empleado["edad"] < 18:
        print("Error: El empleado debe ser mayor de edad.")
        return
    
    if empleado["salario"] < 0:
        print("Error: El salario no puede ser negativo.")
        return
    
    lista.append(empleado)
    print("Empleado agregado correctamente.")


def mostrar_empleados(lista):
    if not lista:
        print("No hay empleados registrados.")
        return
    
    for e in lista:
        print("----------------------------")
        print(f"ID: {e['id']}")
        print(f"Nombre: {e['nombre']}")
        print(f"Edad: {e['edad']}")
        print(f"Puesto: {e['puesto']}")
        print(f"Salario: {e['salario']}")
        print(f"Activo: {e['activo']}")
    print("----------------------------")


def buscar_empleado(lista, id_buscar):
    for e in lista:
        if e["id"] == id_buscar:
            return e
    return None


def actualizar_salario(lista, id_buscar, nuevo_salario):
    empleado = buscar_empleado(lista, id_buscar)
    
    if empleado is None:
        print("Empleado no encontrado.")
        return
    
    if nuevo_salario <= 0:
        print("Salario inválido.")
        return
    
    empleado["salario"] = nuevo_salario
    print("Salario actualizado correctamente.")


def eliminar_empleado(lista, id_buscar):
    empleado = buscar_empleado(lista, id_buscar)
    
    if empleado is None:
        print("Empleado no encontrado.")
        return
    
    empleado["activo"] = False
    print("Empleado desactivado (borrado lógico).")


# ==============================
# PRUEBA DEL SISTEMA
# ==============================

empleados = []

agregar_empleado(empleados, {
    "id": 1,
    "nombre": "Ana López",
    "edad": 25,
    "puesto": "Desarrollador",
    "salario": 15000.0,
    "activo": True
})

agregar_empleado(empleados, {
    "id": 2,
    "nombre": "Carlos Pérez",
    "edad": 30,
    "puesto": "Analista",
    "salario": 12000.0,
    "activo": True
})

mostrar_empleados(empleados)

actualizar_salario(empleados, 1, 17000.0)

eliminar_empleado(empleados, 2)

mostrar_empleados(empleados)

#listas o diccionarios