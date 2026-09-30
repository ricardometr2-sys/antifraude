from servicios.reglas import reglas
from servicios.reglas import exepciones
from modelo.cliente import Cliente
from modelo.administrador import Administrador
from repositorios.repositorio_usuarios import Repositorio_Usuarios

#Servicios crelacionados con el cliente, registro, inicio de sesion, editar cuenta, etc.
class Servicios_Banco:
    def __init__(self, repositorio_usuarios:Repositorio_Usuarios):
        self.repositorio_usarios=repositorio_usuarios

    def registrar_cliente(self,id_usuario, nombre, fecha_nacimiento, edad, codigo_postal, correo, contraseña):
        cliente=Cliente(id_usuario, nombre, fecha_nacimiento, edad, codigo_postal, correo, contraseña)
        self.repositorio_usarios.agregar_usuario(cliente, 1)
        return 1

    def registrar_administrador(self, id_usuario, nombre, fecha_nacimiento, edad, codigo_postal, correo, contraseña):
        admin=Administrador(id_usuario, nombre, fecha_nacimiento, edad, codigo_postal, correo, contraseña)
        self.repositorio_usarios.agregar_usuario(admin, 2)
        return 1

    def inicio_sesion(self, num_cuenta):
        usuario=self.repositorio_usarios.buscar_usuario(num_cuenta)
        return usuario

    def editar_datos