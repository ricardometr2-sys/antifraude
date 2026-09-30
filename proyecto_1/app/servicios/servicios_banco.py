from reglas.reglas import Validaciones
from modelo.cliente import Cliente
from modelo.administrador import Administrador
from repositorios.repositorio_usuarios import Repositorio_Usuarios

#Servicios crelacionados con el cliente, registro, inicio de sesion, editar cuenta, etc.
class Servicios_Banco:
    def __init__(self, repositorio_usuarios:Repositorio_Usuarios):
        self.repositorio_usarios=repositorio_usuarios
        self.reglas=Validaciones()

    def registrar_cliente(self,id_usuario, nombre, fecha_nacimiento, codigo_postal, correo, contraseña):
        while True:
            self.reglas.validar_cadena_vacia(id_usuario)
            self.reglas.validar_cadena_vacia(nombre)
            self.reglas.validar_cadena_vacia(fecha_nacimiento)
            self.reglas.validar_cadena_vacia(codigo_postal)
            self.reglas.validar_cadena_vacia(correo)
            break
        cliente=Cliente(id_usuario, nombre, fecha_nacimiento, codigo_postal, correo, contraseña)
        self.repositorio_usarios.agregar_usuario(cliente, 1)
        

    def registrar_administrador(self, id_usuario, nombre, fecha_nacimiento, codigo_postal, correo, contraseña):
        while True:
            self.reglas.validar_cadena_vacia(id_usuario)
            self.reglas.validar_cadena_vacia(nombre)
            self.reglas.validar_cadena_vacia(fecha_nacimiento)
            self.reglas.validar_cadena_vacia(codigo_postal)
            self.reglas.validar_cadena_vacia(correo)
            break     
        admin=Administrador(id_usuario, nombre, fecha_nacimiento, codigo_postal, correo, contraseña)
        self.repositorio_usarios.agregar_usuario(admin, 2)
        return 1

    def inicio_sesion(self, num_cuenta):
        usuario=self.repositorio_usarios.buscar_usuario(num_cuenta)
        return usuario

    def editar_datos(self, dato_nuevo, tipo):
        if tipo==1:
            usuario