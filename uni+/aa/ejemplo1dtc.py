from dataclasses import dataclass

@dataclass
class estudiante:
    id: int
    nombre: str
    email: str
    promedio: float = 0.0
    activo: bool = True

    def __post_init__(self): # va a validar lo que hace init
        #validar promedio
        if not (0.0 <= self.promedio <= 10.0):
            raise ValueError ("El promedio debe estar entre 0 y 10")
        
        #validar correo
        if "@" not in self.email:
            raise ValueError("El correo debe contener @")
        
    def aprobar(self) -> bool:
        return self.promedio >= 5

    def actualizar_promedio(self,nuevo:float):
        if not (0.0 <= nuevo<= 10.0):
            raise ValueError("El nuevo promedio debe estar entrte 0.0 y 10.0")
        self.promedio = nuevo

estudiante1 = estudiante(1,"Juan Perez","juan.perez@gmail.com",8.5)
print(estudiante1.aprobar())

estudiante1.actualizar_promedio(4.5)
print(estudiante1.aprobar())

try:
    e2=estudiante(2,"Luis Flores","no email" )
except ValueError as err:  #as = llama ValueError y renombra  
    print(err)

#dataclass