from collections import namedtuple

Estudiante = namedtuple ("Estudiante", ["cuenta", "nombre", "edad", "carrera", "promedio"])

def mostrarEstudiantes(lista):
    if not lista:
        print("Lista vacia")
        return
    
    for alumno in lista:
        print("___________________________________________")
        print(f"Cuenta: {alumno.cuenta}")
        print(f"Nombre: {alumno.nombre}")
        print(f"Edad: {alumno.edad}")
        print(f"Carrera: {alumno.carrera}")
        print(f"Promedio: {alumno.promedio}")
    print ("*********************************************************************")


def mostrarEstudiantesPromedio(lista):
    if not lista:
        print("Lista vacia")
        return
    
    for alumno in lista:
        if alumno.promedio  >= 8.5:
            print("___________________________________________")
            print(f"Cuenta: {alumno.cuenta}")
            print(f"Nombre: {alumno.nombre}")
            print(f"Edad: {alumno.edad}")
            print(f"Carrera: {alumno.carrera}")
            print(f"Promedio: {alumno.promedio}")
    print ("*********************************************************************")


estudiantes=[
    Estudiante(2521563,"Imanol Dominguez", 18 , "Inteligencia Artificial",8.4),
    Estudiante(2521564,"Imanol Vences", 18 , "Inteligencia Artificial",8.6),
    Estudiante(2521565,"Pedro Dominguez", 18 , "Inteligencia Artificial",7.3),
    Estudiante(2521566,"Pedro Vences", 18 , "Inteligencia Artificial",9.6),
    Estudiante(2521567,"Pancho Villa", 18 , "Inteligencia Artificial",6.4)
]

mostrarEstudiantes(estudiantes)
mostrarEstudiantesPromedio(estudiantes)