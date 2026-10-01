from app.modelo.administrador import Administrador
from app.repositorios.repositorio_clientes import Repositorio_Clientes
from app.repositorios.repositorio_transacciones import Repositorio_Transacciones
from app.modelo.transacciones import Transacciones
from app.reglas.reglas import Validaciones


class Servicios_Administrador:
    def __init__(self, administrador:Administrador, rep_usuarios:Repositorio_Clientes):
        self.administrador=administrador
        self.rep_usuarios=rep_usuarios
        self.reglas=Validaciones()

    def buscar_cliente(self, correo):
        try:
            cliente=self.rep_usuarios.buscar_usuario(correo)
            if cliente:
                id_tr="100"+str(len(self.rep_transacciones+1))
                transaccion=Transacciones(id_tr, "Administrador", f"Buscaste al cliente {cliente.nombre}")
                self.administrador.rep_transacciones.agregar_transaccion(transaccion)
                return cliente
            return 0
        except:
            return "Cliente no encontrado"

    def mostrar_clientes(self,):
        self.rep_usuarios.obtener_clientes(1)
        id_tr="100"+str(len(self.rep_transacciones+1))
        transaccion=Transacciones(id_tr, "Administrador", "Mostrar clientes")
        self.rep_transacciones.agregar_transaccion(transaccion)
