from modelo.administrador import Administrador
from repositorios.repositorio_usuarios import Repositorio_Usuarios
from repositorios.repositorio_transacciones import Repositorio_Transacciones
from modelo.transacciones import Transacciones
from reglas.reglas import Validaciones


class Servicios_Administrador:
    def __init__(self, administrador:Administrador, rep_usuarios:Repositorio_Usuarios, rep_transacciones:Repositorio_Transacciones):
        self.administrador=administrador
        self.rep_usuarios=rep_usuarios
        self.rep_transacciones=rep_transacciones
        self.reglas=Validaciones()

    def buscar_cliente(self, correo):
        try:
            cliente=self.rep_usuarios.buscar_usuario(correo)
            if cliente:
                id_tr="100"+str(len(self.rep_transacciones+1))
                transaccion=Transacciones(id_tr, "Administrador", f"Buscaste al cliente {cliente.nombre}")
                self.rep_transacciones.agregar_transaccion(transaccion)
                return cliente
            return 0
        except:
            return "Cliente no encontrado"

    def mostrar_clientes(self,):
        self.rep_usuarios.obtener_clientes(1)
        id_tr="100"+str(len(self.rep_transacciones+1))
        transaccion=Transacciones(id_tr, "Administrador", "Mostrar clientes")
        self.rep_transacciones.agregar_transaccion(transaccion)
