from app.reglas.reglas import Validaciones
from app.modelo.cliente import Cliente
from app.modelo.administrador import Administrador
from app.repositorios.repositorio_clientes import Repositorio_Clientes
from app.repositorios.repositorio_transacciones import Repositorio_Transacciones
from app.repositorios.repositorio_cuentas import Repositorio_Cuentas

#Servicios crelacionados con el cliente, registro, inicio de sesion, editar cuenta, etc.
class Servicios_Banco:
    def __init__(self, repositorio_usuarios:Repositorio_Clientes):
        self.repositorio_usuarios=repositorio_usuarios
        self.reglas=Validaciones()

    def registrar_cliente(self,id_usuario, nombre, correo, fecha_nacimiento, codigo_postal, contraseña):
        self.reglas.validar_cadena_vacia(id_usuario)
        self.reglas.validar_cadena_vacia(nombre)
        self.reglas.validar_cadena_vacia(fecha_nacimiento)
        self.reglas.validar_cadena_vacia(codigo_postal)
        self.reglas.validar_cadena_vacia(correo)
        transacciones_rep=Repositorio_Transacciones()
        cliente=Cliente(id_usuario, nombre, correo, fecha_nacimiento, codigo_postal, contraseña, transacciones_rep)
        self.repositorio_usuarios.agregar_usuario(cliente)
        return 1
        

    def registrar_administrador(self, id_usuario, nombre, correo, fecha_nacimiento, codigo_postal, contraseña):     
        self.reglas.validar_cadena_vacia(id_usuario)
        self.reglas.validar_cadena_vacia(nombre)
        self.reglas.validar_cadena_vacia(fecha_nacimiento)
        self.reglas.validar_cadena_vacia(codigo_postal)
        self.reglas.validar_cadena_vacia(correo)
            
        transacciones_rep=Repositorio_Transacciones()
        admin=Administrador(id_usuario, nombre, correo, fecha_nacimiento, codigo_postal, contraseña, transacciones_rep)
        self.repositorio_usuarios.agregar_usuario(admin)
        return 1

    def inicio_sesion(self, correo):
        try:
            usuario=self.repositorio_usuarios.buscar_usuario(correo)
            return usuario
        except:
            return False

    def dar(self):
        return self.repositorio_usuarios.dar_primer_usuario()
